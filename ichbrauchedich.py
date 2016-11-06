# paphengstlib importieren
from paphengstlib import *

# Ordner "results" für zukünftige Ergebnisse erstellen
os.makedirs(resultsdir, exist_ok=True)

# Ordner "uploads" erstellen, wo die Daten für die Auswertung rein sollen
os.makedirs(uploadsdir, exist_ok=True)

# Zur Erinnerung eine Datei mit Namen "!!! IN DIESEN ORDNER KOMMEN DIE DATEN FÜR DIE AUSWERTUNG !!!" erstellen
filehandle = open(os.path.join(uploadsdir, "!!! IN DIESEN ORDNER KOMMEN DIE DATEN FÜR DIE AUSWERTUNG !!!"), "w")
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

# Das HTML-Menü in "menu.html" erzeugen
menuhtmlcode = """<span>Ein paar Notizen: blabla<br /><br />
<a href="../../uploads">Upload-Ordner</a>
Das Projekt auf GitHub: <a href="https://github.com/paphengst/paphengst">https://github.com/paphengst/paphengst</a>
</span>
<hr />"""
#TODO Menü-Notizen schöner schreiben
for skriptnummer, bezeichnung in skripte:
    if skriptnummer == "---":
        menuhtmlcode += "<br /><hr />\n"
    else:
        menuhtmlcode += "<a class=\"menuitem\" href=\"../../results/" + skriptnummer + ".html\">" + skriptnummer + "<span>" + bezeichnung + "</span></a>\n"
htmlschreiben(os.path.join(htmldir, "menu.html"), "Menü (PAP Hengst)", menuhtmlcode)

# Für jeden Versuch eine leere Ergebnis-HTML speichern (wobei bestehende Ergebnis-HTMLs nicht überschrieben werden)
ergebnishtmlcode = """<span>Versuch noch nicht ausgewertet. Skript starten mit blablabla
</span>
<hr />"""
#TODO Textnotiz für leeren Versuch schöner schreiben
for skriptnummer, bezeichnung in skripte:
    ergebnishtmldatei = os.path.join(resultsdir, skriptnummer + ".html")
    if not os.path.isfile(ergebnishtmldatei):
        htmlschreiben(ergebnishtmldatei, "Versuch " + skriptnummer + " (PAP Hengst)", ergebnishtmlcode)

# Den Link zum HTML-Menü ausgeben
username = os.path.basename(os.environ["HOME"])
linktext = "Link zum HTML-Menü für PythonAnywhere Benutzer \"" + username + "\":"
print("\n\n" + linktext + "\n" + "-" * len(linktext))
print("https://www.pythonanywhere.com/user/" + username +  "/files" + os.path.join(libdir, "html/menu.html"))
print("(Am besten per Copy'n'paste in einem neuen Browser-Tab einfügen, öffnen und als Bookmark speichern.)")
print("-" * len(linktext) + "\n")
