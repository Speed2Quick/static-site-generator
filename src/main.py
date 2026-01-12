from textnode import TextType, TextNode
from htmlnode import ParentNode, HTMLNode, LeafNode

def main() -> None:

    node = TextNode("this is a test node", TextType.TEXT)

    #testing repr
    print(node)
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())

if __name__ == "__main__":
    main()
