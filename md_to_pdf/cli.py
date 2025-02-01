"""
MarkFlow - Modern Markdown to PDF Converter

Copyright (c) 2025 Raja Namdeo <cse.rajanamdeo@gmail.com>
All rights reserved.

This file is part of MarkFlow, a modern Markdown to PDF converter.
For more information, visit: [website coming soon]

Created by: Raja Namdeo
Email: cse.rajanamdeo@gmail.com
Role: Software Developer

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""
"""
Command-line interface for MarkFlow - Markdown to PDF converter
"""
import click
from pathlib import Path
from .core import convert_to_pdf

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--style', '-s', help='CSS style file for customization')
def cli(input_file, output_file, style=None):
    """Convert Markdown files to beautifully formatted PDFs.
    
    INPUT_FILE: Path to the input Markdown file
    OUTPUT_FILE: Path for the output PDF file
    """
    try:
        convert_to_pdf(
            input_file=str(Path(input_file).resolve()),
            output_file=str(Path(output_file).resolve()),
            style_file=style
        )
        click.echo(f"✨ Successfully converted {input_file} to {output_file}")
    except Exception as e:
        click.echo(f"❌ Error: {str(e)}", err=True)
        raise click.Abort()

if __name__ == '__main__':
    cli()
