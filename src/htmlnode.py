#html object representing blocks and inline

class HTMLNode():
    def __init__(self,
                 tag: str | None = None,
                 value: str | None = None,
                 children: list[str] | None = None,
                 props: dict | None = None,
                 ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    #used by child classes to convert markdown to html
    def to_html(self) -> None:
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
