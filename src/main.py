from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode
from inline_markdown import *

def main():
    Node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev)")
    
main()