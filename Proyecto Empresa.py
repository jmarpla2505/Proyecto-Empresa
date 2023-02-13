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

    usuario = ft.TextField(label = "Usuario", width=400)
    contraseña = ft.TextField(label = "Contraseña", width=400)

    columna = ft.Column(controls=[usuario, contraseña])
    contDatos = ft.Container(content=columna, bgcolor=ft.colors.LIGHT_BLUE, margin=50)

    page.add(img1, contDatos, img2)
ft.app(target=main, assets_dir="Imágenes")