import unittest
from src.inline import split_nodes_delimiter
from src.textnode import TextType, TextNode

class TestInline(unittest.TestCase):
    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes,  
        [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("bold block", TextType.BOLD),
        TextNode(" word", TextType.TEXT),
        ]
        )

    def test_split_nodes_delimiter_multiple_code(self):
        node = TextNode("This is `text` with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes,  
        [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.CODE),
        TextNode(" with a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.TEXT),
        ]
        )

    def test_split_nodes_delimiter_multiple_nodes(self):
        node = TextNode("This is text with an _italic block_ word", TextType.TEXT)
        node2 = TextNode("This is text with an _italic block_ word", TextType.TEXT)
        node3 = TextNode("This is text with an _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2, node3], "_", TextType.ITALIC)
        self.assertEqual(new_nodes,  
        [
        TextNode("This is text with an ", TextType.TEXT),
        TextNode("italic block", TextType.ITALIC),
        TextNode(" word", TextType.TEXT),
        TextNode("This is text with an ", TextType.TEXT),
        TextNode("italic block", TextType.ITALIC),
        TextNode(" word", TextType.TEXT),
        TextNode("This is text with an ", TextType.TEXT),
        TextNode("italic block", TextType.ITALIC),
        TextNode(" word", TextType.TEXT),
        ]
        )

    def test_split_nodes_delimiter_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertEqual(new_nodes,
        [
        TextNode("bold", TextType.BOLD),
        TextNode(" and ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        ]
        )

    def test_split_nodes_delimiter_not_text(self):
        node = TextNode("This is text with an _italic block_ word", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes,  
        [
        TextNode("This is text with an _italic block_ word", TextType.BOLD),
        ]
        )

    def test_split_nodes_delimiter_raises_exception(self):
        node = TextNode("This is text with a **bold block word", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.TEXT)
