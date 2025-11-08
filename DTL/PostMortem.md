# Post Mortem EA

## 1. Was wurde gemacht

Zuerst wurde auf eine angegebene Datentabelle CAL3 und ID3 angewendet, um einen Entscheidungsbaum zu erstellen. Dabei wurden die Entropie und der Informationsgewinn für verschiedene Attribute berechnet, um die beste Aufteilung der Daten zu bestimmen. Anschließend wurde der Entscheidungsbaum konstruiert, indem die Attribute mit dem höchsten Informationsgewinn ausgewählt und die Daten entsprechend aufgeteilt wurden. Danach wurde ein gegebener Baum verkleinert und zuletzt wurde mit Weka Entscheidungsbäume erstellt.

## 2. Interessante Aufgaben

Interessant war es, das aus CAL3 und ID3 resultierende unterschiedliche Verhalten bei der Baumkonstruktion zu beobachten. Es war spannend zu sehen, wie die Wahl des Attributs mit dem höchsten Informationsgewinn den Aufbau des Baumes beeinflusst und wie dies zu unterschiedlichen Strukturen führen kann.

## 3. Schwierigkeiten

Schwierig war es, erstamal die Algorithmen zu verstehen und die Berechnungen für Entropie und Informationsgewinn korrekt durchzuführen. Besonders herausfordernd war es, die verschiedenen Schritte der Baumkonstruktion nachzuvollziehen und sicherzustellen, dass die richtigen Attribute ausgewählt wurden.

## 4. Fazit

Ich fande die Übung sehr anspruchsvoll, da man bei der Handsimulation der Algorithmen sehr genau arbeiten musste, um keine Fehler zu machen, da sonst der gesamte Baum falsch aufgebaut werden konnte.

## 5. GitHub Repository

[GitHub Repository](https://github.com/Hicks-99/Grundlagen-der-KI/tree/main/DTL)
