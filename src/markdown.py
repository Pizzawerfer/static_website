from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType
from block_markdown import *
from inline_markdown import *


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_stripped = strip_block_from_marker(block, block_type)
        node = create_html_from_markdown(block_stripped,block_type)
        nodes.append(node)
        # for node in nodes:
            # print(node.to_html())
    node = ParentNode("div",nodes)
    print(node)
    return node