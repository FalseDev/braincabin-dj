from django import template
from markdown import markdown

register = template.Library()

def convert_markdown(md_text):
    return markdown(md_text)

register.filter('convert_markdown', convert_markdown)