---
id: task-19
title: Visualizzare propagazione ionosferica - Capitolo 7
status: Done
assignee:
  - '@claude'
created_date: '2025-12-07 16:18'
updated_date: '2025-12-07 16:50'
labels:
  - diagrams
  - chapter7
  - matplotlib
dependencies: []
priority: high
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Creare diagrammi per illustrare la propagazione delle onde radio nell'atmosfera: strati ionosferici, zone di skip, frequenza massima utilizzabile (MUF) e angoli critici.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Creare script plot_ionosphere.py
- [x] #2 Generare diagramma strati ionosferici (D, E, F1, F2) con altitudini
- [x] #3 Generare visualizzazione zona di skip e onda di terra/cielo
- [x] #4 Creare grafico MUF vs ora del giorno
- [x] #5 Generare diagramma angolo critico e rifrazione ionosferica
- [x] #6 Integrare visualizzazioni in 07_Propagazione/1_Propagazione.md
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Implementato script plot_ionosphere.py che genera 5 diagrammi PNG:
- strati_ionosferici.png: sezione atmosfera con D/E/F1/F2
- zona_skip.png: onda terra vs onda spaziale
- muf_giornaliero.png: variazione MUF 24h estate/inverno
- angolo_critico.png: rifrazione ionosferica
- propagazione_multihop.png: DX con salti multipli

Integrati in 7_Propagazione.md sostituendo i diagrammi Mermaid.
<!-- SECTION:NOTES:END -->
