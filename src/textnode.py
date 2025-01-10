from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, Node):
        if self.text == Node.text and self.text_type == Node.text_type and self.url == Node.url:
            return True
        else:
            return False
        
    def __repr__(self):
        string = f"TextNode({self.text}, {self.text_type}, {self.url})"
        return string

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None,text_node.text)
        case TextType.BOLD:
            return LeafNode("b",text_node.text)
        case TextType.ITALIC:
            return LeafNode("i",text_node.text)        
        case TextType.CODE:
            return LeafNode("code",text_node.text)        
        case TextType.LINK:
            return LeafNode("a",text_node.text,{"href":text_node.url})        
        case TextType.IMAGE:
            return LeafNode("img","",{"src":text_node.url,"alt":text_node.text})
        case _:
            raise Exception("Not a supported Text Type")   

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    limit_len = []
    new_text_type = None
    if not delimiter in old_nodes.text:
        raise Exception("Delimiter not in text")
    
    for i in range(len(old_nodes.text)):
        if old_nodes.text[i] == "*" and old_nodes.text[i] == delimiter:
            new_text_type = TextType.ITALIC
            limit_len.append(i)
        if old_nodes.text[i] == "`" and old_nodes.text[i] == delimiter:
            new_text_type = TextType.CODE
            limit_len.append(i)
        if i>0:
            if old_nodes.text[i] == old_nodes.text[i-1]:
                new_text_type = TextType.BOLD    
                limit_len.append(i)
    if new_text_type == TextType.BOLD:
        old_nodes.text = old_nodes.text.replace("**","")
        limit_len[0] -= 1
        limit_len[1] -= 3
    elif new_text_type == TextType.ITALIC:
        old_nodes.text = old_nodes.text.replace("*","")
        limit_len[1] -= 1
    elif new_text_type == TextType.CODE:
        old_nodes.text = old_nodes.text.replace("`","")
        limit_len[1] -= 1
    # for i in range(len(limit_len)-1):
    #     if abs(limit_len[i]-limit_len[i+1]) == 1:
    #         limit_len = limit_len.pop(i)
    # print(limit_len)
    a = old_nodes.text[0:limit_len[0]]
    b = old_nodes.text[limit_len[0]:limit_len[1]]
    c = old_nodes.text[limit_len[1]:]

    new_TextNode = [
        TextNode(a, text_type),
        TextNode(b, new_text_type),
        TextNode(c, text_type),
    ]
    return new_TextNode         