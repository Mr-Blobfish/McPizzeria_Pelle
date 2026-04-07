# Vul hier de naam van je programma in: Sky Lander World
#
#
# Vul hier jullie namen in: Pelle (en Jordi)
#
#
#


### --------- Bibliotheken en globale variabelen -----------------
import sqlite3
with sqlite3.connect("MCPizzeria.db") as db:
 #cursor is object waarmee je data uit de database kan halen
 cursor = db.cursor()


### ---------  Functie definities  -----------------



### --------- Hoofdprogramma  ---------------
def maakTabellenAan():
 # Maak een nieuwe tabel met 3 kolommen: id, naam, prijs
 cursor.execute("""
 CREATE TABLE IF NOT EXISTS tbl_pizzas(
 gerechtID INTEGER PRIMARY KEY AUTOINCREMENT,
 gerechtNaam TEXT NOT NULL,
 gerechtPrijs REAL NOT NULL);""")
 print("Tabel 'tbl_pizzas' aangemaakt.")
