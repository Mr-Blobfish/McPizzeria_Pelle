# Dit bestand zorgt voor de gebruikersinterface (GUI)van onze programma.
# Vul hier de naam van je programma in: Sky Lander World
#
#
# Vul hier jullie namen in: Pelle (en Jordi)
#
#
#


### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import MCPizzeriaSQL
import sqlite3
with sqlite3.connect("MCPizzeria.db") as db:
 #cursor is object waarmee je data uit de database kan halen
 cursor = db.cursor()

### ---------  Functie definities  -----------------
def maakTabellenAan():
 # Maak een nieuwe tabel met 3 kolommen: id, naam, prijs
 cursor.execute("""
 CREATE TABLE IF NOT EXISTS tbl_pizzas(
 gerechtID INTEGER PRIMARY KEY AUTOINCREMENT,
 gerechtNaam TEXT NOT NULL,
 gerechtPrijs REAL NOT NULL);""")
 print("Tabel 'tbl_pizzas' aangemaakt.")


### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Pizzeria")









#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
