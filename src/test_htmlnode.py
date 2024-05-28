import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class testHTMLNode(unittest.TestCase):
    def test_prop(self):
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
        self.assertEqual(
            node.props_to_html(),
            ' href="https://google.com" target="_blank"'
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello World!")
        self.assertEqual(node.to_html(), "<p>Hello World!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello World!")
        self.assertEqual(node.to_html(), "Hello World!")

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
            "<div><span><b>grandchild</b></span></div>"
        )

if __name__ == "__main__":
    unittest.main()