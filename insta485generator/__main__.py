"""Build static HTML site from directory of HTML templates and plain files."""

import click
import sys
import json
from pathlib import Path
from Jinja2 import Template

@click.command()
@click.argument('inputDir')
@click.option('--verbose', '-v', isVerbose = True, default = False, help='Print more output.')
@click.option('--output', '-o', nargs = 1, default = "html", required = True, help='Output directory.')


def main():
    """Top level command line interface."""
    print("Hello world!")

    #Error message
    if len(sys.argv) < 2:
        print 'Error: Invalid number of arguments'

    input_dir = pathlib.Path(input_dir)  # convert str to Path object
    output_dir = input_dir/Path(output)  # default, can be changed with --output option

    
    #Might need pathlib to turn into a path
    f = open(/input_dir/"config.json")
    data = json.load(f)

    for el in data:
        url = el["url"]
        url = url.lstrip("/")  # remove leading slash

        output_path = output_dir/url
        os.makedirs(output_path)

        template = Template(el["template"])
        out = template.render(el["context"])
        
        #Rewrite this
        text_file = open("index.html", "w")
        text_file.write(out)
        text_file.close()



if __name__ == "__main__":
    main()