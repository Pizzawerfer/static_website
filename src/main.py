from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def main():
    Node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev)")
    print(Node)
    # Node2 = HTMLNode(tag='h1',value='ASDAJFLKSF',props={"href": "https://www.google.com","target": "_blank",})
    # print(Node2)
    # Node3 = LeafNode

main()