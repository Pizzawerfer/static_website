from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode
from inline_markdown import *
from block_markdown import *
from markdown import markdown_to_html_node

def main():
    # Node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev)")
    # text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
    # markdown_to_blocks(text)
    markdown_text = "# H1 Header\n\nSome Code:\n\n``` Same Code\nas here\ncheck ```\n\n## H2 Header\n\n> Quote\n> Quote 2\n\n### H3 Header\n\n1. OListe und test\n2. OListe\n3. OListe\n\n* UnLi\n* UnLi\n* UnLi\n\n- UnLi\n- UnLi\n- UnLi"
    html_node = markdown_to_html_node(markdown_text)
    # print(html_node)
    print("Main Ende")
main()