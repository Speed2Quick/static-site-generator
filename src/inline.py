from src.textnode import TextNode, TextType
import re

#split a node into into mulitple textnode objects
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_node: list[str] = node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise Exception("invalid markdown: textnode object missing closing delimiter")
        for i in range(len(split_node)):
            if split_node[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_node[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_node[i], text_type))
    return new_nodes

#get anchor text and urls
def extract_markdown_links(text):
    attributes = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return attributes

#get alt text and urls
def extract_markdown_images(text):
    attributes = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return attributes
