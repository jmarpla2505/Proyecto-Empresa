import flet as ft

def main(page: ft.Page):
    page.title = "Proyecto Empresa"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE  
    contador = 0

    def funcionLogin(r):
        usuariob = "Raul"
        contraseñab = "123"
        dlg = ft.AlertDialog(
        title=ft.Text("Vuelvelo a intentar"))
        page.dialog = dlg
        if contador<3 or usuario.value != usuariob or contraseña.value != contraseñab:
            dlg.open = True
            contador = contador + 1
            print(contador)
        elif contador >= 3:
            print("d")
        else:
            print("a")
        page.update()

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

    login = ft.ElevatedButton(text="Login", on_click=funcionLogin)

    page.add(img1, columnaU, login, img2)
ft.app(target=main, assets_dir="Imágenes")