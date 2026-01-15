from textnode import TextType, TextNode
from htmlnode import ParentNode, HTMLNode, LeafNode, textnode_to_html_node
from inline import split_nodes_delimiter, extract_markdown_links, extract_markdown_images, split_nodes_image, split_nodes_link, text_to_textnodes
from markdown_block import markdown_to_blocks, block_to_blocktype

def main() -> None:

    text = "1. one\n2. two"
    print(block_to_blocktype(text))


if __name__ == "__main__":
    main()
