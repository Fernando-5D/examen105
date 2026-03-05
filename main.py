import flet as ft

def main(page: ft.Page):
    page.title = "Examen"
    page.padding = 20

    nombre = ft.TextField(label="Nombre Completo")
    email = ft.TextField(label="Correo Electronico")

    taller = ft.Dropdown(
        label="Taller de Interes",
        options=[
            ft.dropdown.Option("Python para Principiantes"),
            ft.dropdown.Option("Flet Intermedio"),
            ft.dropdown.Option("Analisis de Datos con Pandas")
        ]
    )

    modalidad = ft.RadioGroup(
        content=[
            ft.Radio(label="Pago Completo", value="Completo"),
            ft.Radio(label="Pago por Cuotas", value="Por Cuotas")
        ],
        value="Completo"
    )

    laptop = ft.Checkbox(label="Requiere computadora portatil?")

    def on_change_exp(e):
        experiencia.label = f"Nivel {e.control.value}"
        page.update()

    experiencia = ft.Slider(
        label="Nivel 1",
        value=1,
        min=1,
        max=5,
        divisions=4,
        on_change=lambda e: on_change_exp(e)
    )

    resumen = ft.Text(value="")

    def generarResumen():
        resumen.value = f"""
        --- Ficha del Participante ---
        Nombre: {nombre.value}
        Email: {email.value}
        Taller: {taller.value}
        Pago: {modalidad.value}
        Requiere Portatil: {"Si" if laptop.value == True else "No"}
        Nivel de Experiencia: {experiencia.value}
        --- Gracias por su registro ---
        """
        page.update()

    page.add(ft.Column(
        controls=[
            ft.Text(
                value="Registro de Participantes",
                size=30,
                weight=ft.FontWeight.BOLD
            ),
            nombre,
            email,
            taller,
            modalidad,
            laptop,
            ft.Text(value="Nivel de Experiencia"),
            experiencia,
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.ElevatedButton(
                        content="Mostrar Ficha del Participante",
                        bgcolor=ft.Colors.RED,
                        on_click=lambda e: generarResumen(e)
                    )
                ]
            ),
            ft.Divider(color=ft.Colors.GREY),
            resumen
        ],
        spacing=15,
        alignment=ft.MainAxisAlignment.CENTER
    ))

ft.run(main)
