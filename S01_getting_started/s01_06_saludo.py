import flet
from flet import Page, Row, TextField, ElevatedButton, Text


    
def main(page: Page):
    txt_nombre = TextField(label="Digite su nombre")
    lbl_saludo = Text(value="quieres que te salude?", color="red")
    def saludar(event):
        lbl_saludo.value=f"hola {txt_nombre.value}"
        lbl_saludo.color="blue"
        page.update()
    
    row1 = Row(controls = [
        txt_nombre,
        ElevatedButton(text="Saludar", on_click=saludar),
    ])
    row2 =Row(controls=[
        lbl_saludo
    ])
    
        

    page.add(row1,row2)

flet.app(target=main)