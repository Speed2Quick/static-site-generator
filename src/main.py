from textnode import TextType, TextNode
from htmlnode import ParentNode, HTMLNode, LeafNode, textnode_to_html_node

def main() -> None:

    node = textnode_to_html_node(TextNode("test", TextType.TEXT))
    print(node.tag)

if __name__ == "__main__":
    main()
