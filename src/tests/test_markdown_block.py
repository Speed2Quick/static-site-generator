from src.markdown_block import BlockType, markdown_to_blocks, block_to_blocktype
import unittest

class TestMarkdownBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_extra_whitespace(self):
        md = """
This is **bolded**  paragraph

 

    This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line


- This is a list
- with items        
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded**  paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_blockype_heading(self):
        block = "### this is a test"
        self.assertEqual(block_to_blocktype(block), BlockType.HEADING)

    def test_block_to_blockype_code(self):
        block = "```\nthis is a \ntest\n```"
        self.assertEqual(block_to_blocktype(block), BlockType.CODE)

    def test_block_to_blockype_quote(self):
        block = "> this is a test\n> this is a test\n> this is a test"
        self.assertEqual(block_to_blocktype(block), BlockType.QUOTE)

    def test_block_to_blockype_ulist(self):
        block = "- this is a test\n- this is a test\n- this is a test"
        self.assertEqual(block_to_blocktype(block), BlockType.UNORDERED_LIST)

    def test_block_to_blockype_olist(self):
        block = "1. this is a test\n2. this is a test\n3. this is a test"
        self.assertEqual(block_to_blocktype(block), BlockType.ORDERED_LIST)

if __name__ == "__main__":
    unittest.main()
