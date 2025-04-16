from database.studente_DAO import getStudentiByCodins
from database.corso_DAO import getAllcorsi
studenti = getStudentiByCodins()
for s in studenti:
    print(s)
corsi = getAllcorsi()
for c in corsi:
    print(c)
