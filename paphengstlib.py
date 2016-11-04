# Module laden
import os
import sys
import importlib
import re

# Hauptverzeichnis ermitteln
maindir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../")

# Weitere Verzeichnisse speichern
resultsdir = os.path.join(maindir, "results/")
uploaddir = os.path.join(maindir, "uploads/")
pythondir = os.path.join(maindir, "paphengst/python/")
htmldir = os.path.join(maindir, "paphengst/html/")
