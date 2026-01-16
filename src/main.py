import os
from copystatic import clean_public, copy_static

def main() -> None:

    source: str = "./static"
    destination: str = "./public/"

    #copy files to public
    clean_public(source, destination)
    contents = os.listdir(source)
    copy_static(contents, source, destination)

if __name__ == "__main__":
    main()
