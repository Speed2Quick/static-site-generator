import os
import shutil

#clean the public directory
def clean_public(source: str, destination: str):
    if not os.path.exists(source):
        raise FileNotFoundError("Directory to copy from does not exist")
    if not os.path.exists(destination):
        raise FileNotFoundError("Directory to copy to does not exist")
    shutil.rmtree(destination)
    os.mkdir(destination)

#copy all content from the static directory to public
def copy_static(contents: list[str], source: str, destination: str):
    if len(contents) == 0:
        return
    file_path: str = os.path.join(source, contents[0])
    if os.path.isfile(file_path):
        shutil.copy(file_path, destination)
        copy_static(contents[1:], source, destination)
    else:
        new_destination: str = os.path.join(destination, contents[0])
        os.mkdir(new_destination)
        new_contents: list[str] = os.listdir(file_path)
        copy_static(new_contents, file_path, new_destination)
        copy_static(contents[1:], source, destination)
