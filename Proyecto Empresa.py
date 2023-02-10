import flet as ft

def main(page: ft.Page):
    page.title="Proyecto Empresa"
     
    def row_with_alignment(align: ft.MainAxisAlignment):
        img = ft.Image(
            src=f"Icono.png",
            width=250,
            height=250,
            fit=ft.ImageFit.CONTAIN,
        )
        return ft.Column(
            [
                ft.Text(str(align), size=16),
                ft.Container(
                    content=ft.Row(img(3), alignment=align),
                    bgcolor=ft.colors.AMBER_100,
                ),
            ]
        )
    



    img2 = ft.Image(
        src=f"Logotipo.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )


    page.add(row_with_alignment(ft.MainAxisAlignment.CENTER))
ft.app(target=main, assets_dir="Imágenes")