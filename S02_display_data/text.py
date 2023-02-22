import flet
from flet import Page, Text

def main (page:Page):
    lbl_texto = Text(
        value="Flet y Python",
        size=30,
        color="green",
        bgcolor="black",
        weight="bold",
        italic=True
    )
    
    page.add(lbl_texto)
    

flet.app(target=main)