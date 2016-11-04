# paphengstlib importieren
from paphengstlib import *

# Ordner "results" für zukünftige Ergebnisse erstellen
os.makedirs(resultsdir, exist_ok=True)

# Ordner "uploads" erstellen, wo die Daten für die Auswertung rein sollen
os.makedirs(uploaddir, exist_ok=True)

# Zur Erinnerung eine Datei mit Namen "!!! IN DIESEN ORDNER KOMMEN DIE DATEN FÜR DIE AUSWERTUNG !!!" erstellen
filehandle = open(os.path.join(uploaddir, "!!! IN DIESEN ORDNER KOMMEN DIE DATEN FÜR DIE AUSWERTUNG !!!"), "w")
filehandle.close()

# Skripte aufzählen, die im Menü erscheinen sollen
skripte = [
    ["11", "Einführungsversuch"],
    ["12", "Trägheitsmoment"],
    ["13", "Resonanz"],
    ["14", "Mathematisches Pendel"],
    ["15", "Schiefe Ebene"],
    ["21", "Elektrolyse"],
    ["22", "Bestimmung der Elementarladung nach Millikan"],
    ["23", "Strom- und Spannungsmessung"],
    ["25", "Oszilloskop"],
    ["26", "Schallgeschwindigkeit"],
    ["31", "Optische Abbildung"],
    ["33", "Prismenspektrometer"],
    ["34", "Spektralphotometrie"],
    ["35", "Fotoeffekt"],
    ["41", "Temperaturmessung"],
    ["42", "Spezifische Wärmekapazität fester Körper"],
    ["---", ""],
    ["211", "Gekoppelte Pendel"],
    ["212", "Zähigkeit von Flüssigkeiten"],
    ["213", "Kreisel"],
    ["221", "Adiabatenkoeffizient"],
    ["222", "Heißuftmotor"],
    ["223", "Boltzmannkonstante Teil I Brownsche Bewegung"],
    ["232", "Michelson-Interferometer"],
    ["233", "Fourieroptik"],
    ["234", "Lichtquellen und Gitterspektroskopie"],
    ["241", "Wechselstromeigenschaften von RCL-Gliedern"],
    ["242", "Spannungsverstärkung"],
    ["243", "Boltzmannkonstante Teil II Thermisches Rauschen"],
    ["245", "Induktion"],
    ["251", "Statistik"],
    ["252", "Aktivierung mit thermischen Neutronen"],
    ["253", "Absorption von α- β- und γ-Strahlen"],
    ["255", "Röntgenspektrometer"],
    ["256", "Röntgenfluoreszenz"],
    ]

# Das HTML-Template einlesen
filehandle = open(os.path.join(htmldir, "template.html"), "r")
templatehtml = filehandle.read()
filehandle.close()

# HTML für die "menu.html" aus dem Template erzeugen
menuhtml = templatehtml
menuhtml = menuhtml.replace("<title></title>", "<title>Menü (PAP Hengst)</title>")

# Notizen in "menu.html" einfügen
menuhtmlnotizen = """<span>Ein paar Notizen: blabla<br /><br />
<a href="../../uploads">Upload-Ordner</a>
Das Projekt auf GitHub: <a href="https://github.com/paphengst/paphengst">https://github.com/paphengst/paphengst</a>
</span>
<hr />"""
#TODO Menü-Notizen schöner schreiben
menuhtml = menuhtml.replace("<!-- snipsnap -->", menuhtmlnotizen + "\n<!-- snipsnap -->")

# Aus dem Array mit den Skripten eine Liste fürs HTML erstellen
for skriptnummer, bezeichnung in skripte:
    if skriptnummer == "---":
        menuhtml = menuhtml.replace("<!-- snipsnap -->", "<br /><hr />\n<!-- snipsnap -->")
    else:
        menuhtml = menuhtml.replace("<!-- snipsnap -->", "<a class=\"menuitem\" href=\"../../results/" + skriptnummer + ".html\">" + skriptnummer + "<span>" + bezeichnung + "</span></a>\n<!-- snipsnap -->")

# Das HTML für die "menu.html" speichern
filehandle = open(os.path.join(htmldir, "menu.html"), "w")
filehandle.write(menuhtml)
filehandle.close()

# HTML für die Ergebnis-HTMLs aus dem Template erzeugen
ergebnishtml = templatehtml
ergebnishtml = ergebnishtml.replace("../../paphengst/html/", "../paphengst/html/")
#TODO Textnotiz für leeren Versuch schöner schreiben
ergebnishtmlnotizen = """<span>Versuch noch nicht ausgewertet. Skript starten mit blablabla
</span>
<hr />"""
ergebnishtml = ergebnishtml.replace("<!-- snipsnap -->", ergebnishtmlnotizen + "\n<!-- snipsnap -->")

# Für jeden Versuch eine leere Ergebnis-HTML speichern (wobei bestehende Ergebnis-HTMLs nicht überschrieben werden)
pythonfiles = os.listdir(pythondir)
for item in pythonfiles:
    if item[-3:] == ".py" and os.path.isfile(os.path.join(pythondir, item)):
        htmlfile = os.path.join(resultsdir, item.replace(".py", "") + ".html")
        if not os.path.isfile(htmlfile):
            filehandle = open(htmlfile, "w")
            filehandle.write(ergebnishtml.replace("<title></title>", "<title>Versuch " + item.replace(".py", "") + " (PAP Hengst)</title>"))
            filehandle.close()

# Den Link zum HTML-Menü ausgeben
username = os.path.basename(os.environ["HOME"])
linktext = "Link zum HTML-Menü für PythonAnywhere Benutzer \"" + username + "\":"
print("\n\n" + linktext + "\n" + "-" * len(linktext))
print(r"https://www.pythonanywhere.com/user/" + username +  r"/files/home/" + username + r"/paphengst/html/menu.html")
print("(Am besten per Copy'n'paste in einem neuen Browser-Tab einfügen, öffnen und als Bookmark speichern.)")
print("-" * len(linktext) + "\n")
