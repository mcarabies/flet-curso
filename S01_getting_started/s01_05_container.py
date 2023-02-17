import flet
from flet import Page, Row, Text

def main(page: Page):
    row_datos= Row(controls=[
            Text("Python", color="blue"),
            Text("Flet", color="green"),
            Text("Flutter", color="red")
    ])
    page.add(row_datos)
    

app = flet.app(target=main)