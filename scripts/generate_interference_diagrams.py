#!/usr/bin/env python3
"""
Generazione schemi soppressione disturbi EMI/RFI.
Filtri di linea, ferrite, disaccoppiamento, schermatura.
"""

import schemdraw
import schemdraw.elements as elm
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
import numpy as np
from pathlib import Path

# Directory di output
OUTPUT_DIR = Path(__file__).parent.parent / "images" / "09_disturbi"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def schema_filtro_linea_ac():
    """Schema filtro EMI per linea AC (filtro di rete)."""
    d = schemdraw.Drawing(unit=2.5)

    # Ingresso AC
    d += elm.Dot().at((0, 2)).label('L\n(Fase)', loc='left', fontsize=9)
    d += elm.Dot().at((0, 0)).label('N\n(Neutro)', loc='left', fontsize=9)

    # Linea superiore
    d += elm.Line().right().length(0.5).at((0, 2))

    # Condensatore X (tra L e N) - ingresso
    d.push()
    d += elm.Capacitor().down().label('Cx\n100nF', loc='right', fontsize=8)
    d.pop()

    # Induttore di modo comune (trasformatore bifilar)
    d += elm.Inductor().right().label('L1', loc='top', fontsize=9)

    # Condensatori Y (verso terra)
    d.push()
    d += elm.Line().down().length(0.3)
    d += elm.Capacitor().down().label('Cy\n2.2nF', loc='right', fontsize=8).length(0.7)
    d += elm.Ground()
    d.pop()

    d += elm.Line().right().length(0.5)

    # Secondo condensatore X
    d.push()
    d += elm.Capacitor().down().label('Cx\n100nF', loc='right', fontsize=8)
    d.pop()

    # Uscita
    d += elm.Line().right().length(0.5)
    d += elm.Dot().label('L', loc='right', fontsize=9)

    # Linea inferiore (Neutro)
    d += elm.Line().right().length(0.5).at((0, 0))
    d += elm.Inductor().right().label('L2', loc='bottom', fontsize=9)
    d += elm.Line().down().length(0.3).at((3.5, 0))
    d += elm.Capacitor().down().label('Cy\n2.2nF', loc='right', fontsize=8).length(0.7)
    d += elm.Ground()

    d += elm.Line().right().length(1.5).at((4, 0))
    d += elm.Dot().label('N', loc='right', fontsize=9)

    # Terra
    d += elm.Line().right().length(2.75).at((0, -1.5))
    d += elm.Dot().label('PE\n(Terra)', loc='left', fontsize=9).at((0, -1.5))
    d += elm.Line().right().length(3).at((2.75, -1.5))
    d += elm.Dot().label('PE', loc='right', fontsize=9)

    d.save(OUTPUT_DIR / 'filtro_linea_ac.svg')
    print(f"✓ Salvato: {OUTPUT_DIR / 'filtro_linea_ac.svg'}")


def schema_ferrite_cavo():
    """Schema applicazione ferrite su cavi."""
    fig, ax = plt.subplots(figsize=(12, 6))

    # Cavo
    ax.plot([1, 11], [3, 3], 'b-', linewidth=8, solid_capstyle='round')
    ax.text(6, 2.2, 'Cavo coassiale / USB / alimentazione', ha='center', fontsize=10)

    # Ferrite clip-on
    ferrite1 = FancyBboxPatch((3, 2.3), 1.5, 1.4, boxstyle="round,pad=0.05",
                               facecolor='gray', edgecolor='black', linewidth=2)
    ax.add_patch(ferrite1)
    ax.text(3.75, 3, 'Ferrite\nClip-on', ha='center', va='center', fontsize=9,
            fontweight='bold', color='white')

    # Ferrite toroidale (multiple turns)
    ferrite2 = mpatches.Circle((7.5, 3), 0.8, facecolor='dimgray', edgecolor='black', linewidth=2)
    ax.add_patch(ferrite2)
    ax.plot([6.5, 7, 7.5, 8, 8.5], [3.3, 3.6, 3.3, 3.6, 3.3], 'b-', linewidth=4)
    ax.text(7.5, 1.8, 'Toroide\n(più spire)', ha='center', fontsize=9)

    # Annotazioni impedenza
    ax.annotate('Z = jωL', xy=(3.75, 4), fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightyellow'))
    ax.text(3.75, 4.8, 'Impedenza aumenta\ncon frequenza', ha='center', fontsize=9, style='italic')

    # Frecce corrente di modo comune
    ax.annotate('', xy=(2.5, 3.8), xytext=(1.5, 3.8),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(2, 4.2, 'I_cm\n(disturbo)', ha='center', fontsize=8, color='red')

    ax.annotate('', xy=(10, 3.8), xytext=(9, 3.8),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(9.5, 4.2, 'I_cm\nattenuata', ha='center', fontsize=8, color='green')

    # Legenda applicazioni
    apps = ['• Cavi USB: elimina RFI da PC',
            '• Cavi alimentazione: blocca RF',
            '• Cavi antenna: modo comune']
    ax.text(1, 0.8, '\n'.join(apps), fontsize=9, va='top',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5.5)
    ax.set_title('Applicazione Ferrite per Soppressione Disturbi di Modo Comune',
                 fontsize=12, fontweight='bold')
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'ferrite_cavo.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'ferrite_cavo.png'}")


def schema_disaccoppiamento():
    """Schema circuito disaccoppiamento alimentazione IC."""
    d = schemdraw.Drawing(unit=2.5)

    # Alimentazione principale
    d += elm.Dot().at((0, 3)).label('+Vcc\n(5V/12V)', loc='left', fontsize=9)
    d += elm.Line().right().length(1)

    # Condensatore elettrolitico bulk
    d.push()
    d += elm.Capacitor().down().label('C1\n100μF\nElettrol.', loc='right', fontsize=8)
    d += elm.Ground()
    d.pop()

    # Ferrite bead
    d += elm.Inductor().right().label('FB\nFerrite', loc='top', fontsize=8)

    # Condensatori ceramici vicino IC
    d.push()
    d += elm.Capacitor().down().label('C2\n100nF\nCeram.', loc='right', fontsize=8)
    d += elm.Ground()
    d.pop()

    d += elm.Line().right().length(0.5)

    d.push()
    d += elm.Capacitor().down().label('C3\n10nF\nCeram.', loc='right', fontsize=8)
    d += elm.Ground()
    d.pop()

    # IC
    d += elm.Line().right().length(0.5)
    d += elm.Ic(pins=[elm.IcPin('Vcc', side='left'),
                      elm.IcPin('GND', side='left'),
                      elm.IcPin('OUT', side='right')]).anchor('inL1').label('IC', loc='center', fontsize=10)

    d.save(OUTPUT_DIR / 'disaccoppiamento_ic.svg')
    print(f"✓ Salvato: {OUTPUT_DIR / 'disaccoppiamento_ic.svg'}")


def schema_filtro_armoniche_tx():
    """Schema filtro passa-basso per armoniche TX."""
    d = schemdraw.Drawing(unit=2.5)

    # Ingresso da TX
    d += elm.Dot().at((0, 2)).label('TX\nOutput', loc='left', fontsize=9)
    d += elm.Line().right().length(0.5)

    # Filtro π passa-basso
    # C1 parallelo
    d.push()
    d += elm.Capacitor().down().label('C1', loc='right', fontsize=9)
    d += elm.Ground()
    d.pop()

    # L1 serie
    d += elm.Inductor().right().label('L1', loc='top', fontsize=9)

    # C2 parallelo
    d.push()
    d += elm.Capacitor().down().label('C2', loc='right', fontsize=9)
    d += elm.Ground()
    d.pop()

    # L2 serie
    d += elm.Inductor().right().label('L2', loc='top', fontsize=9)

    # C3 parallelo
    d.push()
    d += elm.Capacitor().down().label('C3', loc='right', fontsize=9)
    d += elm.Ground()
    d.pop()

    # Uscita antenna
    d += elm.Line().right().length(0.5)
    d += elm.Dot().label('Antenna\n50Ω', loc='right', fontsize=9)

    # Etichetta
    d += elm.Label().at((3, 3.5)).label('Filtro π 5 poli - Passa-basso', fontsize=11)

    d.save(OUTPUT_DIR / 'filtro_armoniche_tx.svg')
    print(f"✓ Salvato: {OUTPUT_DIR / 'filtro_armoniche_tx.svg'}")


def diagramma_schermatura_emi():
    """Diagramma concettuale schermatura EMI."""
    fig, ax = plt.subplots(figsize=(14, 8))

    # Sorgente EMI esterna
    for i in range(5):
        ax.annotate('', xy=(3, 4 + i * 0.8 - 1.6), xytext=(0.5, 4 + i * 0.8 - 1.6),
                    arrowprops=dict(arrowstyle='->', color='red', lw=1.5,
                                    connectionstyle='arc3,rad=0.1'))
    ax.text(0.5, 5.5, 'Campo EM\nesterno\n(disturbo)', ha='center', fontsize=10, color='red')

    # Schermo metallico
    schermo = Rectangle((3, 1), 0.3, 6, facecolor='silver', edgecolor='black', linewidth=3)
    ax.add_patch(schermo)
    ax.text(3.15, 7.3, 'SCHERMO\nMETALLICO', ha='center', fontsize=10, fontweight='bold')

    # Area protetta
    area_prot = Rectangle((3.5, 1.5), 5, 5, facecolor='lightgreen', edgecolor='green',
                           linewidth=2, alpha=0.3)
    ax.add_patch(area_prot)
    ax.text(6, 4, 'AREA\nPROTETTA', ha='center', va='center', fontsize=14,
            fontweight='bold', color='darkgreen')

    # Circuito interno
    circ = FancyBboxPatch((5, 3), 2, 2, boxstyle="round,pad=0.1",
                          facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax.add_patch(circ)
    ax.text(6, 4, 'Circuito\nSensibile', ha='center', va='center', fontsize=10)

    # Riflessione
    for i in range(3):
        ax.annotate('', xy=(1.5, 3.5 + i * 0.8), xytext=(2.8, 3.5 + i * 0.8),
                    arrowprops=dict(arrowstyle='<-', color='orange', lw=1.5,
                                    connectionstyle='arc3,rad=-0.2'))
    ax.text(1.5, 2, 'Riflesso\n~80%', ha='center', fontsize=9, color='orange')

    # Assorbimento (dentro lo schermo)
    ax.text(3.15, 0.5, 'Assorbito\n~15%', ha='center', fontsize=9, color='gray')

    # Campo residuo (molto attenuato)
    ax.annotate('', xy=(4.5, 4), xytext=(3.5, 4),
                arrowprops=dict(arrowstyle='->', color='pink', lw=1, alpha=0.5))
    ax.text(4, 4.5, '~5%\nresiduo', ha='center', fontsize=8, color='gray')

    # Messa a terra
    ax.plot([3.15, 3.15], [1, 0.3], 'k-', linewidth=2)
    ax.plot([2.9, 3.4], [0.3, 0.3], 'k-', linewidth=2)
    ax.plot([3, 3.3], [0.1, 0.1], 'k-', linewidth=2)
    ax.plot([3.1, 3.2], [-0.1, -0.1], 'k-', linewidth=2)
    ax.text(3.7, 0, 'Terra', fontsize=9)

    # Formula attenuazione
    ax.text(10, 6.5, 'Attenuazione schermo:\n\nSE = R + A + B  (dB)\n\nR = riflessione\nA = assorbimento\nB = multi-riflessione',
            fontsize=10, va='top', family='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow'))

    # Materiali tipici
    ax.text(10, 2.5, 'Materiali tipici:\n• Rame: 60-100 dB\n• Alluminio: 50-80 dB\n• Acciaio: 40-60 dB\n• Mu-metal: campo H',
            fontsize=9, va='top',
            bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.8))

    ax.set_xlim(-0.5, 13)
    ax.set_ylim(-0.5, 8)
    ax.set_title('Principi della Schermatura EMI', fontsize=14, fontweight='bold')
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'schermatura_emi.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'schermatura_emi.png'}")


def schema_filtro_rete_completo():
    """Schema filtro di rete EMI completo con annotazioni."""
    fig, ax = plt.subplots(figsize=(14, 8))

    # Box filtro
    filtro = Rectangle((2, 2), 8, 4, facecolor='lightyellow', edgecolor='black', linewidth=2)
    ax.add_patch(filtro)
    ax.text(6, 6.3, 'FILTRO EMI DI RETE', ha='center', fontsize=12, fontweight='bold')

    # Componenti interni (stilizzati)
    # Induttori di modo comune
    ax.add_patch(mpatches.Circle((4, 4), 0.5, facecolor='brown', edgecolor='black'))
    ax.text(4, 4, 'L', ha='center', va='center', fontsize=10, color='white', fontweight='bold')
    ax.text(4, 3.2, 'Induttore\nmodo comune', ha='center', fontsize=8)

    # Condensatori X
    ax.add_patch(Rectangle((5.5, 3.5), 0.3, 1, facecolor='blue', edgecolor='black'))
    ax.text(5.65, 4, 'Cx', ha='center', va='center', fontsize=8, color='white')
    ax.text(5.65, 3.2, 'Cond. X\n(L-N)', ha='center', fontsize=8)

    # Condensatori Y
    ax.add_patch(Rectangle((7.5, 3.5), 0.3, 1, facecolor='green', edgecolor='black'))
    ax.text(7.65, 4, 'Cy', ha='center', va='center', fontsize=8, color='white')
    ax.text(7.65, 3.2, 'Cond. Y\n(L/N-PE)', ha='center', fontsize=8)

    # Ingresso
    ax.annotate('', xy=(2, 5), xytext=(0.5, 5),
                arrowprops=dict(arrowstyle='->', lw=2))
    ax.annotate('', xy=(2, 3), xytext=(0.5, 3),
                arrowprops=dict(arrowstyle='->', lw=2))
    ax.text(0.3, 5.3, 'L (Fase)', fontsize=9)
    ax.text(0.3, 2.7, 'N (Neutro)', fontsize=9)
    ax.text(1.2, 4, '230V AC\n+ disturbi', ha='center', fontsize=9, color='red')

    # Uscita
    ax.annotate('', xy=(11.5, 5), xytext=(10, 5),
                arrowprops=dict(arrowstyle='->', lw=2))
    ax.annotate('', xy=(11.5, 3), xytext=(10, 3),
                arrowprops=dict(arrowstyle='->', lw=2))
    ax.text(11.7, 5.3, 'L', fontsize=9)
    ax.text(11.7, 2.7, 'N', fontsize=9)
    ax.text(10.8, 4, '230V AC\nfiltrata', ha='center', fontsize=9, color='green')

    # Terra
    ax.plot([6, 6], [2, 1], 'g-', linewidth=2)
    ax.text(6, 0.7, 'PE (Terra)', ha='center', fontsize=9, color='green')

    # Caratteristiche
    specs = ['Specifiche tipiche:',
             '• Attenuazione: 40-60 dB',
             '• Frequenza: 150 kHz - 30 MHz',
             '• Corrente max: 1-16 A',
             '• Tensione: 250V AC']
    ax.text(0.5, 1.5, '\n'.join(specs), fontsize=9, va='top',
            bbox=dict(boxstyle='round', facecolor='lightblue'))

    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7)
    ax.set_title('Filtro EMI di Rete - Vista Funzionale', fontsize=14, fontweight='bold')
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'filtro_rete_funzionale.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'filtro_rete_funzionale.png'}")


def main():
    """Genera tutti i diagrammi soppressione disturbi."""
    print("Generazione schemi soppressione disturbi EMI/RFI...")
    print(f"Directory output: {OUTPUT_DIR}\n")

    schema_filtro_linea_ac()
    schema_ferrite_cavo()
    schema_disaccoppiamento()
    schema_filtro_armoniche_tx()
    diagramma_schermatura_emi()
    schema_filtro_rete_completo()

    print("\n✅ Tutti gli schemi sono stati generati con successo!")


if __name__ == "__main__":
    main()
