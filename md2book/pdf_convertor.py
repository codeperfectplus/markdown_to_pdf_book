import os
import subprocess
import argparse


class MarkdownToPDFConverter:
    def __init__(self, input_dir, output_dir='output', template_file='template.tex'):
        self.input_dir = input_dir
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.template_file = template_file

    def convert_markdown_to_pdf(self, input_md_file, output_pdf_file):
        # Use Pandoc to convert Markdown to PDF with xelatex
        cmd = [
            'pandoc',
            '--pdf-engine=xelatex',
            '--template=' + self.template_file,
            input_md_file,
            '-o',
            output_pdf_file,
            '--verbose'
        ]
        try:
            result = subprocess.run(cmd, check=True, stderr=subprocess.PIPE, text=True)
            print(f'Converted {input_md_file} to {output_pdf_file}')
        except subprocess.CalledProcessError as e:
            print(f'Error converting {input_md_file} to PDF:')
            print(f'Error message: {e.stderr}')
            print(f'Command: {" ".join(cmd)}')

    def combine_markdown_files(self):
        combined_md_file_path = os.path.join(self.output_dir, 'combined.md')
        with open(combined_md_file_path, 'w') as outfile:
            for root, dirs, files in os.walk(self.input_dir):
                for file in sorted(files):
                    if file.endswith('.md') and file not in ['README.md', 'SUMMARY.md', 'combined.md']:
                        input_md_file = os.path.join(root, file)
                        with open(input_md_file, 'r', encoding='utf-8') as infile:
                            outfile.write(infile.read() + '\n\n')
        print(f'Combined Markdown files into {combined_md_file_path}')

        output_pdf_file = os.path.join(self.output_dir, 'combined.pdf')
        self.convert_markdown_to_pdf(combined_md_file_path, output_pdf_file)

    def batch_convert_markdown_to_pdf(self):
        os.makedirs(self.output_dir, exist_ok=True)

        for root, dirs, files in os.walk(self.input_dir):
            for file in sorted(files):
                if file.endswith('.md'):
                    input_md_file = os.path.join(root, file)
                    rel_path = os.path.relpath(input_md_file, self.input_dir)
                    output_subdir = os.path.dirname(rel_path)
                    output_subdir_path = os.path.join(self.output_dir, output_subdir)
                    os.makedirs(output_subdir_path, exist_ok=True)

                    output_pdf_file = os.path.join(self.output_dir, rel_path.replace('.md', '.pdf'))

                    self.convert_markdown_to_pdf(input_md_file, output_pdf_file)


def main():
    parser = argparse.ArgumentParser(description='Convert Markdown files to PDF.')
    parser.add_argument('-i', '--input_dir', type=str, help='Directory containing Markdown files.', required=True)
    parser.add_argument('-o', '--output_dir', type=str, help='Directory to save PDF files.', default='PDFs')
    parser.add_argument('-t', '--template_file', type=str, help='Path to LaTeX template file.', default='md2book/template/template.tex')
    parser.add_argument('--single', action='store_true', help='Combine all Markdown files into one PDF.')

    args = parser.parse_args()

    converter = MarkdownToPDFConverter(args.input_dir, args.output_dir, args.template_file)
    if args.single:
        converter.combine_markdown_files()
    else:
        converter.batch_convert_markdown_to_pdf()

if __name__ == "__main__":
    main()