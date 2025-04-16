import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCercaIscritti(self, e):
        self._view.txt_result.controls.clear()
        corso = self._view.dd_corsi.value
        if not corso or corso=="":
            self._view.create_alert("Inserire un corso")
            return
        studenti = self._model.cercaIscritti(corso)
        self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(studenti)} iscritti al corso:"))
        for s in studenti:
            self._view.txt_result.controls.append(
                ft.Text(str(s))
            )
        self._view.update_page()

    def handleCercaStudente(self, e):
        matr = self._view.txt_matr.value
        if not matr or matr=="":
            self._view.create_alert("Inserisci matricola")
            self._view.txt_nome.value = ""
            self._view.txt_cognome.value = ""
            self._view.update_page()
            return
        try:
            matr = int(matr)
        except ValueError:
            self._view.create_alert("Matricola non valida. Assicurati che sia un numero intero.")
            self._view.txt_nome.value = ""
            self._view.txt_cognome.value = ""
            self._view.update_page()
            return
        studente = self._model.cercaStudente(matr)
        if not studente or studente=="":
            self._view.create_alert("Matricola non valida")
            self._view.txt_nome.value = ""
            self._view.txt_cognome.value = ""
            self._view.update_page()
            return
        self._view.txt_nome.value = studente._nome
        self._view.txt_cognome.value = studente._cognome
        self._view.update_page()

    def handleCercaCorsi(self, e):
        self._view.txt_result.controls.clear()
        self.handleCercaStudente(e)
        matr = self._view.txt_matr.value
        corsi = self._model.corsiSeguiti(matr)
        if not corsi or len(corsi)==0:
            self._view.create_alert("Matricola non valida o nessun corso seguito")
            return
        self._view.txt_result.controls.append(ft.Text(f"Lo studente è iscritto a {len(corsi)} corsi:"))
        for c in corsi:
            self._view.txt_result.controls.append(
                ft.Text(str(c)))
        self._view.update_page()

    def handleIscrivi(self, e):
        pass


