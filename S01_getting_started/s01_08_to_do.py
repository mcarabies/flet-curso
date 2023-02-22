import flet
from flet import Page, Checkbox, ElevatedButton, Row, TextField

def main (page:Page):
    def agregar_tarea_clicked(event):
        page.add(Checkbox(label=txt_nueva_tarea.value))
        
    txt_nueva_tarea = TextField(hint_text="escriba la tarea a agregar", width=300)
    btn_agregar_tarea = ElevatedButton('Agregar Tarea', on_click=agregar_tarea_clicked)
    page.add(Row([txt_nueva_tarea, btn_agregar_tarea]))
    
flet.app(target=main)