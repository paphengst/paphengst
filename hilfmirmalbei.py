import os
import sys

# Hauptverzeichnis ermitteln
maindir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../")

# Skriptverzeichnis "python" nach Skript für angegebenem Parameter durchsuchen
pythondir = os.path.join(maindir, "paphengst/python/")
pythonfiles = os.listdir(pythondir)
pythonfile = ""
for item in pythonfiles:
    if (sys.argv[1] if len(sys.argv) > 1 else "") == item.replace(".py", "") and os.path.isfile(os.path.join(pythondir, item)):
        pythonfile = os.path.join(pythondir, item)
        print("Datei \"" + pythonfile + "\" gefunden")
        break

# Überprüfen ob Skript gefunden
if pythonfile == "":
    print("Nicht gefunden")
    sys.exit()

# Datei ausführen
print("Ausführung wird gestartet")
os.system("python3 " + pythonfile)

# Meldung ausgeben, dass beendet
print("Ausführung ist beendet")
