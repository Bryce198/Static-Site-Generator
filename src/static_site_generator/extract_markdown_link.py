import re

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

#Returns a list of tuples for each link in a sentence string.