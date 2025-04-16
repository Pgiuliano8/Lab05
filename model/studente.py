class Studente:
    def __init__(self, matricola, cognome, nome, CDS):
        self._matricola = matricola
        self._cognome = cognome
        self._nome = nome
        self._CDS = CDS

    @property
    def matricola(self):
        return self._matricola

    def __str__(self):
        return f"{self._nome}, {self._cognome} ({self._matricola})"