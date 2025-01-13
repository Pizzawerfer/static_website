import unittest
from inline_markdown import *
from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode(
            "This is text with a **bolded** word", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode(
            "This is text with an *italic* word", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode(
            "**bold** and *italic*", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode(
            "This is text with a `code block` word", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            extract_markdown_image(text)
        )

    def test_extract_images_empty(self):
        text = "Hier steht nur text"
        self.assertListEqual(
            [], extract_markdown_image(text)
        )

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev")
            ],
            extract_markdown_link(text)
        )

    def test_extract_links_empty(self):
        text = "Hier steht nur text"
        self.assertListEqual(
            [], extract_markdown_link(text)
        )

class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image(self):
        Node = [TextNode("This is text with a link ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",TextType.TEXT)]
        self.assertListEqual(
            [
                TextNode("This is text with a link ",TextType.TEXT, None),
                TextNode("rick roll",TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ",TextType.TEXT,None),
                TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            split_nodes_image(Node)
        )

class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link(self):
        Node = [TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)]
        self.assertListEqual(
            [   
                TextNode("This is text with a link ", TextType.TEXT, None),
                TextNode("to boot dev",TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT, None),
                TextNode("to youtube",TextType.LINK,"https://www.youtube.com/@bootdotdev")
            ],
            split_nodes_link(Node)
        )

class TestTextToTextnode(unittest.TestCase):
    def test_text_to_textnode(self):
        text= "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT, None),
                TextNode("text", TextType.BOLD, None),
                TextNode(" with an ", TextType.TEXT, None),
                TextNode("italic", TextType.ITALIC, None),
                TextNode(" word and a ", TextType.TEXT, None),
                TextNode("code block", TextType.CODE, None),
                TextNode(" and an ", TextType.TEXT, None),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT, None),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ], text_to_textnodes(text)
        )





if __name__ == "__main__":
    unittest.main()
