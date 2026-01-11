import unittest

from src.htmlnode import HTMLNode

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
