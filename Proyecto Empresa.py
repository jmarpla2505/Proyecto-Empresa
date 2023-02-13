import flet as ft

def main(page: ft.Page):
    page.title = "Proyecto Empresa"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE

    def funcionLogin():


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
    contraseña = ft.TextField(label = "Contraseña", width=400, password=True, can_reveal_password=True)


    contUsuario = ft.Container(content=usuario, margin=10, bgcolor=ft.colors.LIGHT_BLUE)
    contContraseña = ft.Container(content=contraseña, margin=10, bgcolor=ft.colors.LIGHT_BLUE)
    columnaU = ft.Column(controls=[contUsuario, contContraseña])

    login = ft.ElevatedButton(text="Login")

    page.add(img1, columnaU, login, img2)
ft.app(target=main, assets_dir="Imágenes")