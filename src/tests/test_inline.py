import unittest
from src.inline import split_nodes_delimiter, extract_markdown_links, extract_markdown_images, split_nodes_image, split_nodes_link
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

    def test_extract_links(self):
        text = "This is text with a link ![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        attributes = extract_markdown_links(text)
        self.assertEqual(attributes, [("to youtube", "https://www.youtube.com/@bootdotdev")]
)

    def test_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg"
        attributes = extract_markdown_images(text)
        self.assertEqual(attributes, [("rick roll", "https://i.imgur.com/aKaOqIh.gif")])

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://test.com) and another [second link](https://test.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://test.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://test.com"
                ),
            ],
            new_nodes,
        )

    def test_split_images_ending_text(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) with more text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" with more text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_normal_text(self):
        node = TextNode(
            "This is text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text", TextType.TEXT),
            ],
            new_nodes,
            )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )
