# Search

## 01. Problemformalisierung, Zustandsraum

### 1. Problemformalisierung

- **Zustände**: Die Positionen der Elben und Orks auf beiden Seiten des Flussufers sowie die Position des Pferdes (links oder rechts).
- **Aktionen**: Mit einem Elben und/oder Ork mit dem Pferd über den Fluss zu fahren.
- **Startzustand**: Drei Elben und drei Orks sind auf der linken Seite des Flusses.
- **Endzustand**: Drei Elben und drei Orks sind auf der rechten Seite des Flusses.

### 2. Problemgraph

![Problemgraph](problemgraph.png)

## 02. Suchverfahren

### 1. Tiefensuche, Breitensuche, A*

- **Tiefensuche**: Frankfurt -> Mannheim -> Karlsruhe -> Augsburg -> München | Frankfurt -> Würzburg -> Erfurt | Würzburg -> Nürnberg -> München
**Würzburg -> Nürnberg -> München**
- **Breitensuche**: Frankfurt -> (Mannheim -> Würzburg -> Kassel) -> ((Kalsruhe) -> (Erfurt -> Nürnberg) -> (München))
**Würzburg -> Frankfurt -> Kassel -> München**
- **A\***: Würzburg -> Frankfurt -> Mannheim -> Karlsruhe -> Augsburg -> München
**Würzburg -> Frankfurt -> Mannheim -> Karlsruhe -> Augsburg -> München**

| Algorithmus  | Maximale Einträge in der Datenstruktur | Durchläufe der Hauptschleife |
| ------------ | -------------------------------------- | ---------------------------- |
| Tiefensuche  | 5                                      | 10                           |
| Breitensuche | 4                                      | 10                           |
| A\*          | 5                                      | 6                            |

### 2. Restkostenabschätzung A*

Restkostenabschätzungen sind in A\* nur zulässig, wenn sie nie größer als die tatsächlichen minimalen Kosten sind. Sind sie zu hoch, kann A* keine optimale Lösung garantieren.

**Korrektur:**  
Die Abschätzungen müssen stets kleiner oder gleich den echten Restkosten sein, z.B. durch die Anzahl der verbleibenden Schritte.

**A\* mit korrigierten Abschätzungen:**  
Würzburg (3) → Nürnberg (2) → Augsburg (1) → München (0).  
A* findet so den optimalen Pfad.

## 03. Dominanz

**Definition:**  
Eine Heuristik $h_1(n)$ dominiert eine Heuristik $h_2(n)$, wenn für jeden Knoten $n$ gilt: $h_1(n) \geq h_2(n)$ und beide Heuristiken zulässig sind.

**Auswirkung in A\*:**  
Die Verwendung einer dominierenden Heuristik $h_1(n)$ in A\* führt dazu, dass weniger Knoten betrachtet werden müssen als bei einer von $h_1$ dominierten Heuristik $h_2(n)$. Das bedeutet, A* arbeitet effizienter und findet den optimalen Pfad mit weniger Aufwand.

**Beispiel:**  

- $h_1(n)$: Luftlinienentfernung zum Ziel.
- $h_2(n)$: Anzahl der noch zu besuchenden Städte.

Da die Luftlinienentfernung meist größer oder gleich der Anzahl der noch zu besuchenden Städte ist, dominiert $h_1$ die Heuristik $h_2$.

## 04. Beweis der Optimalität von A*

**Beweis:**  
A\* wählt stets den Knoten mit minimalen $f(n) = g(n) + h(n)$. Ist $h(n)$ zulässig ($h(n) \leq h^*(n)$), kann A* keinen günstigeren Pfad übersehen: Der erste erreichte Zielknoten hat garantiert minimale Kosten.
