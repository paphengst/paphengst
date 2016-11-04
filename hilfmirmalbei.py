# paphengstlib importieren
from paphengstlib import *

# Skriptverzeichnis "python" nach Skript für angegebenem Parameter durchsuchen
pythonfiles = os.listdir(pythondir)
pythonfile = ""
for item in pythonfiles:
    if (sys.argv[1] if len(sys.argv) > 1 else "") == item.replace(".py", "") and os.path.isfile(os.path.join(pythondir, item)):
        pythonfile = sys.argv[1]
        print("Skript \"" + os.path.join(pythondir, item) + "\" gefunden")
        break

# Überprüfen ob Skript gefunden
if pythonfile == "":
    print("Nicht gefunden")
    sys.exit()

# Modulpfad hinzufügen und Skript ausführen
print("Ausführung wird gestartet")
sys.path = [pythondir] + sys.path
importlib.import_module(pythonfile, package=None)
print("Ausführung ist beendet")
