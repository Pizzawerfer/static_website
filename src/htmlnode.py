class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError("to_hmtl method not yet implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        else:
            string=""
            for key in self.props:
                string += f' {key}="{self.props[key]}"'

            return string
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        if self.value == 0:
            raise ValueError("Value not listed")
        if self.tag is None or self.tag == "":
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return ""
        return f"ParentNode({self.tag}, children: {self.children[0]}, {self.props})"

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag not listed")
        if self.children is None:
            raise ValueError("Children not listed")
        children_html=""
        for child in self.children:
            children_html += child.to_html()
        string= f'<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>'
        return string