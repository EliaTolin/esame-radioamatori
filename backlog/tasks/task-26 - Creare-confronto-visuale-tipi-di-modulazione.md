---
id: task-26
title: Creare confronto visuale tipi di modulazione
status: Done
assignee:
  - '@claude'
created_date: '2025-12-07 16:23'
updated_date: '2025-12-07 18:11'
labels:
  - diagrams
  - chapter1
  - matplotlib
dependencies: []
priority: medium
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Creare diagrammi comparativi per AM, FM, SSB e modi digitali mostrando forma d'onda, spettro, larghezza di banda e rapporto segnale/rumore.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Creare script plot_modulation_comparison.py
- [x] #2 Generare confronto forma d'onda AM vs FM vs SSB
- [x] #3 Generare confronto spettro (bandwidth) per tipo modulazione
- [x] #4 Creare tabella visuale efficienza spettrale
- [x] #5 Generare diagramma costellazione per modi digitali (PSK, QAM)
- [x] #6 Integrare in 01_*/1.8_Segnali_modulati.md
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Creato script plot_modulation_comparison.py con 5 visualizzazioni:
- confronto_forme_onda_modulazione.png: AM vs FM vs SSB nel tempo
- confronto_spettri_modulazione.png: Spettri e larghezze di banda
- efficienza_spettrale_modulazione.png: Tabella efficienza per tipo
- diagrammi_costellazione.png: BPSK, QPSK, 8-PSK, 16-QAM, 64-QAM
- panoramica_modulazioni.png: Tabella completa con designatori ITU

Integrate in 1.8_Segnali_modulati.md
<!-- SECTION:NOTES:END -->
