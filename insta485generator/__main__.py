"""Build static HTML site from directory of HTML templates and plain files."""

import json
import pathlib
import shutil
import click
import jinja2


@click.command()
@click.argument('input_dir', required=True, type=click.Path(exists=True))
@click.option('--verbose', '-v', is_flag=True,
              default=False, help='Print more output.')
@click.option('--output', '-o', nargs=1,
              default="html", required=True, help='Output directory.')
def main(verbose, output, input_dir):
    """Top level command line interface."""
    # print("Hello world!")

    # print(input_dir)
    input_dir = pathlib.Path(input_dir)  # convert str to Path object
    if output == "html":
        output_dir = input_dir/output
    else:
        output_dir = pathlib.Path(output)

    template_dir = input_dir/"templates"
    # careful here
    # output_dir.mkdir(exist_ok=True)

    # Might need pathlib to turn into a path

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(template_dir)),
        autoescape=jinja2.select_autoescape(['html', 'xml']),
    )

    with open(input_dir/"config.json", "r") as content:
        data = json.loads(content.read())

    src_dir = input_dir/"static"
    if src_dir.is_dir():
        shutil.copytree(src_dir, output_dir)
        # figure out the trailing /
        if verbose:
            print("Copied " + str(src_dir) + "/ -> " + str(output_dir) + "/")

    output_dir.mkdir(exist_ok=True, parents=True)

    for element in data:
        url = element["url"]
        url = url.lstrip("/")  # remove leading slash

        output_path = output_dir/url
        output_path.mkdir(exist_ok=True, parents=True)

        template = env.get_template(element["template"])
        out = template.render(element["context"])

        if verbose:
            print("Rendered " + element["template"] + " -> " +
                  str(output_path/"index.html"))
        # print(out)
        # Rewrite this

        with open(output_path/"index.html", "w") as content:
            content.write(out)


if __name__ == "__main__":
    main()
