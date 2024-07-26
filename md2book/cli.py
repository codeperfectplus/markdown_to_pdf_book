import sys
import argparse
from pprint import pprint

sys.path.append('.')

from md2book.pdf_convertor import MarkdownToPDFConverter

# Define the version of your script
__version__ = '1.0.0'

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown files to PDF using Pandoc.')
    parser.add_argument('-v', '--version', action='version', version=__version__)
    parser.add_argument('-i', '--input', help='Input directory containing Markdown files', required=True)
    parser.add_argument('-o', '--output', help='Output directory for PDF files', default='output')
    parser.add_argument('-t', '--template', help='LaTeX template file for Pandoc', default='md2book/template/template.tex')
    parser.add_argument('--single', help='Combine all Markdown files into a single PDF', action='store_true')
    
    args = parser.parse_args()

    input_dir = args.input
    output_dir = args.output
    template_file = args.template

    if input_dir:
        converter = MarkdownToPDFConverter(input_dir, output_dir, template_file)
        if args.single:
            converter.combine_markdown_files()
        else:
            converter.batch_convert_markdown_to_pdf()
    else:
        pprint('Type `cli.py -h` for help')

if __name__ == '__main__':
    main()
