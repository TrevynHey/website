class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        string = ""
        if self.props == None:
            return string
        for key in self.props:
            string += f" {key}=\"{self.props[key]}\""
        return string
    
    def __repr__(self):
        if self.tag == None:
            tag_str = "None"
        else:
            tag_str = self.tag
        if self.value == None:
            value_str = "None"
        else:
            value_str = self.value
        if self.children == None:
            children_str = "None"
        else:
            children_str = self.children
        if self.props == None:
            props_str = "None"
        else:
            props_str = self.props

        print(f"Tag: {tag_str}\nValue: {value_str}\nChildren: {children_str}\nProps: {props_str}")

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        if value == None:
            raise ValueError("All leaf nodes must have a value")
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"