import os

# Hauptverzeichnis ermitteln
maindir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../")

# Ordner "results" für zukünftige Ergebnisse erstellen
resultsdir = os.path.join(maindir, "results/")
os.makedirs(resultsdir, exist_ok=True)

# Ordner "uploads" erstellen, wo die Daten für die Auswertung rein sollen
uploaddir = os.path.join(maindir, "uploads/")
os.makedirs(uploaddir, exist_ok=True)

# Zur Erinnerung eine Datei mit Namen "!!! IN DIESEN ORDNER KOMMEN DIE DATEN FÜR DIE AUSWERTUNG !!!" erstellen
filehandle = open(os.path.join(uploaddir, "!!! IN DIESEN ORDNER KOMMEN DIE DATEN FÜR DIE AUSWERTUNG !!!"), "w")
filehandle.close()

# Den Link zum HTML-Menü ausgeben
username = os.path.basename(os.environ["HOME"])
s = "Link zum HTML-Menü für PythonAnywhere Benutzer \"" + username + "\":"
print("\n\n" + s + "\n" + "-" * len(s))
print(r"https://www.pythonanywhere.com/user/" + username +  r"/files/home/" + username + r"/paphengst/html/menu.html")
print("(Am besten per Copy'n'paste in einem neuen Browser-Tab einfügen, öffnen und als Bookmark speichern.)")
print("-" * len(s) + "\n")
