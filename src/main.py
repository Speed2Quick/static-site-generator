from textnode import TextType, TextNode
from htmlnode import ParentNode, HTMLNode, LeafNode, textnode_to_html_node
from inline import split_nodes_delimiter, extract_markdown_links, extract_markdown_images, split_nodes_image, split_nodes_link, text_to_textnodes
from markdown_block import markdown_to_blocks

def main() -> None:

    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    print(markdown_to_blocks(md))

if __name__ == "__main__":
    main()
