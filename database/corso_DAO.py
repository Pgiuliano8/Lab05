# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso

def getAllcorsi():
    con = get_connection()
    cursor = con.cursor()
    query = ("SELECT * FROM corso")
    cursor.execute(query)
    results = cursor.fetchall()
    corsi = []
    for row in results:
        corso = Corso(row[0], row[1], row[2], row[3])
        corsi.append(corso)
    cursor.close()
    con.close()
    return corsi

def getCorsiByStudente(matricola):
    con = get_connection()
    cursor = con.cursor()
    query = ("""SELECT * 
                FROM corso
                JOIN iscrizione i ON corso.codins = i.codins
                WHERE i.matricola = %s
    """)
    cursor.execute(query, (matricola,))
    results = cursor.fetchall()
    corsiSeguiti = []
    for row in results:
        corso = Corso(row[0], row[1], row[2], row[3])
        corsiSeguiti.append(corso)
    cursor.close()
    con.close()
    return corsiSeguiti
