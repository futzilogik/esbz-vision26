# ESBZ Chatbot – VISION26

Ein lokaler KI-Tutor-Chatbot für Schülerinnen und Schüler des VISION26-Kurses an der Evangelischen Schule Berlin Zentrum (ESBZ). Der Chatbot läuft vollständig lokal auf dem eigenen Rechner – ohne Cloud und ohne Internetzugang.

## Voraussetzungen

- [Ollama](https://ollama.com) – zum Ausführen des Sprachmodells lokal
- [uv](https://docs.astral.sh/uv/) – zur Verwaltung der Python-Umgebung
- Python 3.14 oder neuer

## Installation

### 1. Ollama installieren

```bash
brew install ollama
```

Anschließend das benötigte Sprachmodell laden:

```bash
ollama pull hf.co/bartowski/Llama-3-SauerkrautLM-8b-Instruct-GGUF
```

> Das Modell ist ca. 5 GB groß. Der Download kann je nach Verbindung einige Minuten dauern.

### 2. uv installieren

```bash
brew install uv
```

### 3. Abhängigkeiten installieren

Im Projektverzeichnis:

```bash
uv sync
```

Das erstellt automatisch eine virtuelle Umgebung unter `.venv/` und installiert alle Abhängigkeiten.

## Starten

```bash
uv run chatbot.py
```

Zum Beenden des Chats `exit` oder `quit` eingeben.

## Starten in VS Code

1. Das Projekt in VS Code öffnen
2. Im Menü **Ausführen → Debuggen starten** wählen oder `F5` drücken
3. Die Konfiguration **Chatbot** auswählen

Der Chatbot startet dann im integrierten Terminal.
