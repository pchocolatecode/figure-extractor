# 📦 Figure Extractor

A lightweight Python tool to extract figure captions and labels from LaTeX `.tex` files. It also checks for duplicate labels and outputs a clean summary.

## 🔧 Usage

```bash
python caption.py -i inputs/sample.tex -o outputs/figure_summary.txt
```

### Arguments

- `-i`, `--input`: Path to your LaTeX `.tex` file (required)
- `-o`, `--output`: Path to save the summary file (optional, defaults to `outputs/figure_summary.txt`)

## 📂 Project Structure

```
figure-extractor/
├── caption.py
├── inputs/
│   └── sample.tex
├── outputs/
│   └── figure_summary.txt
├── README.md
└── requirements.txt
```

## ✅ Features

- Extracts `\caption{}` and `\label{}` from LaTeX `figure` environments
- Detects duplicate labels
- Outputs a numbered summary of figures

## 🧪 Example Output

```
1. This is the first figure.
    [fig:first]

2. This is the second figure.
    [fig:second]

3. This is a duplicate label figure.
    [fig:first]
```

## 📜 License

MIT — feel free to use, modify, and share.
```
