from textnode import TextType, TextNode
from htmlnode import ParentNode, HTMLNode, LeafNode, textnode_to_html_node
from inline import split_nodes_delimiter, extract_markdown_links, extract_markdown_images

def main() -> None:

    text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_links(text))

if __name__ == "__main__":
    main()
