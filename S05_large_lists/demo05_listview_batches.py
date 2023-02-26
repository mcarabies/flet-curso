import os
import flet
from flet import Page, ListView, Text

def main(page:Page):
    lvw_lineas = ListView(expand=1, spacing=10, item_extent=50)
    page.add(lvw_lineas)
    
    for i in range(50000):
        lvw_lineas.controls.append(Text(f'Linea: {i}'))
        
        if i % 300 == 0:
            page.update()
    
    page.update()

flet.app(target=main, view=flet.WEB_BROWSER)