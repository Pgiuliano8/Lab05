import flet as ft
from database.corso_DAO import getAllcorsi


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_corsi = None
        self.btn_cercaIscritti = None
        self.txt_matr = None
        self.txt_nome = None
        self.txt_cognome = None
        self._btn_cercaStudente = None
        self._btn_cercaCorsi = None
        self._btn_iscrivi = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # dropdown per i corsi del database
        corsi = getAllcorsi()
        self.dd_corsi = ft.Dropdown(
            label="corso",
            width=800,
            hint_text="Selezionare corso",
            options=[ft.dropdown.Option (key=c._codins, text=c.__str__())for c in corsi]
        )



        self.btn_cercaIscritti = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.handleCercaIscritti)
        row1 = ft.Row([self.dd_corsi, self.btn_cercaIscritti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.txt_matr = ft.TextField(label="matricola")
        self.txt_nome = ft.TextField(label="nome", read_only=True)
        self.txt_cognome = ft.TextField(label="cognome", read_only=True)
        row2 = ft.Row([self.txt_matr, self.txt_nome, self.txt_cognome], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self._btn_cercaStudente = ft.ElevatedButton(text="Cerca studente",
                                                    on_click=self._controller.handleCercaStudente)
        self._btn_cercaCorsi = ft.ElevatedButton(text="Cerca corsi",
                                                 on_click=self._controller.handleCercaCorsi)
        self._btn_iscrivi = ft.ElevatedButton(text="Iscrivi",
                                              on_click=self._controller.handleIscrivi)
        row3 = ft.Row([self._btn_cercaStudente, self._btn_cercaCorsi, self._btn_iscrivi],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)




        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
