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

#LaTeX output nach z.tex

resultsdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../results/z.tex")

s = r"""\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\setlength{\parindent}{0pt}
\begin{document}

blabla
\end{document}
"""
text_file = open(resultsdir, "w")
text_file.write(s)
text_file.close()

#pdflatex z.tex
os.system("pdflatex z.tex")

#convert -density 150 z.pdf z.png
#ergibt z-0.png, z-1.png, ..., z-33.png
os.system("convert -density 150 z.pdf z.png")
