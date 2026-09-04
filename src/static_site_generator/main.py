from textnode import TextType, TextNode
from htmlnode import HTMLNode

def __main__():
    type = TextType.PLAIN_TEXT
    test_dict = {
        "href": "http://www.google.com",
        "target": "_blank"
        }

    new = TextNode("This is some anchor text", type.value, "https://www.boot.dev")
    print(new)
    new_htmlnode = HTMLNode("p", "Hello, there", None, test_dict)
    print(new_htmlnode)
    print(new_htmlnode.props_to_html())
    
__main__()