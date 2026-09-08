from textnode import *

def split_nodes_delimiter(old_nodes: list[TextNode], 
                          delimiter: str, 
                          text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT.value:
            new_nodes.append(node)

        elif node.text_type == TextType.PLAIN_TEXT.value:
            split_node = node.text.split(delimiter)
            if len(split_node) % 2 == 0:
                raise Exception("Error: Invalid Markdown syntax")
            for i in range(len(split_node)):
                if i % 2 == 0:
                    split_node[i] = TextNode(split_node[i], TextType.PLAIN_TEXT.value)
                else:
                    split_node[i] = TextNode(split_node[i], text_type.value)
            


            new_nodes.extend(split_node)

    return new_nodes
            

