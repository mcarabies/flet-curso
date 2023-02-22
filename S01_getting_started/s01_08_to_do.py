import flet
from flet import Page, Text

def main (page:Page):
    page.controls.append(Text(value="To Do", color="blue"))
    page.update()
    
flet.app(target=main)