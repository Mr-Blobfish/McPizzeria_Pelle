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
def zoekKlant():
    #haal de ingevoerde_klantnaam op uit het invoerveld
    # en gebruik dit om met SQL de klant in database te vinden
    gevonden_klanten = MCPizzeriaSQL.zoekKlantInTabel(ingevoerde_klantnaam.get())
    print(gevonden_klanten) # om te testen
    
    invoerveldKlantnaam.delete(0, END) #invoerveld voor naam leeg maken
    invoerveldKlantNr.delete(0, END) #invoerveld voor klantNr leeg maken
    for rij in gevonden_klanten: #voor elke rij dat de query oplevert
        #toon klantnummer, de eerste kolom uit het resultaat in de invoerveld
        invoerveldKlantNr.insert(END, rij[0])
        #toon klantAchternaam, de tweede kolom uit het resultaat in de invoerveld
        invoerveldKlantnaam.insert(END, rij[1]) 

def toonMenuInListbox():
    listboxMenu.delete(0, END) #maak de listbox leeg
    listboxMenu.insert(0, "ID Gerecht Prijs")
    pizza_tabel = MCPizzeriaSQL.vraagOpGegevensPizzaTabel()
    for regel in pizza_tabel:
        listboxMenu.insert(END, regel) #voeg elke regel uit resultaat in listboxMenu
def haalGeselecteerdeRijOp(event): # functie voor het selecteren van een rij uit de listbox en deze in een andere veld teplaatsen
    #bepaal op welke regel er geklikt is
    geselecteerdeRegelInLijst = listboxMenu.curselection()[0]
    #haal tekst uit die regel
    geselecteerdeTekst = listboxMenu.get(geselecteerdeRegelInLijst)
    #verwijder tekst uit veld waar je in wilt schrijven, voor het geval er al iets staat
    invoerveldGeselecteerdePizza.delete(0, END)
    #zet tekst in veld
    invoerveldGeselecteerdePizza.insert(0, geselecteerdeTekst[1])

#voeg de bestelling van klant met gekozen pizza en aantal toe
#in de winkelwagentabel
#en toon de bestelling in de listbox op het scherm
def voegToeAanWinkelWagen():
    klantNr = invoerveldKlantNr.get()
    gerechtID = ingevoerde_pizza.get()
    aantal = aantalGekozen.get()
    MCPizzeriaSQL.voegToeAanWinkelWagen(klantNr, gerechtID, aantal )
    winkelwagen_tabel = MCPizzeriaSQL.vraagOpGegevensWinkelWagenTabel()
    listboxWinkelwagen.delete(0, END) #listbox eerst even leeg maken
    for regel in winkelwagen_tabel:
        listboxWinkelwagen.insert(END, regel)

### --------- Hoofdprogramma  ---------------
venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Pizzeria")

labelIntro = Label(venster, text="Welkom!")
labelIntro.grid(row=0, column=0, sticky="W")

# Klanten GUI
labelKlantNaam = Label(venster, text="Klant Naam:")
labelKlantNaam.grid(row=1, column=0)

ingevoerde_klantnaam = StringVar()
invoerveldKlantnaam = Entry(venster, textvariable=ingevoerde_klantnaam)
invoerveldKlantnaam.grid(row=1, column=1, sticky="W")

klantZoekKnopOpNaam = Button(venster, text="Zoek Klant", command=zoekKlant)
klantZoekKnopOpNaam.grid(row=1, column=3)


labelKlantNr = Label(venster, text="Klant Nr:")
labelKlantNr.grid(row=2, column=0)

invoerveldKlantNr = Entry(venster)
invoerveldKlantNr.grid(row=2, column=1, sticky="W")

# Pizza GUI
labelPizzas = Label(venster, text="Mogelijkheden")
labelPizzas.grid(row=5, column=0)

listboxMenu = Listbox(venster, height=6, width= 50)
listboxMenu.grid(row=5, column=1, rowspan=6, columnspan=2, sticky="W")
listboxMenu.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)

scrollbarlistbox = Scrollbar(venster)
scrollbarlistbox.grid(row=5, column=2, rowspan=6, sticky="E")
listboxMenu.config(yscrollcommand=scrollbarlistbox.set)
scrollbarlistbox.config(command=listboxMenu.yview)

labelGekozenPizza = Label(venster, text="GekozenPizza")
labelGekozenPizza.grid(row=12, column=0)

ingevoerde_pizza = StringVar()
invoerveldGeselecteerdePizza = Entry(venster, textvariable=ingevoerde_pizza)
invoerveldGeselecteerdePizza.grid(row=12, column=1, sticky="W")

knopToonPizzas = Button(venster, text="Toon alle pizza’s", width=12, command=toonMenuInListbox)
knopToonPizzas.grid(row=3, column=4)

# aantal Pizza's
labelAantal = Label(venster, text="Aantal")
labelAantal.grid(row=13, column=0)

aantalGekozen = IntVar()
aantalGekozen.set(1)
optionMenuPizzaAantal = OptionMenu(venster, aantalGekozen, 1,2,3)
optionMenuPizzaAantal.grid(row=13, column=1)


knopVoegToeAanWinkelWagen = Button(venster, text="Voeg toe", width=12, command=voegToeAanWinkelWagen)
knopVoegToeAanWinkelWagen.grid(row=13, column=4)


listboxWinkelwagen = Listbox(venster, height= 3, width= 30)
listboxWinkelwagen.grid(row=14, column=1, rowspan=3, columnspan=2, sticky="W")

labelBestelling = Label(venster, text="Bestelling")
labelBestelling.grid(row=14, column=0)






sluitKnop = Button(venster, text=('Die'), width= 15, height= 1, command= venster.destroy)
sluitKnop.grid(row= 17, column= 4)

#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()