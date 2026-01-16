from textnode import TextType

#html object representing blocks and inline

class HTMLNode():
    def __init__(self,
                 tag: str | None = None,
                 value: str | None = None,
                 children: list | None = None,
                 props: dict | None = None,
                 ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    #used by child classes to convert markdown to html
    def to_html(self) -> str:
        raise NotImplementedError("to_html method not implemented")

    #convert the props dict to html
    def props_to_html(self) -> str:
        if not self.props:
            return ""
        props: str = ""
        for prop in self.props:
            props += f" {prop}=\"{self.props[prop]}\""
        return props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

#html object with children
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict | None = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if len(self.children) is None:
            raise ValueError("invalid HTML: missing children")
        children_html: str = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.children}, {self.props})"


#html object with no children
class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict | None = None) -> None:
        super().__init__(tag, value, None, props)
    
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

#parse textnodes into html leaf nodes
def textnode_to_html_node(text_node) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise AttributeError("Invalid text type: could not parse markdown to leafnode")
