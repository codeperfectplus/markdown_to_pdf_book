# Markdown To Pdf Book Converter

This is a simple python script that converts a markdown file to a pdf book. It uses the `pandoc` library to convert the markdown file to a pdf file.

## Requirements

- Python 3
- Pandoc

## Usage

To use the script, simply run the following command:

### For single book

```bash
python3 markdown_to_pdf.py <input_file> <output_file> --single
```

### For multiple books

```bash
python3 markdown_to_pdf.py <input_file> <output_file>
```


Where `<input_file>` is the path to the markdown file and `<output_file>` is the path to the pdf file and `--single` is an optional argument to convert a single markdown file to a pdf file.

