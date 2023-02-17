import flet as ft
import time

def main(page: ft.Page):
    page.title = "Proyecto Empresa"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE  

    global contador
    txtcontador = ft.TextField(value=0)

    def funcionLogin(r):
        vLista = []
        p = open("UsuarioYContraseña.txt","r")
        for linea in p:
            lineasl = linea.replace("\n","")
            vLista.append(lineasl)
        p.close()        
        #print (vLista)
        contador = txtcontador.value
        #vLista.count(0) == usuario
        #vLista.count(1) == contraseña
        if contador<3:
            if vLista.count(usuario.value) == 0 or vLista.count(contraseña.value) == 0:
                dlg = ft.AlertDialog(
                title=ft.Text("Vuelvelo a intentar"))
                page.dialog = dlg
                dlg.open = True
                contador = contador + 1
                txtcontador.value = contador
                print(contador)
            else:
                dlg = ft.AlertDialog(
                title=ft.Text("Inicio de sesión correcto"))
                page.dialog = dlg
                dlg.open = True
                page.clean()
        else:
                time.sleep(1)
                page.window_close()
                print("Intentos máximos realizados, intento de inicio de sesión fallido")
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