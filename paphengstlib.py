# Module laden
import os
import sys
import importlib
import re

# Hauptverzeichnis ermitteln
maindir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../")
maindir = os.path.abspath(maindir)

# Weitere Verzeichnisse speichern
resultsdir = os.path.join(maindir, "results/")
uploaddir = os.path.join(maindir, "uploads/")
libdir = os.path.join(maindir, "paphengst/")
pythondir = os.path.join(libdir, "python/")
htmldir = os.path.join(libdir, "html/")
