import re
import argparse
from collections import defaultdict
from pathlib import Path

def extract_figures(tex_content):
    figure_blocks = re.findall(r'\\begin{figure}.*?\\end{figure}', tex_content, re.DOTALL)
    results = []
    label_counts = defaultdict(int)

    for block in figure_blocks:
        caption_match = re.search(r'\\caption{(.*?)}', block, re.DOTALL)
        label_match = re.search(r'\\label{(.*?)}', block)

        if caption_match and label_match:
            caption = ' '.join(caption_match.group(1).split())
            label = label_match.group(1)
            label_counts[label] += 1
            results.append((caption, label))

    return results, label_counts

def main():
    parser = argparse.ArgumentParser(description="Extract figure captions and labels from a LaTeX file.")
    parser.add_argument("-i", "--input", required=True, help="Path to input .tex file")
    parser.add_argument("-o", "--output", default="outputs/figure_summary.txt", help="Path to output summary file")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"❌ Error: File '{input_path}' not found.")
        return

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            tex_content = f.read()

        figures, label_counts = extract_figures(tex_content)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as out:
            for i, (caption, label) in enumerate(figures, start=1):
                out.write(f"{i}. {caption}\n\t[{label}]\n\n")

        print(f"✅ Extracted {len(figures)} figures to '{output_path}'.")

        duplicates = [label for label, count in label_counts.items() if count > 1]
        if duplicates:
            print("\n⚠️ Duplicate labels detected:")
            for label in duplicates:
                print(f"  - '{label}' appears {label_counts[label]} times")
        else:
            print("\n🎉 No duplicate labels found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
