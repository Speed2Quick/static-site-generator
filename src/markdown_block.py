from enum import Enum

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

def block_to_blocktype(block):
    lines: list[str] = block.split("\n")
    if block.startswith("#") and block.find("# ") >= 0 and block.find("# ") < 6:
        return BlockType.HEADING
    elif block.startswith("```\n") and block.endswith("\n```"):
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
