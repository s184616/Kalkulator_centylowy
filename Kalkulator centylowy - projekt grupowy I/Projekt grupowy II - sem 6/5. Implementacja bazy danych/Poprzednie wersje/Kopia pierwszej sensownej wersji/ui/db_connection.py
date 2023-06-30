import mysql.connector
import pandas

# Creating connection object
mydb = mysql.connector.connect(
    host="marchapp.sytes.net",
    user="web_root",
    password="@#fasv#FAe576!@",
    database="ksiazeczka_zdrowia"
)
cursor = mydb.cursor()


def read_patients_from_base():
    cursor.execute("SELECT * FROM pacjent")
    return cursor.fetchall()


def read_patient_data(pesel: str):
    query = "SELECT p.płeć, s.`wiek[miesiace]`, s.`wysokosc[cm]`, s.`waga[kg]`, s.`obwod_glowy[cm]` FROM " \
            "siatka_centylowa s JOIN pacjent p ON p.pesel = s.pesel WHERE s.pesel = %s "
    val = [pesel]
    cursor.execute(query, val)
    return pandas.DataFrame(cursor.fetchall(), columns=["Gender", "Age", "Height", "Weight", "Head Circumference"])


def save_new_patient(info: list):
    # assuming list format: (pesel, imie, nazwisko, płeć, imia_ojca, imie_matki)
    query = "INSERT INTO pacjent VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.execute(query, info)
    mydb.commit()


def save_patients_data(data: list):
    # assuming list format: (pesel, wiek, wysokosc, waga, obwód głowy)
    query = "INSERT INTO siatka_centylowa (`pesel`, `wiek[miesiace]`, `wysokosc[cm]`, `waga[kg]`, `obwod_glowy[cm]`)"\
            "VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, data)
    mydb.commit()


def check_gender(pesel: str):
    query = "SELECT `płeć` FROM pacjent WHERE pesel = %s"
    cursor.execute(query, [pesel])
    return cursor.fetchall()[0][0]
