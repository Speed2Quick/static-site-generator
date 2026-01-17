import os
import sys
from copystatic import clean_public, copy_static
from generate_html import generate_page, generate_pages_recursive

def main() -> None:

    if not sys.argv[1]:
        basepath = "/"
    else:
        basepath = sys.argv[1]

    source_dir: str = "./static"
    content_dir: str = "./content"
    contents: list[str] = os.listdir(content_dir)
    template_dir: str = "template.html"
    destination_dir: str = "./docs"

    #copy files to public
    clean_public(source_dir, destination_dir)
    static_contents = os.listdir(source_dir)
    copy_static(static_contents, source_dir, destination_dir)

    #generate the page
    generate_pages_recursive(contents, basepath, content_dir, template_dir, destination_dir)


if __name__ == "__main__":
    main()
