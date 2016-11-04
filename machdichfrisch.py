# paphengstlib importieren
from paphengstlib import *

# Alle Dateien und Ordner im Ordner "paphengst" und seinen Unterordnern löschen
for path, folders, files in os.walk(os.path.join(maindir, "paphengst/"), topdown=False):
    for file in files:
        os.remove(os.path.join(path, file))
    for folder in folders:
        os.rmdir(os.path.join(path, folder))

# Dateien frisch von Github laden
os.system("git clone --depth=1 https://github.com/paphengst/paphengst")

# Dateistruktur (neu) initialisieren
os.system("python3 paphengst/ichbrauchedich.py")
