import os

# Hauptverzeichnis ermitteln
maindir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../")

# Fehler ausgeben, falls kein Parameter angegeben
#TODO

# Skriptverzeichnis "python" nach angegebenem Parameter durchsuchen
pythondir = os.path.join(maindir, "paphengst/python/")
#TODO

# Datei ausführen
pythonfile = os.path.join(pythondir, "243.py")
print("Datei \"" + pythonfile + "\" wird ausgeführt.")
os.system("python3 " + pythonfile)

# Meldung ausgeben, dass beendet
print("Ausführung beendet")
