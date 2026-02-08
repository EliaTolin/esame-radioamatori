---
id: task-28
title: Semplificare diagrammi circuitali complessi
status: Done
assignee:
  - '@claude'
created_date: '2025-12-07 16:23'
updated_date: '2025-12-07 23:09'
labels:
  - diagrams
  - simplification
dependencies: []
priority: low
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Revisionare i diagrammi circuitali esistenti per semplificarli dove possibile, migliorare le etichette e aggiungere annotazioni didattiche.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Revisionare diagrammi PLL per chiarezza (semplificare blocchi)
- [x] #2 Aggiungere annotazioni flusso segnale ai diagrammi ricevitore/trasmettitore
- [x] #3 Uniformare stile etichette componenti (italiano)
- [x] #4 Aggiungere valori tipici ai componenti dove utile
- [x] #5 Verificare leggibilità a dimensioni ridotte (mobile-friendly)
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Riscritto completamente generate_pll_diagrams.py usando matplotlib:

- **Etichette italiane**: RIVELATORE di Fase (PD), FILTRO di Anello (LF), VCO (Osc. Controllato), DIVISORE (:N)
- **Annotazioni flusso segnale**: Errore fase, V_ctrl, f_out / N sui collegamenti
- **Formula boxes**: f_out = N × f_ref con esempio numerico
- **Valori tipici**: Intervalli frequenza VCO (100 MHz - 2 GHz), varactor (5-50 pF)
- **3 diagrammi generati**:
  - pll_schema_base.png - Schema PLL semplificato con legenda colori
  - pll_sintetizzatore.png - Sintetizzatore completo con frequenze tipiche
  - vco_dettaglio.png - Dettaglio VCO con varactor e formule
- **Stile moderno**: FancyBboxPatch con ombre, colori Tailwind CSS
<!-- SECTION:NOTES:END -->
