import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_1(self):
        node1 = HTMLNode("p","Testing paragraph",None,{"href":"test url","target":"_blank"})
        self.assertEqual(node1.props_to_html()," href=\"test url\" target=\"_blank\"")
        #print(node1.__repr__())

class TestLeafNode(unittest.TestCase):
    def test_leaf(self):
        node1 = LeafNode("p","This is the paragraph text")
        self.assertEqual(node1.to_html(),"<p>This is the paragraph text</p>")
        print(node1.to_html())