import re

def extract_markdown_images(text) -> list[tuple]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

#Returns a list of tuples representing the image url string.