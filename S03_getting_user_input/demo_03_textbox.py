import flet
from flet import Page, ElevatedButton, Text, TextField

def main(page:Page):
    
    def saludar_clicked(event):
        if not txt_nombre.value:
            txt_nombre.error_text = "Por favor ingrese su nombre"
            page.update()
        else:
            saludo_actual = Text (f"Hola {txt_nombre.value}")
            page.clean()
            page.add(
                saludo_actual
            )
    txt_nombre = TextField(label="Su nombre")
    page.add(
        txt_nombre,
        ElevatedButton('Saludar', on_click=saludar_clicked)
    )
            
flet.app(target=main, view=flet.WEB_BROWSER)