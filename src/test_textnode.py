import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)
        
    def test_eq3(self):
        node = TextNode("This is a text node", TextType.BOLD,"https://www.boot.dev/")
        node2 = TextNode("This is a text node", TextType.BOLD,"https://www.boot.dev/")
        self.assertEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("*This `is` italic*", TextType.ITALIC)
        nodes = split_nodes_delimiter(node, "`", TextType.ITALIC)
        self.assertEqual(nodes[0].text, "*This ")
        self.assertEqual(nodes[0].text_type, TextType.ITALIC)
        self.assertEqual(nodes[1].text, "is")
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertEqual(nodes[2].text, " italic*")
        self.assertEqual(nodes[2].text_type, TextType.ITALIC)

    def test_split_nodes_delimiter2(self):
        node = TextNode("This `is` italic", TextType.TEXT)
        nodes = split_nodes_delimiter(node, "`", TextType.TEXT)
        self.assertEqual(nodes[0].text, "This ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "is")
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertEqual(nodes[2].text, " italic")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        
    def test_split_nodes_delimiter3(self):
        node = TextNode("This **is** italic", TextType.TEXT)
        nodes = split_nodes_delimiter(node, "**", TextType.TEXT)
        self.assertEqual(nodes[0].text, "This ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "is")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " italic")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)


if __name__ == "__main__":
    unittest.main()
