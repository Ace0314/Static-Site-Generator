import unittest

from htmlnode import HTMLNode


class testHTMLNode(unittest.TestCase):
    def test_prop(self):
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
        self.assertEqual(
            node.props_to_html(),
            ' href="https://google.com" target="_blank"'
        )

if __name__ == "__main__":
    unittest.main()