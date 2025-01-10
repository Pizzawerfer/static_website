from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    limit_len = []
    new_text_type = None
    if not delimiter in old_nodes.text:
        raise Exception("Delimiter not in text")
    
    for i in range(len(old_nodes.text)):
        if old_nodes.text[i] == "*" and old_nodes.text[i] == delimiter:
            new_text_type = TextType.ITALIC
            limit_len.append(i)
        if old_nodes.text[i] == "`" and old_nodes.text[i] == delimiter:
            new_text_type = TextType.CODE
            limit_len.append(i)
        if i>0:
            if old_nodes.text[i] == old_nodes.text[i-1]:
                new_text_type = TextType.BOLD    
                limit_len.append(i)
    if new_text_type == TextType.BOLD:
        old_nodes.text = old_nodes.text.replace("**","")
        limit_len[0] -= 1
        limit_len[1] -= 3
    elif new_text_type == TextType.ITALIC:
        old_nodes.text = old_nodes.text.replace("*","")
        limit_len[1] -= 1
    elif new_text_type == TextType.CODE:
        old_nodes.text = old_nodes.text.replace("`","")
        limit_len[1] -= 1
    # for i in range(len(limit_len)-1):
    #     if abs(limit_len[i]-limit_len[i+1]) == 1:
    #         limit_len = limit_len.pop(i)
    # print(limit_len)
    a = old_nodes.text[0:limit_len[0]]
    b = old_nodes.text[limit_len[0]:limit_len[1]]
    c = old_nodes.text[limit_len[1]:]

    new_TextNode = [
        TextNode(a, text_type),
        TextNode(b, new_text_type),
        TextNode(c, text_type),
    ]
    return new_TextNode         