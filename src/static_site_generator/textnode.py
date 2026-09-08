from enum import Enum
from htmlnode import *

class TextType(Enum):
    PLAIN_TEXT = "text"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINKS = "link"
    IMAGES = "image"
    
class TextNode():
    def __init__(self, text: str, text_type: str, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return NotImplemented
        return (self.text == other.text 
                and self.text_type == other.text_type 
                and self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type not in (
             TextType.PLAIN_TEXT.value,
             TextType.BOLD_TEXT.value,
             TextType.ITALIC_TEXT.value,
             TextType.CODE_TEXT.value,
             TextType.LINKS.value,
             TextType.IMAGES.value
        ):
            raise Exception("Error: must be a TextType")
    elif text_node.text_type == TextType.PLAIN_TEXT.value:
            return LeafNode(None, text_node.text)

    elif text_node.text_type == TextType.BOLD_TEXT.value:
            return LeafNode("b", text_node.text)

    elif text_node.text_type == TextType.ITALIC_TEXT.value:
            return LeafNode("i", text_node.text)

    elif text_node.text_type == TextType.CODE_TEXT.value:
            return LeafNode("code", text_node.text)

    elif text_node.text_type == TextType.LINKS.value:
            return LeafNode("a", text_node.text, props={"href": f"{text_node.url}"})

    elif text_node.text_type == TextType.IMAGES.value:
            return LeafNode("img", "", props={"src": f"{text_node.url}", "alt": f"{text_node.text}"})
    raise Exception("Error: must be a TextType")

#text_node_to_html_node takes a textnode as an argument and returns an html leafnode 
#based on the textnode TextType.

        
        
