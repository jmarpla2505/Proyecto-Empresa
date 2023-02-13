import flet as ft

def main(page: ft.Page):
    page.title = "Proyecto Empresa"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE

    img1 = ft.Image(
        src=f"Icono.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )

    img2 = ft.Image(
        src=f"Logotipo.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )

    page.add(img1, img2)
ft.app(target=main, assets_dir="Imágenes")