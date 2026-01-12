import unittest

from src.htmlnode import HTMLNode, ParentNode, LeafNode

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

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_great_grandchildren(self):
        great_grandchild_node = LeafNode("i", "greatgrandchild")
        grandchild_node = ParentNode("b", [great_grandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b><i>greatgrandchild</i></b></span></div>",
        )

    def test_to_html_with_many_great_grandchildren(self):
        great_grandchild_node1 = LeafNode("i", "greatgrandchild1")
        great_grandchild_node2 = LeafNode("a", "greatgrandchildnode2", {"href": "www.test.org"})
        grandchild_node1 = ParentNode("b", [great_grandchild_node1, great_grandchild_node2])
        grandchild_node2 = LeafNode("i", "grandchild2")
        child_node = ParentNode("span", [grandchild_node1, grandchild_node2])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b><i>greatgrandchild1</i><a href=\"www.test.org\">greatgrandchildnode2</a></b><i>grandchild2</i></span></div>",
        )

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("p", None)
        self.assertRaises(ValueError)
