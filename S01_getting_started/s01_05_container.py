import flet
from flet import Page, Row, Text

def main(page: Page):
    lenguajes = [
        ("Python","blue"),
        ("Flet", "green"),
        ("Flutter", "red")
    ]
    etiquetas = []
    for etiqueta in lenguajes:
        etiquetas.append(Text(etiqueta[0],color=etiqueta[1]))
    row_datos= Row(controls=etiquetas)
    page.add(row_datos)
    

app = flet.app(target=main)