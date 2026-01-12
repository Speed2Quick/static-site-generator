import unittest

from src.textnode import TextType, TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a **test** node", TextType.BOLD)
        node2 = TextNode("This is a **test** node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_link(self):
        node = TextNode("This is a test node with a link", TextType.LINK, "https://test.com")
        node2 = TextNode("This is a test node with a link", TextType.LINK, "https://test.com")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is another text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.LINK, "https://test.com")
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
