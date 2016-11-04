# paphengstlib importieren
from paphengstlib import *

# Alle Dateien und Ordner im Ordner "paphengst" und seinen Unterordnern löschen
for path, folders, files in os.walk(libdir, topdown=False):
    for file in files:
        os.remove(os.path.join(path, file))
    for folder in folders:
        os.rmdir(os.path.join(path, folder))

# Dateien frisch von Github laden
os.system("git clone --depth=1 https://github.com/paphengst/paphengst.git \"" + libdir + "\"")

# Dateistruktur (neu) initialisieren
importlib.import_module("ichbrauchedich", package=None)
