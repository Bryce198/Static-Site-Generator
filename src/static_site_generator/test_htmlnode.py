import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_node(self):
        test_dict =  {
                "href": "http://www.google.com",
                "target": "_blank"
                }
        node = HTMLNode("p", "Hello, there", None, test_dict)
        self.assertIsInstance(node, HTMLNode)