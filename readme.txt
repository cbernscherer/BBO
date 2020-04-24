memberlist.py
=============

Das Script verwendet die Datei "Spielerliste BBO" und extrahiert daraus Namen und BBO Nicks. Pro Spieler werden
bis zu 5 Nicks akzeptiert. Die Datei muss als Excel von unserem Google Drive Ordner heruntergeladen und in dasselbe
Verzeichnis wie das Script gelegt werden.

Die Ausgabe heißt "bridgewebs_import.csv" und kann in BridgeWebs importiert werden.

Das Script benötigt das Paket pandas.

Alle markieren in BridgeWebs mit
v1=document.querySelectorAll("input[type=checkbox]")
for(var i=0;i<v1.length;i++){v1[i].checked=true;}