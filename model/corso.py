class Corso:
    def __init__(self, codins, crediti, nome, pd):
        self._codins = codins
        self._crediti = crediti
        self._nome = nome
        self._pd = pd

    def __str__(self):
        return f"{self._nome} ({self._codins})"

    @property
    def getCodins(self):
        return self._codins