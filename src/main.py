from textnode import TextType, TextNode
from htmlnode import ParentNode, HTMLNode, LeafNode, textnode_to_html_node
from inline import split_nodes_delimiter, extract_markdown_links, extract_markdown_images, split_nodes_image, split_nodes_link, text_to_textnodes

def main() -> None:

    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    print(text_to_textnodes(text))

if __name__ == "__main__":
    main()
