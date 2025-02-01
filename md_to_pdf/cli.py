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
