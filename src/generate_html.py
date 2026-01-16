import os
from markdown_block import markdown_to_html_node

def extract_title(markdown):
    lines: list[str] = markdown.split("\n")
    title: str = "<h1>"
    for line in lines:
        if line[:2] == "# ":
            line = line.strip("# ").strip()
            return title + line + "</h1>"
    raise Exception("Error: title missing heading")

def generate_page(from_path, template_path, dest_path):
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
