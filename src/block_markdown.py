from htmlnode import HTMLNode, ParentNode, LeafNode
from inline_markdown import *
from textnode import TextType, TextNode, text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"
block_type_quote = "quote"

def markdown_to_blocks(markdown):
    block = markdown.split("\n\n")
    blockstrings = []
    for line in block:
        if line != "":
            blockstrings.append(line.strip())
        else:
            continue
    return blockstrings

def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith(("# ","## ","### ","#### ","##### ","###### ")):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return "paragraph"
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return "paragraph"
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return "unordered_list"
    if block.startswith("1. "):
        for i in range(len(lines)):
            if not lines[i].startswith(f"{i+1}. "):
                return "paragraph"
        return block_type_olist
    return block_type_paragraph
    
def strip_block_from_marker(block, block_type):
    lines = block
    new_lines = []
    if block_type == block_type_paragraph:
        lines = lines.split("\n")
        lines = " ".join(lines)
        return lines
    if block_type == block_type_heading:
        lines = lines.split(" ")
        counter = lines[0].count("#")
        lines = " ".join(lines[1:])
        return (lines, counter)
    if block_type == block_type_code:
        lines = lines.replace("```", "")
        lines = lines.replace("```", "")
        return lines
    if block_type == block_type_quote:
        lines = block.split("\n")
        for line in lines:
            line = line.lstrip(">")
            line = line.lstrip()
            new_lines.append(line)
        if len(new_lines) > 1:
            new_lines = " ".join(new_lines)
        else:
            new_lines = new_lines[0]
        return new_lines
    if block_type == block_type_ulist:
        lines = block.split("\n")
        for line in lines:
            line = line.split(" ")
            line = " ".join(line[1:])
            new_lines.append(line)
        # if len(new_lines) > 1:
        #     new_lines = "\n".join(new_lines)
        # else:
        #     new_lines[0]
        return new_lines
    if block_type == block_type_olist:
        lines = block.split("\n")
        for line in lines:
            line = line.split(" ")
            line = " ".join(line[1:])
            new_lines.append(line)
        # if len(new_lines) > 1:
        #     new_lines = "\n".join(new_lines)
        # else:
        #     new_lines[0]
        return new_lines
    
def create_html_from_markdown(block_text, block_type):
    nodes = []
    html_type = convert_type(block_type)
    if isinstance(block_text, tuple):
        html_type += f"{block_text[1]}"
        block_text = block_text[0]
    
    #for ordered and unordered list:
    if isinstance(block_text, list):
        children = []
        nodes = []
        for block in block_text:
            text_nodes = text_to_textnodes(block)
            print(text_nodes)
            for text_node in text_nodes:
                html_node = text_node_to_html_node(text_node)
                node = ParentNode("li", html_node)
                children.append(node)
            # nodes.append(ParentNode("li", children))
        return ParentNode(html_type, children)


        #     # print("TEST")
        #     node = LeafNode("li",block)
        #     nodes.append(node)
        # # print(nodes)
        # node = ParentNode(html_type,nodes)
        # return [node]

    #for quote, heading and paragraph:
    elif isinstance(block_text, str):
        text_nodes = text_to_textnodes(block_text)
        children = []
        for text_node in text_nodes:
            html_node = text_node_to_html_node(text_node)
            children.append(html_node)
        return ParentNode(html_type, children)
    return None


def convert_type(type_markdown):
    if isinstance(type_markdown, str):
        if type_markdown == block_type_paragraph:
            return "p"
        if type_markdown == block_type_quote:
            return "blockquote"
        if type_markdown == block_type_code:
            return "code"
        if type_markdown == block_type_ulist:
            return "ul"
        if type_markdown == block_type_olist:
            return "ol"
        if type_markdown == block_type_heading:
            return "h"
    # elif isinstance(type_markdown, tuple):
    #     return f"h{type_markdown[1]}"