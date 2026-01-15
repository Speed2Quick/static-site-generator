from src.markdown_block import BlockType, markdown_to_blocks, block_to_blocktype, markdown_to_html_node
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

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
and a ![test](https://test.com) img plus a
[link](https://test.com)
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here and a <img src=\"https://test.com\" alt=\"test\"></img> img plus a <a href=\"https://test.com\">link</a></p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quoteblock(self):
        md = """
> This is a quote _block_
> This is still a **quote** block
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote <i>block</i> This is still a <b>quote</b> block</blockquote></div>",
        )

    def test_heading(self):
        md = """
###### This is text that _is_
a **heading**
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>This is text that <i>is</i> a <b>heading</b></h6></div>",
        )

    def test_ul(self):
        md = """
- This is a _ul_
- This is a **ul**
- This is a ![test](https://test.com) ul
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a <i>ul</i></li><li>This is a <b>ul</b></li><li>This is a <img src=\"https://test.com\" alt=\"test\"></img> ul</li></ul></div>",
        )

    def test_ol(self):
        md = """
1. This is a _ol_
2. This is a **ol**
3. This is a [test](https://test.com) ol
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is a <i>ol</i></li><li>This is a <b>ol</b></li><li>This is a <a href=\"https://test.com\">test</a> ol</li></ol></div>",
        )

if __name__ == "__main__":
    unittest.main()
