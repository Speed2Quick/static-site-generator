import os
from markdown_block import markdown_to_html_node

def extract_title(markdown: str):
    lines: list[str] = markdown.split("\n")
    title: str = "<h1>"
    for line in lines:
        if line[:2] == "# ":
            line = line.strip("# ").strip()
            return title + line + "</h1>"
    raise Exception("Error: title missing heading")

#generate a html page from markdown
def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html: str = markdown_to_html_node(markdown).to_html()
    title: str = extract_title(markdown)

    template: str = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    if not os.path.exists(dest_path):
        directory = os.path.dirname(dest_path)
        os.makedirs(directory, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)

#generate all html pages from content dir
def generate_pages_recursive(dir_path_content: list[str], source: str, template_path: str, dest_dir_path: str):
    if len(dir_path_content) == 0:
        return
    new_path: str = os.path.join(source, dir_path_content[0])
    if os.path.isfile(new_path):
        path_to_write: str = os.path.join(dest_dir_path, dir_path_content[0]).replace(".md", ".html")
        generate_page(new_path, template_path, path_to_write)
    else:
        new_directory: str = os.path.join(dest_dir_path, dir_path_content[0])
        new_content: list[str] = os.listdir(new_path)
        os.mkdir(new_directory)
        generate_pages_recursive(new_content, new_path, template_path, new_directory)
        generate_pages_recursive(dir_path_content[1:], source, template_path, dest_dir_path)
