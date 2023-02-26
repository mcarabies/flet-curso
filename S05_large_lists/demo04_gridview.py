import os
import flet
from flet import Page, Container, GridView, Text, alignment, border, border_radius, colors

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def main(page:Page):
    gvw_datos = GridView(expand=True, max_extent=100, child_aspect_ratio=3)
    page.add(gvw_datos)
    
    for i in range(5000):
        gvw_datos.controls.append(
            Container(
                Text(f'item: {i}'),
                alignment=alignment.center,
                bgcolor=colors.AMBER_100,
                border=border.all(1,colors.AMBER_400),
                border_radius=border_radius.all(5)
            )
        )
    page.update()
    
    
flet.app(target=main, view=flet.WEB_BROWSER)