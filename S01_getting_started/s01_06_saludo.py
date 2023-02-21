import flet
from flet import Page, Row, TextField, ElevatedButton, Text


    
def main(page: Page):
    txt_nombre = TextField(label="Digite su nombre")
    def saludar(event):
        print(f"Hola {txt_nombre.value}")
    
    row = Row(controls = [
        txt_nombre,
        ElevatedButton(text="Saludar", on_click=saludar)
    ])

    page.add(row)

flet.app(target=main)