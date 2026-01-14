#format markdown into blocks, every piece of text separated by a double newline is a block
def markdown_to_blocks(markdown) -> list[str]:
    blocks: list[str] = markdown.split("\n\n")
    cleaned_blocks: list[str] = [block.strip() for block in blocks if block.strip() != ""]
    return cleaned_blocks
