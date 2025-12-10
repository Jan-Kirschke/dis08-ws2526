# Mein Markdown Cheat Sheet

Quelle: https://www.markdowntutorial.com/

---

## 1. Basic Formatting
Grundlagen, um Texte lesbar zu machen.

### Headings (Überschriften)
Ich nutze Rauten (#) für Überschriften.
# Hauptüberschrift (H1)
## Unterüberschrift (H2)
### Kleinerer Abschnitt (H3)

### Paragraphs & Line Breaks
Ein "Enter" im Code reicht oft nicht.
* **Neuer Absatz:** Eine Leerzeile lassen.
* **Zeilenumbruch (weich):** Zwei Leerzeichen am Ende der Zeile.  

### Text Styles
Hervorhebungen im Text:
**Fett** oder __Fett__
*Kursiv* oder _Kursiv_
***Fett und Kursiv***
~~Durchgestrichen~~

---

## 2. Lists
Listen helfen mir, Struktur reinzubringen.

### Unordered (Aufzählung)
Ich mag Bindestriche (-), aber (*) geht auch.
- Einkaufen
- Lernen
  - Markdown (eingerückt mit Tab)
  - Git

### Ordered (Nummeriert)
Die Zahlen im Code sind egal, Markdown zählt automatisch richtig.
1. Erster Punkt
1. Zweiter Punkt (wird automatisch zu 2.)
1. Dritter Punkt

---

## 3. Links & Images
Verweise und Bilder einbinden.

### Links
Text in eckige Klammern [], URL in runde ().
Hier ist ein Link zu [Google](https://www.google.com).

### Reference-style Links
Hält den Text sauberer. Ich definiere den Link ganz unten im Dokument.
Hier ist ein Link zu [Wikipedia][wiki].

[wiki]: https://www.wikipedia.org

### Images
Wie Links, aber mit einem Ausrufezeichen (!) davor.
![Beschreibung des Bildes](https://via.placeholder.com/150)

### Image + Link
Ein Bild, das man anklicken kann.
[![Bild-Beschreibung](https://via.placeholder.com/150)](https://target-url.com)

---

## 4. Code & Technical Content
Wichtig für meine Programmier-Notizen.

### Inline Code
Für einzelne Befehle im Satz nutze ich Backticks (`).
Nutze den Befehl `git status` oft.

### Fenced Code Blocks
Für ganze Skripte nutze ich drei Backticks. Mit dem Sprachkürzel gibt es Syntax-Highlighting.
```python
def hallo():
    print("Hallo Welt")

## 5. Quotes & Notes
Zitate eignen sich super für Hinweise.

### Blockquotes
> Das ist ein Zitat.
>
> > Das ist ein verschachteltes Zitat.
>
> Hier geht es weiter mit **Formatierung**.

---

## 6. Tables
Tabellen sehen im Code etwas wild aus, werden aber schön gerendert.
Die Doppelpunkte bestimmen die Ausrichtung (links, mittig, rechts).

| Linksbündig | Zentriert | Rechtsbündig |
| :--- | :---: | ---: |
| Text A | Text B | Text C |
| 1 | 2 | 3 |

---

## 7. Task Lists
Meine To-Dos direkt im Dokument.

- [x] Tutorial abgeschlossen
- [ ] Cheat Sheet schreiben
- [ ] Pause machen

---

## 8. Dividers & Layout
Um Abschnitte visuell zu trennen.

Text oben
***
Text unten (getrennt durch horizontale Linie)

---

## 9. Online Editors
Diese Tools habe ich gefunden, um Markdown zu schreiben:
* **HackMD:** Gut für Zusammenarbeit.
* **Obsidian:** Toll für vernetzte Notizen.
* **VS Code:** Mein Editor für die Uni.

---

## 10. GitHub Specifics
Spezielle Funktionen, die nur auf GitHub funktionieren:

* **Task Lists:** Anklickbar in Issues/PRs.
* **Mentions:** `@username` benachrichtigt Leute.
* **Issues verlinken:** `#1` verlinkt automatisch auf Issue Nr 1
* **Emojis:** `:tada:` wird zu 🎉, `:rocket:` wird zu 🚀.