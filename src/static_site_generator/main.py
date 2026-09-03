from textnode import TextType, TextNode

def __main__():
    type = TextType.PLAIN_TEXT

    new = TextNode("This is some anchor text", type.value, "https://www.boot.dev")
    print(new)
    
__main__()