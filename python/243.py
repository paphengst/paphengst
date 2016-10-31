import os

#Beispielcode für matplotlib-Plots
"""
import numpy
import sympy
print(numpy.pi)
print(sympy.diff("x**2", "x"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(100))
fig.savefig("graph.png")
"""

#LaTeX output nach 243.tex

versuchsnummer = "243"
resultsdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../results/")
texfile = os.path.join(resultsdir, versuchsnummer + ".tex")
pdffile = os.path.join(resultsdir, versuchsnummer + ".pdf")
pngfile = os.path.join(resultsdir, versuchsnummer + ".png")

s = r"""\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\setlength{\parindent}{0pt}
\begin{document}

blabla

\end{document}
"""
text_file = open(texfile, "w")
text_file.write(s)
text_file.close()

#PDF erzeugen
os.system("pdflatex --output-directory=" + resultsdir + " " + texfile)

#PNGs erzeugen
os.system("convert -density 150 " + pdffile + " " + pngfile)
#ergibt z-0.png, z-1.png, ..., z-33.png
#anzahl der PNGs rausfinden und HTML entsprechend erzeugen:
