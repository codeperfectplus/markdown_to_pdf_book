
import sys
import random
import argparse
from pprint import pprint

sys.path.append('.')

from src.pdf_convertor import MarkdownToPDFConverter

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version', action='version', version=__version__)
parser.add_argument('-i', '--input', help='Input directory containing Markdown files', required=True)
parser.add_argument('-o', '--output', help='Output directory for PDF files', default='output')
parser.add_argument('-t', '--template', help='LaTeX template file for Pandoc', default='template.tex')
parser.add_argument('-c', '--combine', help='Combine all Markdown files into a single PDF', action='store_true')
args = parser.parse_args()

input_dir = args.input
output_dir = args.output
template_file = args.template
is_combine = args.combine



def main():
    if args.input:
        converter = MarkdownToPDFConverter(input_dir, output_dir, template_file)
        if is_combine:
            converter.combine_markdown_files()
        else:
            converter.batch_convert_markdown_to_pdf()
    else:
        pprint('Type `rp -h` for help')


if __name__ == '__main__':
    main()