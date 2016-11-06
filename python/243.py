# paphengstlib importieren
from paphengstlib import *

# Versuchsauswertung
latexschreiben(r"blabla blabla blabla ")
latexschreiben(r"\\")
latexschreiben(r"$ \sqrt{77} $")
latexkompilieren()

sys.exit()

def neuegrafikdatei(matplotlibgraph):
    pngfile = os.path.join(resultsdir, "243-1.png")
    matplotlibgraph.savefig(pngfile)
    return pngfile

#Beispielcode für matplotlib-Plots
"""
import numpy
import sympy
print(numpy.pi)
print(sympy.diff("x**2", "x"))
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(100))
a = neuegrafikdatei(fig)

s += r"\\ \\ \includegraphics[width=10cm]{" + a + r"}"
