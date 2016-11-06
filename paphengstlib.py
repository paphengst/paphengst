# Module laden
import os
import sys
import importlib
import re

def htmlschreiben(htmldateiname, titel, code):
    # Das HTML-Template einlesen
    filehandle = open(os.path.join(htmldir, "template.html"), "r")
    templatehtml = filehandle.read()
    filehandle.close()
    # In welcher Ordnerebene liegt die neue HTML-Datei im Vergleich zum Ordner mit den Grafiken?
    htmlordnerebene = os.path.abspath(os.path.dirname(os.path.realpath(htmldateiname)))
    # Der Pfad zur neuen HTML-Datei muss mindestens bis zum Hauptverzeichnis gleich sein
    if not htmlordnerebene[:len(maindir)] == maindir:
        sys.exit("Pfad außerhalb des Hauptverzeichnisses nicht erlaubt.")
    # Die Schleife geht Ebene für Ebene zurück, bis das Hauptverzeichnis erreicht ist
    ebenenwechsel = 0
    while True:
        if htmlordnerebene == maindir:
            break
        htmlordnerebene = os.path.abspath(os.path.join(htmlordnerebene, "../"))
        ebenenwechsel = ebenenwechsel + 1
        # Vorsichtshalber Abbrechen, falls Verdacht auf Endlosschleife wegen irgendeinem komischen Fehler
        if ebenenwechsel > 100:
            sys.exit("Hä? Irgendwas stimmt nicht.")
    # Pfade im HTML-Code an die Ordnerebene anpassen
    templatehtml = templatehtml.replace("../../paphengst/html/", "../" * ebenenwechsel + "paphengst/html/")
    # Template anpassen
    templatehtml = templatehtml.replace("<title></title>", "<title>" + titel + "</title>")
    templatehtml = templatehtml.replace("<!-- snipsnap -->", code + "\n<!-- snipsnap -->")
    # Neue HTML-Datei schreiben
    filehandle = open(htmldateiname, "w")
    filehandle.write(templatehtml)
    filehandle.close()
    return None

# Den Dateinamen des Skripts ermitteln, welches die Funktion aufgerufen hat (der Dateiname des Codes von zwei Frames zurück)
def aufrufskriptdateiname():
    filename = sys._getframe().f_back.f_back.f_code.co_filename
    # Alternativ folgender Code (Achtung: eventuell erst ab Python 3.5?)
    #import inspect
    #(frame, filename, line_number, function_name, lines, index) = inspect.getouterframes(inspect.currentframe())[2]
    #print(frame, filename, line_number, function_name, lines, index)
    return filename

# LaTeX-Code in passende Datei im "results" Ordner schreiben
def latexschreiben(latexcode, aufrufendesskript = ""):
    # Falls Parameter "aufrufendesskript" nicht (richtig) gesetzt, dann automatisch zuweisen
    if not os.path.isfile(aufrufendesskript):
        aufrufendesskript = aufrufskriptdateiname()
    # Code zum Zwischenspeicher hinzufügen
    if not aufrufendesskript in latexbuffer:
        latexbuffer[aufrufendesskript] = ""
    latexbuffer[aufrufendesskript] += latexcode
    return None

# LaTeX-Datei mit pdflatex zu PDF-Datei verarbeiten
def latexkompilieren(templatedazu = True, aufrufendesskript = ""):
    # Falls Parameter "aufrufendesskript" nicht (richtig) gesetzt, dann automatisch zuweisen
    if not os.path.isfile(aufrufendesskript):
        aufrufendesskript = aufrufskriptdateiname()
    # Aus dem Dateinamen des aufrufenden Skripts die Dateinamen der TEX-, PDF- und PNG-Dateien erzeugen
    skriptnummer = os.path.basename(aufrufendesskript).replace(".py", "")
    texdateiname = os.path.join(resultsdir, skriptnummer + ".tex")
    pdfdateiname = os.path.join(resultsdir, skriptnummer + ".pdf")
    pngdateiname = os.path.join(resultsdir, skriptnummer + ".png")
    htmldateiname = os.path.join(resultsdir, skriptnummer + ".html")
    # Sicherstellen, dass überhaupt Daten im Buffer existieren (wenn auch nur "")
    latexschreiben("", aufrufendesskript)
    # Header und Footer hinzufügen
    if templatedazu:
        latexbuffer[aufrufendesskript] = latexheader + latexbuffer[aufrufendesskript] + latexfooter
    # TEX-Datei schreiben
    filehandle = open(texdateiname, "w")
    filehandle.write(latexbuffer[aufrufendesskript])
    filehandle.close()
    # Buffer leeren
    latexbuffer[aufrufendesskript] = ""
    # Alte PDF-Datei löschen
    if os.path.isfile(pdfdateiname):
        os.remove(pdfdateiname)
    # Kompilieren mit pdflatex
    os.system("pdflatex -halt-on-error -output-directory=\"" + resultsdir + "\" \"" + texdateiname + "\"")
    # Falls keine PDF-Datei existiert, war da wohl ein Fehler
    if not os.path.isfile(texdateiname):
        #TODO HTML erzeugen
        return None
    # PNGs im "results" Ordner suchen (weil ja die Seitenzahl des PDFs und damit die Anzahl der PNGs unbekannt)
    gefundenepngs = lambda: re.findall(skriptnummer + r"(?:-[0-9]*?)?\.png", " ".join(os.listdir(resultsdir)), re.IGNORECASE)
    # Alte PNGs löschen
    for pngdatei in gefundenepngs():
        os.remove(os.path.join(resultsdir, pngdatei))
    # Aus der PDF-Datei PNGs mit ImageMagick erzeugen
    os.system("convert -density 150 \"" + pdfdateiname + "\" \"" + pngdateiname + "\"")
    print("Gefundene PNGs:", gefundenepngs())
    #TODO Sortieren notwendig?
    # HTML erzeugen
    htmltitel = "Versuch " + skriptnummer + " (PAP Hengst)"
    htmlcode = "<a href=\"http://www.google.de\"><button><span></span>PDF-Datei downloaden</button></a>\n"
    for pngdatei in gefundenepngs():
        htmlcode += "<br />\n"
        htmlcode += "<img src=\"" + pngdatei + "\" />\n"
    htmlschreiben(htmldateiname, htmltitel, htmlcode)
    return None

# LaTeX-Header und -Footer
latexheader = r"""\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{color}
\setlength{\parindent}{0pt}
\begin{document}
\pagecolor{white}
"""
latexfooter = r"""
\end{document}
"""

# Zwischenspeicher für LaTeX-Code, bevor er in die Datei geschrieben wird
latexbuffer = {}

# Hauptverzeichnis ermitteln
maindir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../")
maindir = os.path.abspath(maindir)

# Weitere Verzeichnisse speichern
resultsdir = os.path.join(maindir, "results/")
uploadsdir = os.path.join(maindir, "uploads/")
libdir = os.path.join(maindir, "paphengst/")
pythondir = os.path.join(libdir, "python/")
htmldir = os.path.join(libdir, "html/")
