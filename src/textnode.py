from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode():
    def __init__(self, content, text_type, url=None):
        self.text = content
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