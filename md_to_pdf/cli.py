"""
Command-line interface for the Markdown to PDF converter.
"""
import click
from .converter import MarkdownToPDFConverter
import sys

@click.group()
def cli():
    """Convert Markdown to PDF with various options."""
    pass

@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--template', default='default.html', help='HTML template to use')
@click.option('--watermark', help='Watermark text to add to the PDF')
@click.option(
    '--watermark-position',
    type=click.Choice(['center', 'top-left', 'top-right', 'bottom-left', 'bottom-right']),
    default='center',
    help='Position of the watermark'
)
@click.option(
    '--watermark-rotation',
    type=int,
    default=-45,
    help='Rotation angle of the watermark in degrees'
)
@click.option(
    '--watermark-opacity',
    type=float,
    default=0.3,
    help='Opacity of the watermark (0.0 to 1.0)'
)
def convert_file(
    input_file: str,
    output_file: str,
    template: str,
    watermark: str,
    watermark_position: str,
    watermark_rotation: int,
    watermark_opacity: float
):
    """Convert a Markdown file to PDF."""
    converter = MarkdownToPDFConverter()
    success = converter.convert(
        input_file,
        output_file,
        template,
        watermark_text=watermark,
        watermark_position=watermark_position,
        watermark_rotation=watermark_rotation,
        watermark_opacity=watermark_opacity
    )
    
    if success:
        click.echo(f"Successfully converted {input_file} to {output_file}")
    else:
        click.echo("Conversion failed!", err=True)
        sys.exit(1)

@cli.command()
@click.argument('output_file', type=click.Path())
@click.option('--template', default='default.html', help='HTML template to use')
@click.option('--watermark', help='Watermark text to add to the PDF')
@click.option(
    '--watermark-position',
    type=click.Choice(['center', 'top-left', 'top-right', 'bottom-left', 'bottom-right']),
    default='center',
    help='Position of the watermark'
)
@click.option(
    '--watermark-rotation',
    type=int,
    default=-45,
    help='Rotation angle of the watermark in degrees'
)
@click.option(
    '--watermark-opacity',
    type=float,
    default=0.3,
    help='Opacity of the watermark (0.0 to 1.0)'
)
def convert_string(
    output_file: str,
    template: str,
    watermark: str,
    watermark_position: str,
    watermark_rotation: int,
    watermark_opacity: float
):
    """Convert Markdown from stdin to PDF."""
    if sys.stdin.isatty():
        click.echo("Error: No input provided via stdin", err=True)
        sys.exit(1)
    
    content = sys.stdin.read()
    converter = MarkdownToPDFConverter()
    success = converter.convert_string(
        content,
        output_file,
        template,
        watermark_text=watermark,
        watermark_position=watermark_position,
        watermark_rotation=watermark_rotation,
        watermark_opacity=watermark_opacity
    )
    
    if success:
        click.echo(f"Successfully converted stdin to {output_file}")
    else:
        click.echo("Conversion failed!", err=True)
        sys.exit(1)

if __name__ == '__main__':
    cli()
