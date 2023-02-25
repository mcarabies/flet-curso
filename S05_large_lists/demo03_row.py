import os
import flet
from flet import Page, Container, Row, Text, alignment,border, border_radius, colors

os.environ['FLET_WS_MAX_MESSAGE_SIZE']='8000000'

def main(page:Page):
    row = Row(wrap=True, scroll='always', expand=True)
    page.add(row)
    
    for i in range(5000):
        row.controls.append(
            Container(
                Text(f"item: {i}"),
                width=100,
                height=100,
                alignment=alignment.center,
                bgcolor=colors.AMBER_400,
                border_radius=border_radius.all(5)
            )
        )
    page.update()
    
    
flet.app(target=main)