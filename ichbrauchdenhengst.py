import os

# Hauptverzeichnis ermitteln
maindir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../")

# Ordner "results" für zukünftige Ergebnisse erstellen
resultsdir = os.path.join(maindir, "results/")
os.makedirs(resultsdir, exist_ok=True)

# Ordner "uploads" erstellen, wo die Daten für die Auswertung rein sollen
uploaddir = os.path.join(maindir, "uploads/")
os.makedirs(uploaddir, exist_ok=True)

# Zur Erinnerung  eine Datei mit Namen "!!! IN DIESEN ORDNER KOMMEN DIE DATEN FÜR DIE AUSWERTUNG !!!" erstellen
filehandle = open(os.path.join(uploaddir, "!!! IN DIESEN ORDNER KOMMEN DIE DATEN FÜR DIE AUSWERTUNG !!!"), "w")
filehandle.close()

# Menüskript paphengst.py schreiben (Versuchsauswertung, Link zur HTML anzeigen, Update)
#filehandle = open(os.path.join(maindir, "paphengst.py"), "w")
content = """git clone --depth=1 https://github.com/paphengst/paphengst
python3 paphengst/ichbrauchdenhengst.py
"""
#filehandle.write(content)
#filehandle.close()

# Updateablauf: paphengst-Ordner löschen (alte results und uploads bleiben erhalten), per git neuen Code laden, paphengst/ichbrauchdenhengst.py ausführen für neue Installation
for path, folders, files in os.walk(os.path.join(maindir, "paphengst/"), topdown=False):
    for file in files:
        os.remove(os.path.join(path, file))
    for folder in folders:
        os.rmdir(os.path.join(path, folder))
