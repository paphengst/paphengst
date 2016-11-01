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

# Skripte aufzählen
skripte = [
    [211, "Gekoppelte Pendel"],
    [212, "Zähigkeit von Flüssigkeiten"],
    [213, "Kreisel"],
    [221, "Adiabatenkoeffizient"],
    [222, "Heißuftmotor"],
    [223, "Boltzmannkonstante Teil I Brownsche Bewegung"],
    [232, "Michelson-Interferometer"],
    [233, "Fourieroptik"],
    [234, "Lichtquellen und Gitterspektroskopie"],
    [241, "Wechselstrom- eigenschaften von RCL-Gliedern"],
    [242, "Spannungsverstärkung"],
    [243, "Boltzmannkonstante Teil II Thermisches Rauschen"],
    [245, "Induktion"],
    [251, "Statistik"],
    [252, "Aktivierung mit thermischen Neutronen"],
    [253, "Absorption von α- β- und γ-Strahlen"],
    [255, "Röntgenspektrometer"],
    [256, "Röntgenfluoreszenz"],
    ]

# Die Template-HTML einlesen
htmldir = os.path.join(maindir, "paphengst/html/")
filehandle = open(os.path.join(htmldir, "template.html"), "r")
templatehtml = filehandle.read()
filehandle.close()

# Aus dem Array mit den Skripten eine Liste fürs HTML erstellen
menuhtml = templatehtml.replace("<title></title>", "<title>Menü (PAP Hengst)</title>")
for skriptnummer, bezeichnung in skripte:
    menuhtml = menuhtml.replace("<!-- snipsnap -->", "<a class=\"menuitem\">" + str(skriptnummer) + "<span>" + bezeichnung + "</span></a>\n<!-- snipsnap -->")

# Das HTML für die "menu.html" speichern
filehandle = open(os.path.join(htmldir, "menu.html"), "w")
filehandle.write(menuhtml)
filehandle.close()

# Den Link zum HTML-Menü ausgeben
username = os.path.basename(os.environ["HOME"])
s = "Link zum HTML-Menü für PythonAnywhere Benutzer \"" + username + "\":"
print("\n\n" + s + "\n" + "-" * len(s))
print(r"https://www.pythonanywhere.com/user/" + username +  r"/files/home/" + username + r"/paphengst/html/menu.html")
print("(Am besten per Copy'n'paste in einem neuen Browser-Tab einfügen, öffnen und als Bookmark speichern.)")
print("-" * len(s) + "\n")
