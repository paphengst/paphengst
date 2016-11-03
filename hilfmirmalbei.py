import os
import sys

# Hauptverzeichnis ermitteln
maindir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../")

# Fehler ausgeben, falls kein Parameter angegeben
#TODO

# Skriptverzeichnis "python" nach Skript für angegebenem Parameter durchsuchen
pythondir = os.path.join(maindir, "paphengst/python/")
pythonfiles = os.listdir(pythondir)
for item in pythonfiles:
    if sys.argv[1] == item.replace(".py", "") and os.isfile(os.join(pythondir, item)):
        pythonfile = os.path.join(pythondir, item)
        print("Datei \"" + pythonfile + "\" gefunden")
        break

# Datei ausführen
print("Ausführung wird startet")
os.system("python3 " + pythonfile)

# Meldung ausgeben, dass beendet
print("Ausführung ist beendet")
