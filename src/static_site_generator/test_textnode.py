import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT.value)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT.value)
        node3 = TextNode("This is a text node", TextType.LINKS.value)
        node4 = TextNode("This is a text node", TextType.PLAIN_TEXT.value)
        node5 = TextNode("This is a text node", TextType.IMAGES.value, "http://www.coolmath.com")
        node6 = TextNode("This is a text node", TextType.IMAGES.value, "http://www.coolmath.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node3, node4)
        self.assertEqual(node5, node6)

if __name__ == "__main__":
    unittest.main()