import os
import flet
from flet import Page, Container, GridView, Text, alignment, border, border_radius, colors

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def main(page:Page):
    ...
    
    
flet.app(target=main)