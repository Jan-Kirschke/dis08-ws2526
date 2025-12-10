## 1. Beschriebenes Dataset: Global Power Plant Database

### Titel & Quelle
* **Titel:** Global Power Plant Database (GPPD)
* **Quelle:** **WRI (World Resources Institute)**, Open Power Plant Data. Gefunden auf [Github](https://github.com/wri/global-power-plant-database/blob/master/output_database/global_power_plant_database.csv)

### Format, Größe & Statistik
| Merkmal | Details |
| :--- | :--- |
| **Format** | CSV |
| **Größe** | 34.936 Zeilen, 36 Spalten (ca. 11.6 MB) |
| **Mittelwert Kapazität** | 163.355 MW |
| **Median Kapazität** | 16.744 MW |
| **Max Kapazität** | 22500.00 MW (Dreischluchten-Staudamm, China) |
| **Häufigster Brennstoff** | Solar |

### Abdeckung & Lizenz
* **Geografisch:** **Global** (fokussiert auf entwickelte Länder).
* **Temporal:** Von ca. **1890 bis zur Gegenwart**.
* **Lizenz:** **Creative Commons Attribution 4.0 International (CC BY 4.0).** Offen und frei nutzbar unter korrekter **Namensnennung (Attribution)** des WRI.

---

## 2. Augmentierung des Datasets (Gekürzte Version)

### A. Potenzielle Erweiterung
* **Zweites Dataset:** **Weltbank-Indikatoren** zur Energiepolitik und Wirtschaftsentwicklung (z.B. BIP pro Kopf, CO2-Emissionen).
* **Externe Daten:** **Geografische Daten** wie Satellitenbilder (Sentinel/Landsat) oder Nachtlichter-Intensität (VIIRS DNB) zur Analyse der tatsächlichen Betriebsaktivität oder Urbanisierung am Standort.

### B. Verknüpfung und Forschungsfragen
* **Verknüpfung:** Über **Ländercodes** (mit Weltbank-Daten) und **Geokoordinaten** (`latitude`, `longitude`) für lokale Daten. 
* **Forschungsfragen:**
    * **Wirtschaft:** Korrelation zwischen **installierter Kapazität erneuerbarer Energien** und **BIP pro Kopf** eines Landes.
    * **Umwelt:** Zusammenhang zwischen nationalen **CO2-Grenzwerten** und der **Dominanz bestimmter Brennstoffarten** (Kohle vs. Gas).
    * **Geopolitik:** Vergleich der Kraftwerkstypen in Regionen mit **hoher vs. geringer Nachtlicht-Intensität** (Indikator für Entwicklung/Urbanisierung).

### C. Nächste Schritte zum Daten-Merge
1.  **Datenbereinigung:** Standardisierung der **Ländernamen/Codes** (GPPD und Weltbank) auf einen gemeinsamen Standard (z.B. ISO 3166-1 Alpha-3).
2.  **Filterung:** Weltbank-Daten auf das relevante **Zeitfenster/Jahr** des GPPD-Updates vorbereiten.
3.  **Merge-Operation:** Durchführung eines **Left Join** über den standardisierten Ländercode.
4.  **Validierung:** Stichprobenartige Überprüfung der gemergten Daten.

---

## 3. Review nach den FAIR-Prinzipien (Gekürzte Version)

| Kriterium | Frage | Bewertung | Begründung (Kürzer) |
| :--- | :--- | :--- | :--- |
| **F**indable | Leicht zu lokalisieren und ausreichende Metadaten? | **Sehr gut** | Über vertrauenswürdige Repositorien (WRI, GitHub) auffindbar; registriert mit DOI/URN und detaillierten Metadaten. |
| **A**ccessible | Ohne Barrieren herunterladbar? | **Gut** | Direkter Download (CSV) ohne Registrierung/Anmeldung möglich. |
| **I**nteroperable | Maschinenlesbar und standardisiert? | **Gut** | CSV ist universell; Geodaten nutzen **WGS84-Standard**. Ländercodes erfordern jedoch oft eine Bereinigung/Standardisierung. |
| **R**eusable | Klare Lizenz und ausreichende Dokumentation? | **Sehr gut** | Explizite **CC BY 4.0-Lizenz** und umfangreiches **Data Dictionary** für jede Spalte. |

> **Zusammenfassendes Fazit:** Die Global Power Plant Database erfüllt die FAIR-Prinzipien sehr gut. Der Datensatz ist ein hervorragendes Beispiel für eine offene Datenressource von hoher Qualität und Nutzbarkeit, was die Wiederverwendung stark vereinfacht.
```