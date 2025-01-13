from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType
from block_markdown import *
from inline_markdown import *
import os


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_stripped = strip_block_from_marker(block, block_type)
        node = create_html_from_markdown(block_stripped,block_type)
        nodes.append(node)
    node = ParentNode("div",nodes)
    return node

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block[2:]
        else:
            raise Exception("No h1 Header")
        
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    main_path = os.path.dirname(os.path.realpath(__file__)).replace("src","")
    source = os.path.join(main_path.replace("src/",""),from_path)
    template = os.path.join(main_path.replace("src/",""),template_path)
    
    with open(source) as file:
        markdown = file.read()
        file.close()
    with open(template) as file2:
        template = file2.read()
        file2.close()
    
    HTML_str_nodes = markdown_to_html_node(markdown)
    HTML_str = HTML_str_nodes.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", HTML_str)

    with open(dest_path, "w") as file:
        file.write(template)
        file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    ls = os.listdir(dir_path_content)

    with open(template_path) as file:
        template = file.read()
        file.close()

    for item in ls:
        if os.path.isfile(item):
            print(dir_path_content)
            with open(dir_path_content + item) as file:
                markdown = file.read()
                file.close()

            HTML_str_nodes = markdown_to_html_node(markdown)
            HTML_str = HTML_str_nodes.to_html()
            title = extract_title(markdown)
            template_new = template.replace("{{ Title }}", title)
            template_new = template_new.replace("{{ Content }}", HTML_str)

            with open(dest_dir_path + "index.html", "w") as file:
                file.write(template_new)
                file.close()
        else:
            os.makedirs(dest_dir_path + item + "/")
            generate_pages_recursive(dir_path_content + item + "/", template_path, dest_dir_path + item + "/")

        
