# Hol dir den Hengst!

Der PAP Hengst hilft, wo er kann. Und das alles __ohne__ Jupyter Notebook. :stuck_out_tongue_winking_eye:

---

* __Erstinstallation__
  
  Bei PythonAnywhere unter [https://www.pythonanywhere.com](https://www.pythonanywhere.com) ein kostenloses Konto registrieren. Dort eine Bash-Konsole starten und folgende Befehle ausführen, um einen lokalen Klon zu erstellen:
  
      cd $HOME
      git clone --depth=1 https://github.com/paphengst/paphengst.git
      python3 paphengst/ichbrauchedich.py
  
  Wenn alles funktioniert hat sollte nach dem letzten Befehl ein Link zum HTML-Menü ausgegeben werden. Dort finden sich alle weitere Informationen.

---

* __Update__
  
  Um den einen lokalen Klon auf den neusten Stand zu bringen genügen folgende Befehle:
  
      cd $HOME
      python3 paphengst/machdichfrisch.py

  Alle Auswertungen und Messwerte bleiben erhalten. Sollen die auch entfernt werden, einfach die Ordner `results` und `uploads` manuell löschen.

---
