import os
from copystatic import clean_public, copy_static
from generate_html import generate_page

def main() -> None:

    source: str = "./static"
    destination: str = "./public/"

    #copy files to public
    clean_public(source, destination)
    contents = os.listdir(source)
    copy_static(contents, source, destination)

    #generate the page
    generate_page("./content/index.md", "template.html", "./public/index.html")


if __name__ == "__main__":
    main()
