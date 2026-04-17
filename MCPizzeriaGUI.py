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

### ---------  Functie definities  -----------------


### --------- Hoofdprogramma  ---------------
venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Pizzeria")

labelIntro = Label(venster, text="Welkom!")
labelIntro.grid(row=0, column=0, sticky="W")

labelKlantNaam = Label(venster, text="Klant Naam:")
labelKlantNaam.grid(row=1, column=0)

ingevoerde_klantnaam = StringVar()
invoerveldKlantnaam = Entry(venster, textvariable=ingevoerde_klantnaam)
invoerveldKlantnaam.grid(row=1, column=1, sticky="W")

labelKlantNr = Label(venster, text="Klant Nr:")
labelKlantNr.grid(row=2, column=0)

invoerveldKlantNr = Entry(venster)
invoerveldKlantNr.grid(row=2, column=1, sticky="W")




sluitKnop = Button(venster, text=('Die'), width= 15, height= 1, command= venster.destroy)
sluitKnop.grid(row= 17, column= 4)

#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()