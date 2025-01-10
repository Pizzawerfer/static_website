from textnode import TextNode, TextType

# def split_nodes_delimiter2(old_nodes, delimiter, text_type):
#     limit_len = []
#     new_text_type = None
#     if not delimiter in old_nodes.text:
#         raise Exception("Delimiter not in text")
    
#     for i in range(len(old_nodes.text)):
#         if old_nodes.text[i] == "*" and old_nodes.text[i] == delimiter:
#             new_text_type = TextType.ITALIC
#             limit_len.append(i)
#         if old_nodes.text[i] == "`" and old_nodes.text[i] == delimiter:
#             new_text_type = TextType.CODE
#             limit_len.append(i)
#         if i>0:
#             if old_nodes.text[i] == old_nodes.text[i-1]:
#                 new_text_type = TextType.BOLD    
#                 limit_len.append(i)
    

#     new_nodes = old_nodes.split(delimiter)
#     if len(new_nodes)%2 == 0:
#         raise Exception("Delimiter was not closed!")

#     new_TextNode = [
#         TextNode(new_nodes[0], text_type),
#         TextNode(new_nodes[1], new_text_type),
#         TextNode(new_nodes[2], text_type),
#     ]
#     return new_TextNode         

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        texts = node.text.split(delimiter)

        if len(texts)%2==0:
            raise Exception("Error: Delimiter not closed!")


        for i in range(len(texts)):
            if texts[i] == "":
                continue
            if i %2 == 0:
                new_nodes.append(TextNode(texts[i],TextType.TEXT))
            else:
                new_nodes.append(TextNode(texts[i],text_type))
    return new_nodes