import flet
from flet import Page, Text

def main(page: Page):
    label_texto = Text(
        value="Hello, Marcelo!!", 
        color="red"
        )
    page.controls.append(label_texto)
    page.update()

flet.app(target=main, view=flet.WEB_BROWSER)