# Variablen
import pandas as pd



a = 2
b = "hello "
c = 'world'
d= "4"
# Debugging

# string manipulation
print(b+c)


print(f"hello {c}")

name = input("wie lautet dein Name")

print(f"hello {name}")


# Erstellt einen Namensgenerator für euer Projekt.
# Es sollen Variablen genutzt werden, und User input.
# Im Fehlerfall bitte eure "Debugging"-Kenntnisse nutzen und die Fehler identifizieren.

print(a+str(d))

# Dateimanipulation
# Öffnen der Datei im Lesemodus und Lesen des gesamten Inhalts
with open("beispiel.txt", "r") as datei:
    inhalt = datei.read()  # Liest den gesamten Dateiinhalt
print(inhalt)

# Öffnen der Datei und Lesen der ersten Zeile
with open("beispiel.txt", "r") as datei:
    erste_zeile = datei.readline()  # Liest nur die erste Zeile
print(erste_zeile.strip())

# Lesen aller Zeilen und Speichern als Liste
with open("beispiel.txt", "r") as datei:
    zeilen = datei.readlines()  # Liest alle Zeilen in eine Liste
print(zeilen)

# Schreiben von Text in die Datei (überschreibt den Inhalt)
with open("beispiel.txt", "w") as datei:
    datei.write("Das ist ein neuer Text.\n")  # Schreibt eine Zeile in die Datei

# Schreiben mehrerer Zeilen auf einmal
zeilen = ["Zeile 1\n", "Zeile 2\n", "Zeile 3\n"]
with open("beispiel.txt", "w") as datei:
    datei.writelines(zeilen)  # Schreibt die Liste von Zeilen in die Datei


