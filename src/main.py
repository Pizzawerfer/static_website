from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode

def main():
    Node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev)")
    print(Node)
    test1 = TextNode("Test",TextType.TEXT)
    test2 = TextNode("Test",TextType.BOLD)
    test3 = TextNode("Test",TextType.ITALIC)
    test4 = TextNode("Test",TextType.CODE)
    test5 = TextNode("Test",TextType.LINK,"www.google.com")
    test6 = TextNode("Test",TextType.IMAGES,"www.google.com")

    Leafnode1=text_node_to_html_node(test1)
    Leafnode2=text_node_to_html_node(test2)
    Leafnode3=text_node_to_html_node(test3)
    Leafnode4=text_node_to_html_node(test4)
    Leafnode5=text_node_to_html_node(test5)
    Leafnode6=text_node_to_html_node(test6)

    print(Leafnode1.to_html())
    print(Leafnode2.to_html())
    print(Leafnode3.to_html())
    print(Leafnode4.to_html())
    print(Leafnode5.to_html())
    print(Leafnode6.to_html())
    



main()