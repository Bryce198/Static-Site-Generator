from textnode import *
from htmlnode import *

def __main__():
    type = TextType.LINKS
    test_dict = {
        "href": "http://www.google.com",
        "target": "_blank"
        }

    new = TextNode("This is some anchor text", type.value, "https://www.boot.dev")
    result = text_node_to_html_node(new)
    print(result)
    print(result.to_html())

    
__main__()