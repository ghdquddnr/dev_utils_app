# Entwickler-Dienstprogramm-App (Dev Utils App)

Eine Python-GUI-Anwendung, die verschiedene nützliche Funktionen für Entwickler bietet. Mit einer modernen Benutzeroberfläche und praktischen Funktionen macht sie die Entwicklungsarbeit effizienter.

![Anwendungs-Screenshot](screenshot.png)

## Hauptfunktionen

### Textvergleich (Text Diff)
- Visuelle Anzeige der Unterschiede zwischen zwei Texten
- Präzise Hervorhebung von Unterschieden durch zeilenweisen Vergleich
- Intuitive Benutzeroberfläche für einfache Bedienung
- Reset-Taste zum schnellen Starten einer neuen Arbeit

### JSON-Viewer
- Visualisierung von JSON-Strings als Baumstruktur
- Funktionalität zum Ein-/Ausklappen von Knoten für einfache Navigation in komplexen Strukturen
- Beispieldaten für schnelles Testen bereitgestellt
- Automatische Themenanpassung je nach Hell-/Dunkelmodus

## Technologie-Stack

- **Frontend**: CustomTkinter (Python GUI-Bibliothek)
- **Vergleichsalgorithmus**: diff-match-patch-Bibliothek
- **JSON-Parsing**: Python-integriertes json-Modul
- **Themensystem**: Unterstützung für Hell-/Dunkelmodus

## Systemanforderungen

- Python 3.8 oder höher
- Die folgenden Python-Pakete:
  - customtkinter
  - pillow
  - diff-match-patch

## Installation

### 1. Repository klonen
```bash
git clone https://github.com/ghdquddnr/dev_utils_app.git
cd dev_utils_app
```

### 2. Virtuelle Umgebung einrichten und Pakete installieren
```bash
# Virtuelle Umgebung erstellen
python -m venv venv

# Virtuelle Umgebung aktivieren
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Pakete installieren
pip install customtkinter pillow diff-match-patch
```

### 3. Anwendung ausführen
```bash
python main.py
```

## Bedienungsanleitung

### Textvergleichsfunktion
1. Geben Sie den Originaltext in den linken Textbereich ein.
2. Geben Sie den zu vergleichenden Text in den rechten Textbereich ein.
3. Klicken Sie auf die Schaltfläche "Vergleichen", um die Unterschiede zwischen den beiden Texten farblich hervorgehoben zu sehen.
   - Gelöschte Teile: Roter Hintergrund
   - Hinzugefügte Teile: Grüner Hintergrund
4. Klicken Sie auf die Schaltfläche "Zurücksetzen", um den gesamten Text zu löschen und einen neuen Vergleich zu starten.

### JSON-Viewer-Funktion
1. Geben Sie einen JSON-String in den linken Textbereich ein.
2. Klicken Sie auf die Schaltfläche "Konvertieren", um den JSON als Baumstruktur auf der rechten Seite zu visualisieren.
3. Klicken Sie auf die + oder - Schaltflächen auf den Baumknoten, um sie zu erweitern oder zu reduzieren.
4. Verwenden Sie die Schaltfläche "Alle erweitern"/"Alle reduzieren", um den gesamten Baum auf einmal zu steuern.
5. Klicken Sie auf die Schaltfläche "Beispieldaten", um automatisch JSON-Beispieldaten einzugeben.
6. Klicken Sie auf die Schaltfläche "Zurücksetzen", um alle Daten zu löschen.

### Themenwechsel
- Klicken Sie auf die Schaltfläche "Thema ändern" am unteren Rand der Seitenleiste, um zwischen Hell- und Dunkelmodus zu wechseln.

## Entwicklungsumgebung einrichten

```bash
# Entwicklungspakete installieren
pip install -e ".[dev]"
```

## Zukunftspläne

- Zusätzliche Dienstprogrammfunktionen in Entwicklung
- Leistungsoptimierung
- Funktionalität zum Speichern von Benutzereinstellungen

## Lizenz

Dieses Projekt wird unter der MIT-Lizenz vertrieben. Weitere Details finden Sie in der [LICENSE](LICENSE)-Datei.

## Mitwirkung

Beiträge sind immer willkommen! Sie können dazu beitragen, dieses Projekt durch Fehlerberichte, Funktionsanfragen oder Codebeiträge zu verbessern. 