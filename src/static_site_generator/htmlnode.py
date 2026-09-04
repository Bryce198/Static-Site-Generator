class HTMLNode():
    def __init__(self, 
                 tag: str | None = None, 
                 value: str | None = None, 
                 children: list["HTMLNode"] | None = None,
                 props: dict[str, str] | None = None):
        self.tag = tag
        self.value = value
        self.__children = children or []
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        return " ".join(f"{k}={v}" for k, v in self.props.items())

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.__children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, 
                 tag: str | None, 
                 value: str, 
                 props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value
        self.props = props or {}

    def to_html(self):
        attributes = ""
        if self.value is None:
            raise ValueError("Value is empty")
        if self.tag is None:
            return str(self.value)
        else:
            if not self.props:
                return f"<{self.tag}>{self.value}</{self.tag}>"
        
        for k, v in self.props.items():
            attributes += f" {k}={v}"
        return f'<{self.tag}{attributes}>{self.value}</{self.tag}>'

    def __repr__(self) -> str:
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"


