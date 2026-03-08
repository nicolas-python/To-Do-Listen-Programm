#To-Do-Listen-Programm
#menü
to_do_liste= []

def to_do_list_menue():
    choice = None

    while choice not in ["1","2","3","4"]:
        print("To Do Liste:")
        print("1 = Anzeigen")
        print("2 = hinzufügen")
        print("3 = Löschen")
        print("4 = Beenden")

        choice = input("Wähle eine Option:")

        if choice not in ["1","2","3","4"]:
            print("Ungültige Option, bitte erneut wählen.")

    return choice

#funktionen
def anzeigen():

    if to_do_liste == []:
        print("Keine Aufgaben mehr")

    else :
        print ("Deine Aufgaben:")
        for aufgaben in to_do_liste:
            print(aufgaben)



def hinzufuegen():
        print("Was möchtest du hinzufügen? :")
        aufgabe = input()
        to_do_liste.append(aufgabe)
        print("Aufgabe hinzugefügt")


def loeschen():
    print("Was möchtest du löschen")
    aufgabe = input()

    if aufgabe in to_do_liste:
        to_do_liste.remove(aufgabe)
        print("Die aufgabe wurde gelöscht")

    else:
        print("Aufgabe nicht gefunden")


#funktionen abrufen
while True :
    choice = to_do_list_menue()

    if choice == "1":
        anzeigen()

    if choice == "2":
        hinzufuegen()

    if choice == "3":
        loeschen()

    if choice == "4":
        print("Beenden")
        break





