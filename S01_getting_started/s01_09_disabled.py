import flet
from flet import Page, TextField, Column

def main(page:Page):
    txt_first_name = TextField()
    txt_last_name = TextField()

    col_controles = Column(controls=[txt_first_name,txt_last_name])
    
    page.add(col_controles)

flet.app(target=main)