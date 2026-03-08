#To-Do-Listen-Programm
#menü
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

