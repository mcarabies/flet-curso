import flet
from flet import Page, Text
from time import sleep

def main (page:Page):
    for i in range(100):
        page.controls.append(Text(f"Linea: {i}"))
        if i > 4:
            page.controls.pop(0)
        page.update()
        sleep(0.3)

flet.app(target=main)