
from database.corso_DAO import getAllcorsi, getCorsiByStudente
from database.studente_DAO import getStudentiByCodins, getAllStudenti

class Model:
    def __init__(self):
        self._corsi = getAllcorsi()
        self._studenti = getAllStudenti()

    def cercaIscritti(self, corso):
        """
        prende come parametro un oggetto di tipo Corso e restituisce tutti gli studenti che
        lo seguono
        :param corso: Oggetto di tipo Corso
        :return: lista di studenti
        """
        return getStudentiByCodins(corso)

    def cercaStudente(self, matricola):
        for s in self._studenti:
            if s.matricola == matricola:
                return s
        return None

    def corsiSeguiti(self, matricola):
        return getCorsiByStudente(matricola)


