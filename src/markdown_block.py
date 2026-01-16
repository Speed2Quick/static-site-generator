from enum import Enum
from htmlnode import ParentNode, LeafNode, textnode_to_html_node
from inline import TextType, TextNode, text_to_textnodes


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

#format markdown into blocks, every piece of text separated by a double newline is a block
def markdown_to_blocks(markdown) -> list[str]:
    blocks: list[str] = markdown.split("\n\n")
    cleaned_blocks: list[str] = [block.strip() for block in blocks if block.strip() != ""]
    return cleaned_blocks

def block_to_blocktype(block) -> BlockType:
    lines: list[str] = block.split("\n")

    if block.startswith("#") and block.find("# ") >= 0 and block.find("# ") < 6:
        return BlockType.HEADING

    elif block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    elif block.startswith("> "):
        for line in lines:
            if not line.startswith("> "):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST

    elif block.startswith("1. "):
        num: int = 1
        for line in lines:
            if not line.startswith(f"{num}. "):
                return BlockType.PARAGRAPH
            num += 1
        return BlockType.ORDERED_LIST

    else:
        return BlockType.PARAGRAPH

#parse markdown into html
def markdown_to_html_node(markdown) -> ParentNode:
    #splits markdown into blocks | still has multiple lines
    parent_nodes = []
    blocks: list[str] = markdown_to_blocks(markdown)
    for block in blocks:
        #only determines the type of block
        block_type: BlockType = block_to_blocktype(block)

        if block_type == BlockType.PARAGRAPH:
            text = clean_paragraph(block)
            children: list[LeafNode] = text_to_children(text)
            parent_node = ParentNode("p", children)

        elif block_type == BlockType.HEADING:
            heading_num, text = clean_heading(block)
            children: list[LeafNode] = text_to_children(text)
            parent_node = ParentNode(f"h{heading_num}", children)

        elif block_type == BlockType.CODE:
            text: str = clean_code(block)
            text_node = TextNode(text, TextType.CODE)
            code: LeafNode = textnode_to_html_node(text_node)
            parent_node = ParentNode("pre", [code])

        elif block_type == BlockType.QUOTE:
            text: str = clean_quote(block)
            children: list[LeafNode] = text_to_children(text)
            parent_node = ParentNode("blockquote", children)

        elif block_type == BlockType.UNORDERED_LIST:
            text: str = clean_ul(block)
            list_items = get_list_elements(text)
            parent_node = ParentNode("ul", list_items)
            
        elif block_type == BlockType.ORDERED_LIST:
            text: str = clean_ol(block)
            list_items = get_list_elements(text)
            parent_node = ParentNode("ol", list_items)

        parent_nodes.append(parent_node)
    html_nodes = ParentNode("div", parent_nodes)
    return html_nodes

#convert inline text to html leafnodes
def text_to_children(text) -> list[LeafNode]:
    children: list[LeafNode] = []
    textnodes: list[TextNode] = text_to_textnodes(text)
    for node in textnodes:
        children.append(textnode_to_html_node(node))
    return children

#parse the li nodes and return a ul parentnode
def get_list_elements(text) -> list[ParentNode]:
    list_items: list[ParentNode] = []
    lines = text.split("\n")
    for line in lines:
        child: list[LeafNode] = text_to_children(line.replace("\n", " "))
        list_node = ParentNode("li", child)
        list_items.append(list_node)
    return list_items

#clean up markdown for html
def clean_paragraph(block):
    text = block.replace("\n", " ")
    return text

def clean_heading(block):
    num: int = block.find("# ") + 1
    heading: str = block.strip("###### ").replace("\n", " ")
    return num, heading

def clean_code(block):
    code: str = block.lstrip("```\n").rstrip("```")
    return code

def clean_quote(block):
    lines = block.split("\n")
    lines: list[str] = [line.lstrip("> ") for line in lines]
    quote: str = "\n".join(lines)
    return quote.replace("\n", " ")

def clean_ul(block):
    lines = block.split("\n")
    lines: list[str] = [line.lstrip("- ") for line in lines]
    ul: str = "\n".join(lines)
    return ul

def clean_ol(block):
    ol: list[str] = []
    line_num: int = 1
    lines: list[str] = block.split("\n")
    for line in lines:
        ol.append(line.strip(f"{line_num}. ").replace("\n", ""))
        line_num += 1
    return "\n".join(ol)
        
