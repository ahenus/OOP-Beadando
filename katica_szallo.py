#Szukseges modulok importalasa:
from art import logo
from abc import ABC, abstractmethod
import random
import datetime

#'Szoba' osztaly letrehozasa a fo attributumokkal:
class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

#Ket szarmaztatott osztaly letrehozasa a 'Szoba' osztalyhoz:
class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar, emelet):
        super().__init__(szobaszam, ar)
        self.emelet = emelet
        self.ar = ar

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar, emelet):
        super().__init__(szobaszam, ar)
        self.emelet = emelet
        self.ar = ar

#'Szalloda' osztaly letrehozasa a szallodahoz:
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = {}

#Szobak hozzaadasa a szallodahoz:
    def szobak_hozzaadasa(self):
        self.szobak["101"] = ["Egyágyas szoba", 40000]
        self.szobak["102"] = ["Egyágyas szoba", 40000]
        self.szobak["201"] = ["Kétágyas szoba", 50000]

#'Foglalas' osztaly letrehozasa a foglalasok tarolasahoz:
class Foglalas:
    def __init__(self):
        self.szalloda = Szalloda(" ")
        self.foglalasok = {
            "101":[],
            "102":[],
            "201":[]
        }

#Szobafoglalasi fuggveny definialasa:
    def szobafoglalas(self):
        print(f"\nJelenleg a következő szobáink állnak rendelkezésre a feltüntetett árakkal:"
              f"\n🐞Szobaszám: 101., {szalloda.szobak['101']} HUF"
              f"\n🐞Szobaszám: 102., {szalloda.szobak['102']} HUF"
              f"\n🐞Szobaszám: 201., {szalloda.szobak['201']} HUF")
        valasztott_datum = input("Kérem, adja meg a választani kívánt dátumot YYYY-MM-DD formátumban: ")
        valasztott_szobaszam = input("Kérem, adja meg a foglalandó szoba számát: ")
        if valasztott_datum >= datetime.datetime.now().strftime('%Y-%m-%d'):
            if self.foglalasellenorzo(valasztott_szobaszam, valasztott_datum):
                self.foglalasok[valasztott_szobaszam].append(valasztott_datum)
                print(f"A foglalás sikeres!👌😎 Szobáját az alábbi adatokkal rögzítettük rendszerünkben:"
                      f"\n📆Foglalási dátum: {valasztott_datum}"
                      f"\n🔢Foglalt szoba száma: {valasztott_szobaszam}"
                      f"\n💰A szobafoglalás ára: {szalloda.szobak[valasztott_szobaszam][1]} HUF"
                      f"\nKöszönjük foglalását!🙏🏻🥰")
            else:
                print("Ezen a dátumon a szoba sajnos foglalt.😱 Válasszon másik szobát vagy másik dátumot!🤗\n")
        else:
            print("A foglalás legkorábbi dátuma a mai nap lehet.👉📅")

#Szobalemondasi fuggveny definialasa:
    def lemondas(self):
        print(f"Szobáink az alábbi dátumokon foglaltak:"
              f"\n🐞101-es szoba: {self.foglalasok['101']}"
              f"\n🐞102-es szoba: {self.foglalasok['102']}"
              f"\n🐞201-es szoba: {self.foglalasok['201']}")
        lemondott_datum = input("Kérem, adja meg a lemondani kívánt foglalási dátumot YYYY-MM-DD formátumban: ")
        lemondott_szoba = input("Kérem, adja meg a lemondani kívánt szoba számát: ")
        if self.foglalasellenorzo(lemondott_szoba, lemondott_datum) is False:
            self.foglalasok[lemondott_szoba].remove(lemondott_datum)
            print("A lemondás sikeres volt!👍 Reméljük, még meggondolja magát és később visszatér hozzánk!😊")
        else:
            print("Sajnos ilyen foglalás nincs a rendszerünkben.😔 Kérem, ellenőrizze a bevitt adatokat.🧐")

#Foglalaslistazasi fuggveny definialasa:
    def listazas(self):
        print(f"\nSzobáink az alábbi dátumokon foglaltak:"
              f"\n⛔101-es szoba: {self.foglalasok['101']}"
              f"\n⛔102-es szoba: {self.foglalasok['102']}"
              f"\n⛔201-es szoba: {self.foglalasok['201']}\n")

#Foglalasellenorzo fuggveny definialasa:
    def foglalasellenorzo(self, valasztott_szobaszam, valasztott_datum):
        if valasztott_szobaszam in self.foglalasok:
            lista = self.foglalasok[valasztott_szobaszam]
            if valasztott_datum in lista:
                return False
            return True

#Fuggveny definialasa 5 random foglalashoz:
    def foglalasfeltoltes(self):
        mai_datum = datetime.date.today()
        for i in range(5):
            helyes_datum = mai_datum + datetime.timedelta(days=random.randint(60, 90))
            self.foglalasok[random.choice(list(self.foglalasok.keys()))].append(helyes_datum.strftime('%Y-%m-%d'))


# FOPROGRAM:
szalloda = Szalloda("Katica_Szallo")
foglalas = Foglalas()
szalloda.szobak_hozzaadasa()
foglalas.foglalasfeltoltes()

# FELHASZNÁLÓI MENÜ:
print(logo)
i = True
while i is True:
    print("Az alábbi menüpontok közül választhat:"
          "\n🐞 ❶ 🐞 Szobafoglalások listázása"
          "\n🐞 ❷ 🐞 Szobafoglalás"
          "\n🐞 ❸ 🐞 Szobafoglalás lemondása"
          "\n🐞 ❹ 🐞 Kilépés")

    valasztott_menu = input("Választott menüpont: ")
    if valasztott_menu == "1":
        foglalas.listazas()
    elif valasztott_menu == "2":
        foglalas.szobafoglalas()
    elif valasztott_menu == "3":
        foglalas.lemondas()
    elif valasztott_menu == "4":
        i = False
        print("Térjen vissza hozzánk, ha meggondolta magát! Viszontlátásra!🤗👋")
    else:
        i = False
        print("Sajnos érvénytelen számot/szöveget ütött be. Viszontlátásra!🌷")