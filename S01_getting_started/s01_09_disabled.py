import flet
from flet import Page, TextField, Column

def main(page:Page):
    txt_first_name = TextField(hint_text="Ingrese su Nombre")
    txt_last_name = TextField(hint_text="Ingrese su apellido")
    
    # propiedad disabled de forma individual
    txt_first_name.disabled = True

    col_controles = Column(controls=[txt_first_name,txt_last_name])
    
    #aplicando el disabled al componente padre
    col_controles.disabled = True
    
    page.add(col_controles)

flet.app(target=main)