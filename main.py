# =========================
# TO-DO LIST APP (Deutsch)
# =========================

aufgaben = []

while True:
    print("\n====== TO-DO LISTE ======")
    print("1 - Aufgabe hinzufügen")
    print("2 - Aufgaben anzeigen")
    print("3 - Aufgabe löschen")
    print("4 - Programm beenden")

    auswahl = input("Wähle eine Option: ")

    # Aufgabe hinzufügen
    if auswahl == "1":
        aufgabe = input("Neue Aufgabe eingeben: ")
        aufgaben.append(aufgabe)
        print("Aufgabe hinzugefügt!")

    # Aufgaben anzeigen
    elif auswahl == "2":
        if len(aufgaben) == 0:
            print("Keine Aufgaben vorhanden.")
        else:
            print("\nDeine Aufgaben:")
            for i, aufgabe in enumerate(aufgaben, start=1):
                print(f"{i}. {aufgabe}")

    # Aufgabe löschen
    elif auswahl == "3":
        if len(aufgaben) == 0:
            print("Keine Aufgaben zum Löschen.")
        else:
            print("\nAufgaben:")
            for i, aufgabe in enumerate(aufgaben, start=1):
                print(f"{i}. {aufgabe}")

            nummer = int(input("Welche Aufgabe löschen? Nummer eingeben: "))

            if 1 <= nummer <= len(aufgaben):
                geloescht = aufgaben.pop(nummer - 1)
                print(f"'{geloescht}' wurde gelöscht.")
            else:
                print("Ungültige Nummer!")

    # Programm beenden
    elif auswahl == "4":
        print("Programm beendet. Tschüss ")
        break

    # Falsche Eingabe
    else:
        print("Ungültige Auswahl!")