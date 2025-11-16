# Post Mortem CSP

## 1. Was wurde gemacht

Es wurde das Einstein-Rätsel als Constraint Satisfaction Problem (CSP) implementiert und gelöst. Dabei wurden verschiedene Lösungsalgorithmen implementiert und verglichen. Der BT_Search (Backtracking) diente als Basis-Algorithmus zum Lösen des CSP. Zur Optimierung wurden die MRV- und Grad-Heuristik als Variablenauswahlstrategien zur Reduktion des Suchraums integriert. Die AC-3 Kantenkonsistenz wurde als Vorverarbeitung zur Domänenreduktion vor der Suche angewendet. Weiterhin wurde MAC (Maintaining Arc Consistency) implementiert, welche die Kantenkonsistenz während der Backtracking-Suche aufrechterhält. Zusätzlich kam die Min-Conflicts Heuristik als lokale Suchmethode zur Problemlösung zum Einsatz. Die Implementation umfasste die Modellierung des Rätsel-Problems mit Variablen, Wertebereichen und Constraints, sowie empirische Vergleiche der Algorithmen bezüglich Laufzeit und Sucheffizienz.

## 2. Interessante Aufgaben

Besonders interessant war die Implementierung und Integration der AC-3 Kantenkonsistenz und MAC in den Backtracking-Algorithmus. Diese Techniken zur Domänenreduktion und Konsistenzsicherung sind entscheidend, um die Effizienz bei der Lösung von CSPs zu verbessern. Es war spannend zu beobachten, wie sich die Anwendung dieser Methoden auf die Anzahl der Backtracking-Schritte und die Gesamtlaufzeit auswirkte. Zudem bot die Modellierung des Einstein-Rätsels als CSP eine herausfordernde Aufgabe, da es eine Vielzahl von Variablen und komplexen Constraints beinhaltete, die sorgfältig definiert und implementiert werden mussten.

## 3. Schwierigkeiten

Die größte Herausforderung bestand darin, die verschiedenen Algorithmen korrekt zu implementieren und sicherzustellen, dass sie nahtlos zusammenarbeiten. Insbesondere die Integration von AC-3 und MAC in den Backtracking-Prozess erforderte ein tiefes Verständnis der zugrunde liegenden Prinzipien der Kantenkonsistenz und deren Auswirkungen auf die Domänen der Variablen. Zudem war die Modellierung des Einstein-Rätsels komplex, da viele Variablen und Constraints berücksichtigt werden mussten, was zu einer erhöhten Komplexität bei der Implementierung führte. Fehler in der Definition der Constraints oder der Domänen konnten leicht zu falschen Ergebnissen führen, weshalb eine sorgfältige Validierung und Tests notwendig waren.

## 4. Fazit

Es war schön zu sehen, wie die verschiedenen Algorithmen zusammenarbeiten konnten, um das CSP effizient zu lösen. Die Anwendung von Kantenkonsistenz und die Nutzung heuristischer Methoden zeigten deutlich, wie wichtig diese Techniken für die Leistungssteigerung bei der Lösung komplexer Probleme sind.
Jedoch fande ich die Implementierung und das Verständnis der Algorithmen sehr herausfordernd.

## 5. GitHub Repository

[GitHub Repository](https://github.com/Hicks-99/Grundlagen-der-KI/tree/main/CSP)
