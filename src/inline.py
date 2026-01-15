from src.textnode import TextNode, TextType
import re

#functions to split nodes with nested texttypes into into mulitple textnode objects

def text_to_textnodes(text) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    return nodes

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

def split_nodes_link(old_nodes) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        text: str = node.text
        attributes: list[tuple] = extract_markdown_links(text)
        if len(attributes) == 0:
            new_nodes.append(node)
            continue
        for anchor_text, url in attributes:
            split_node: list[str] = text.split(f"[{anchor_text}]({url})", 1)
            if len(split_node) != 2:
                raise Exception("invalid markdown: textnode object missing closing delimiter")
            elif split_node[0] != "":
                new_nodes.append(TextNode(split_node[0], TextType.TEXT))
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            text = split_node[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes_image(old_nodes) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        text: str = node.text
        attributes: list[tuple] = extract_markdown_images(text)
        if len(attributes) == 0:
            new_nodes.append(node)
            continue
        for alt_text, url in attributes:
            split_node: list[str] = text.split(f"![{alt_text}]({url})", 1)
            if len(split_node) != 2:
                raise Exception("invalid markdown: textnode object missing closing delimiter")
            elif split_node[0] != "":
                new_nodes.append(TextNode(split_node[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            text = split_node[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

#get anchor text and urls
def extract_markdown_links(text) -> list[tuple]:
    attributes: list[tuple] = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return attributes

#get alt text and urls
def extract_markdown_images(text) -> list[tuple]:
    attributes: list[tuple] = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return attributes
