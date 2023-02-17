from time import sleep
import flet
from flet import Page, Text

def main(page: Page):
    lbl_contador = Text()
    page.add(lbl_contador)
    for i in range(10):
        lbl_contador.value = f"Step {i+1}"
        page.update()
        sleep(0.5)
        
flet.app(target=main)