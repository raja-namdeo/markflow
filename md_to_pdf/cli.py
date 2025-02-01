"""
Command-line interface for the Markdown to PDF converter.
"""
import click
from .converter import MarkdownToPDFConverter
import sys

@click.group()
def cli():
    """Markdown to PDF converter CLI."""
    pass

@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--template', default='default.html', help='HTML template to use')
def convert_file(input_file, output_file, template):
    """Convert a Markdown file to PDF.
    
    INPUT_FILE: Path to the input Markdown file
    OUTPUT_FILE: Path where to save the PDF file
    """
    converter = MarkdownToPDFConverter()
    if converter.convert(input_file, output_file, template):
        click.echo(f"Successfully converted {input_file} to {output_file}")
    else:
        click.echo("Conversion failed!", err=True)
        sys.exit(1)

@cli.command()
@click.argument('output_file', type=click.Path())
@click.option('--template', default='default.html', help='HTML template to use')
def convert_string(output_file, template):
    """Convert Markdown from stdin to PDF.
    
    OUTPUT_FILE: Path where to save the PDF file
    
    Reads Markdown content from stdin until EOF (Ctrl+D).
    """
    # Read from stdin
    content = sys.stdin.read()
    
    converter = MarkdownToPDFConverter()
    if converter.convert_string(content, output_file, template):
        click.echo(f"Successfully converted input to {output_file}")
    else:
        click.echo("Conversion failed!", err=True)
        sys.exit(1)

if __name__ == '__main__':
    cli()
