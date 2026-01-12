import unittest

from src.htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode("p", "test")
        result: str = node.props_to_html()
        self.assertEqual(result, "")

    def test_props(self):
        node = HTMLNode("a", "test", None, {"href": "www.test.org"})
        result: str = node.props_to_html()
        self.assertEqual(result, " href=\"www.test.org\"")

    def test_multiple_props(self):
        node = HTMLNode("a", "test", None, {"href": "www.test.org", "target": "www.test.org"})
        result: str = node.props_to_html()
        self.assertEqual(result, " href=\"www.test.org\" target=\"www.test.org\"")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {"href": "www.test.org"})
        self.assertEqual(node.to_html(), "<a href=\"www.test.org\">Hello, world!</a>")
