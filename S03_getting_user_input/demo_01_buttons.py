import flet
from flet import Page, ElevatedButton

def main(page:Page):
    btn_accion = ElevatedButton('Click!')
    
    page.add(btn_accion)
    
flet.app(target=main, view=flet.WEB_BROWSER)