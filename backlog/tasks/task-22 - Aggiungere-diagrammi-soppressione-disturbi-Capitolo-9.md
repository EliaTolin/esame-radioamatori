---
id: task-22
title: Aggiungere diagrammi soppressione disturbi - Capitolo 9
status: Done
assignee:
  - '@claude'
created_date: '2025-12-07 16:19'
updated_date: '2025-12-07 17:07'
labels:
  - diagrams
  - chapter9
  - schemdraw
dependencies: []
priority: medium
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Creare schemi circuitali per i filtri e le tecniche di soppressione dei disturbi EMI/RFI: filtri di linea, ferrite, schermature e circuiti di disaccoppiamento.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Creare script generate_interference_diagrams.py
- [x] #2 Generare schema filtro di linea AC
- [x] #3 Generare schema applicazione ferrite su cavi
- [x] #4 Generare schema circuito disaccoppiamento alimentazione
- [x] #5 Generare schema filtro passa-basso per armoniche TX
- [x] #6 Generare diagramma concettuale schermatura EMI
- [x] #7 Integrare diagrammi in 09_Disturbi_Protezione/
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Implementato script generate_interference_diagrams.py che genera 6 diagrammi:
- filtro_linea_ac.svg: schema filtro EMI con Cx, Cy, induttori
- filtro_rete_funzionale.png: vista funzionale con specifiche
- ferrite_cavo.png: applicazione ferrite clip-on e toroide
- disaccoppiamento_ic.svg: condensatori + ferrite bead
- filtro_armoniche_tx.svg: filtro π passa-basso 5 poli
- schermatura_emi.png: principi riflessione/assorbimento

Integrati in 9.3_Protezione_contro_i_disturbi.md.
<!-- SECTION:NOTES:END -->
