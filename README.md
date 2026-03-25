# 🔍 Banner Grabber & Port Scanner

Ein schneller, minimalistischer Portscanner mit optionalem Banner‑Grabbing.
Ideal, um offene Ports zu identifizieren und erste Fingerprints von Diensten zu sammeln.

## 🚀 Features

Erkennt offene TCP‑Ports

Optionales Banner‑Grabbing (-b)

Unterstützt flexible Port‑Angaben:

    Einzelne Ports → -p 22

    Mehrere Ports → -p 22,80,443

Automatischer Full‑Scan (1–65535), wenn -p nicht angegeben wird

Sauberes Fehler‑Handling

Strg+C bricht den Scan sauber ab

## 📦 Installation

    git clone https://github.com/<dein-user>/banner_graber.git
    cd banner_graber
    python3 addmain.py -H <target>

# 🧪 Usage Examples
## 🔎 Alle Ports scannen
bash

python3 addmain.py -H 192.168.1.10

## 🎯 Bestimmte Ports scannen
bash

python3 addmain.py -H 192.168.1.10 -p 22,80,443

## 🏷️ Banner‑Grabbing aktivieren
bash

python3 addmain.py -H 192.168.1.10 -b

## ⚠️ Einschränkungen

Manche Dienste senden kein Banner, bevor der Client spricht (z. B. HTTP ohne Request)

Banner‑Grabbing ist aktuell generisch, nicht service‑spezifisch

## 🛠️ Roadmap

Erweiterte Banner‑Erkennung (HTTP, FTP, SMTP, etc.)

Service‑Fingerprinting

Fortschrittsanzeige

Thread‑Pool für bessere Performance

UDP‑Scan

Ausgabe im Nmap‑Stil

Automatische CVE‑Erkennung basierend auf Banner‑Versionen

## 🔒 CVE‑Support (in Arbeit)

Geplant ist eine Funktion, die erkannte Banner automatisch mit bekannten CVE‑Datenbanken abgleicht, um potenziell verwundbare Versionen zu identifizieren.


    
