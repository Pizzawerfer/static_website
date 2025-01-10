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
        super().__init__(self, tag, value, props)

    def to_html(self):
        if self.value == 0:
            raise ValueError
        if self.tag == None or self.tag == "":
            return self.value
        
        return f"<{self.tag}{self.props}>{self.value}</{self.tag}>"