import flet
from flet import Page, Row, TextField, ElevatedButton, Text

def saludar(event):
    print("Hola!!!")
    print("Chau!!!")
    
def main(page: Page):
    row = Row(controls = [
        TextField(label="Digite su nombre"),
        ElevatedButton(text="Saludar", on_click=saludar)
    ])

    page.add(row)

flet.app(target=main)