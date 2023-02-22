import flet
from flet import Page, Column, ElevatedButton, Text, TextField,Ref

def main(page:Page):
    txt_first_name = Ref[TextField]()
    txt_last_name = Ref[TextField]()
    
    col_controles = Ref[Column]()
    
    def saludar_clicked(event):
        col_controles.controls.append(Text(f"Hola, {txt_first_name.current.value} {txt_last_name.current.value}!!!"))
        
        txt_first_name.current.value = ''
        txt_last_name.current.value = ''
        
        page.update()
        
        txt_first_name.focus()
    
    btn_saludar = ElevatedButton('Saludar', on_click=saludar_clicked)
    
    page.add(txt_first_name, txt_last_name, btn_saludar, col_controles)
    
flet.app(target=main)