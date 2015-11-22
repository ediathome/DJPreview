# DJPreview

Didaktische Jahresplanung **syntax highlighting** plugin and **color scheme** for Sublime Text 3 based on Markdown syntax.

## Features

- Schnelle Erstellung von Didaktischen Jahresplänen in Sublime Text 3
- Basierend auf dem [Markdown Standard](https://daringfireball.net/projects/markdown/) von John Gruber
- Kurzbefehle zum schnellen Erstellen der notwendigen Dokumentenstruktur
- Textergänzung mit Verben-Listen für unterschiedliche Kompetenzbereichen

## SublimeText und DJPreview installieren

1. [Download der aktuellen Version von SublimeText](http://www.sublimetext.com/3) (in der Regel die Version für Windows 64-Bit, für Mac oder Linux die jeweils aktuelle Version)
2. SublimeText starten
3. Befehl **Windows:** "Preferences -> Browse Packages" / **Mac:** "SublimeText -> Preferences -> Browse Packages" auswählen. Es öffnet sich ein Fenster im Windows Explorer bzw. Finder (Mac).
4. Die [Zip-Datei](https://github.com/ediathome/DJPreview/archive/master.zip) herunterladen und in den soeben geöffneten Ordner 'User' entpacken. Bitte beachten Sie, dass die Dateiendung .tmSnippet erhalten bleibt.

## Lernfeld in SublimeText eingeben
1. In SublimeText können nun ab sofort die Textsnippets abgerufen werden. Eine Übersicht über alle Tastenkürzel siehe unten.
2. Wenn das Lernfeld fertig eingegeben ist, drücken Sie strg + R (Windows) oder Command + R (Mac). Die Seite [http://vt-learn.de/didplanapp/stable/index.html](http://vt-learn.de/didplanapp/stable/index.html) wird aufgerufen und der Text in die Zwischenablage kopiert. Fügen Sie den Text aus der Zwischenablage in das Eingabefeld ein und klicken auf "Vorschau". Das Lernfeld wird formatiert ausgegeben. Über den Befehl "Drucken" wird der Druck-Dialog geöffnet.

## Tab-Kürzel
Geben Sie die folgenden Kürzel, gefolgt von der Tabulator-Taste ein, um die Vorlagen abzurufen. Wenn der Vorlagentext eingefügt ist, können Sie mit der Tabulator-Taste zu den Eingabefeldern springen.

|Tab-Kürzel | Ausgabe |
|-----------|---------|
|__lf__     |Überschrift für ein Lernfeld |
|__ls__     |Vorlage für eine Lernsituation im Didaktischen Jahresplan |
|__lsb__    |Vorlage für eine Lernsituationsbeschreibung |

## Textergänzung und Wortvorschläge
Drücken Sie strg + Leertaste, um Wortvorschläge zu erhalten. Das DJPreview-Plugin erkennt, in welchem Kontext Sie sich gerade befinden und gibt zu den momentan bearbeiteten Kompetenzen passende Verbvorschläge an.