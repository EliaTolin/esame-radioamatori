#!/usr/bin/env python3
"""
Generazione diagrammi propagazione ionosferica.
Visualizza strati ionosferici, zona di skip, MUF e angolo critico.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Arc, FancyArrowPatch
import numpy as np
from pathlib import Path

# Directory di output
OUTPUT_DIR = Path(__file__).parent.parent / "images" / "07_propagazione"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Configurazione stile
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['figure.facecolor'] = 'white'


def plot_strati_ionosferici():
    """
    Diagramma a sezione degli strati ionosferici con altitudini.
    Mostra D, E, F1, F2 con colori e caratteristiche.
    """
    fig, ax = plt.subplots(figsize=(12, 8))

    # Definizione strati
    strati = [
        {'nome': 'Troposfera', 'h_min': 0, 'h_max': 12, 'color': '#87CEEB', 'alpha': 0.4},
        {'nome': 'Stratosfera', 'h_min': 12, 'h_max': 50, 'color': '#E0E0E0', 'alpha': 0.3},
        {'nome': 'Strato D', 'h_min': 60, 'h_max': 90, 'color': '#FFD700', 'alpha': 0.5},
        {'nome': 'Strato E', 'h_min': 90, 'h_max': 150, 'color': '#FFA500', 'alpha': 0.5},
        {'nome': 'Strato F1', 'h_min': 150, 'h_max': 250, 'color': '#FF6347', 'alpha': 0.5},
        {'nome': 'Strato F2', 'h_min': 250, 'h_max': 400, 'color': '#DC143C', 'alpha': 0.5},
    ]

    # Disegna strati
    for s in strati:
        rect = mpatches.Rectangle((0, s['h_min']), 10, s['h_max'] - s['h_min'],
                                   facecolor=s['color'], alpha=s['alpha'],
                                   edgecolor='black', linewidth=1)
        ax.add_patch(rect)

        # Etichetta strato
        y_mid = (s['h_min'] + s['h_max']) / 2
        ax.text(5, y_mid, s['nome'], ha='center', va='center',
                fontsize=12, fontweight='bold')

    # Terra
    terra = mpatches.Rectangle((0, -20), 10, 20, facecolor='#8B4513', alpha=0.7)
    ax.add_patch(terra)
    ax.text(5, -10, 'TERRA', ha='center', va='center', fontsize=12,
            fontweight='bold', color='white')

    # Annotazioni altitudini
    altezze = [0, 60, 90, 150, 250, 400]
    for h in altezze:
        ax.axhline(y=h, color='gray', linestyle='--', alpha=0.5, xmin=0.02, xmax=0.98)
        ax.text(10.2, h, f'{h} km', va='center', fontsize=10)

    # Annotazioni caratteristiche (lato destro)
    info = [
        (75, 'Assorbe onde corte\n(solo diurno)', '#FFD700'),
        (120, 'Riflessioni sporadiche Es\nVHF occasionale', '#FFA500'),
        (200, 'HF regolare\n(solo diurno)', '#FF6347'),
        (325, 'DX HF mondiale\n(giorno e notte)', '#DC143C'),
    ]

    for y, text, color in info:
        ax.annotate(text, xy=(10, y), xytext=(11.5, y),
                    fontsize=9, ha='left', va='center',
                    bbox=dict(boxstyle='round', facecolor=color, alpha=0.3),
                    arrowprops=dict(arrowstyle='->', color='gray'))

    # Sole
    sun = plt.Circle((9, 450), 15, color='yellow', ec='orange', linewidth=2)
    ax.add_patch(sun)
    ax.text(9, 450, '☀️', fontsize=20, ha='center', va='center')
    ax.annotate('Radiazione UV\nionizza gli strati', xy=(9, 435), xytext=(7, 420),
                fontsize=9, ha='center',
                arrowprops=dict(arrowstyle='->', color='orange'))

    # Configurazione
    ax.set_xlim(-0.5, 14)
    ax.set_ylim(-30, 480)
    ax.set_ylabel('Altitudine (km)', fontsize=12, fontweight='bold')
    ax.set_title('Strati Ionosferici e Loro Caratteristiche', fontsize=14, fontweight='bold', pad=15)
    ax.set_xticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'strati_ionosferici.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'strati_ionosferici.png'}")


def plot_zona_skip():
    """
    Visualizzazione zona di skip con onda di terra e onda spaziale.
    """
    fig, ax = plt.subplots(figsize=(14, 8))

    # Terra (arco)
    theta = np.linspace(-0.3, np.pi + 0.3, 100)
    r_terra = 50
    x_terra = r_terra * np.cos(theta) + 50
    y_terra = r_terra * np.sin(theta) - 45

    ax.fill_between(x_terra, y_terra, -10, color='#8B4513', alpha=0.6)
    ax.plot(x_terra, y_terra, 'brown', linewidth=2)

    # Ionosfera (arco superiore)
    r_iono = 70
    x_iono = r_iono * np.cos(theta) + 50
    y_iono = r_iono * np.sin(theta) - 45

    ax.fill_between(x_iono, y_iono, y_iono + 8, color='#FF6347', alpha=0.3)
    ax.plot(x_iono, y_iono, 'red', linewidth=2, linestyle='--')
    ax.text(50, 30, 'IONOSFERA (Strato F)', ha='center', fontsize=11, fontweight='bold', color='darkred')

    # Antenna trasmittente
    ax.plot([15, 15], [6, 12], 'k-', linewidth=3)
    ax.plot([13, 17], [12, 12], 'k-', linewidth=2)
    ax.text(15, 14, 'TX', ha='center', fontsize=10, fontweight='bold')

    # Onda di terra (verde)
    x_ground = np.linspace(15, 35, 50)
    y_ground = 5 + 2 * np.exp(-0.1 * (x_ground - 15))
    ax.plot(x_ground, y_ground, 'g-', linewidth=2.5, label='Onda di terra')
    ax.annotate('', xy=(35, 5.5), xytext=(25, 6),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))

    # Onda spaziale (blu) - salto ionosferico
    # Primo raggio verso ionosfera
    ax.annotate('', xy=(40, 22), xytext=(15, 10),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2,
                                connectionstyle='arc3,rad=-0.2'))

    # Riflessione e discesa
    ax.annotate('', xy=(70, 6), xytext=(40, 22),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2,
                                connectionstyle='arc3,rad=-0.2'))

    ax.plot([40, 40], [22, 24], 'r*', markersize=15)  # Punto riflessione

    # Zona di skip (area rossa tratteggiata)
    skip_x = [35, 70, 70, 35]
    skip_y = [5, 5, 8, 8]
    ax.fill(skip_x, skip_y, color='red', alpha=0.3, hatch='///')
    ax.text(52.5, 3, 'ZONA DI SKIP\n(nessun segnale)', ha='center', va='top',
            fontsize=10, fontweight='bold', color='darkred')

    # Zona ricezione onda di terra
    ax.annotate('Ricezione\nonda di terra', xy=(30, 5), xytext=(28, -2),
                fontsize=9, ha='center', color='green',
                arrowprops=dict(arrowstyle='->', color='green'))

    # Zona ricezione onda spaziale
    ax.annotate('Ricezione\nonda spaziale', xy=(72, 5), xytext=(78, -2),
                fontsize=9, ha='center', color='blue',
                arrowprops=dict(arrowstyle='->', color='blue'))

    # Antenna ricevente 1 (nella zona ground wave)
    ax.plot([30, 30], [5, 9], 'g-', linewidth=2)
    ax.text(30, 10, 'RX1', ha='center', fontsize=9, color='green')

    # Antenna ricevente 2 (nella skip zone - no signal)
    ax.plot([52, 52], [5, 9], 'r-', linewidth=2)
    ax.text(52, 10, 'X', ha='center', fontsize=12, fontweight='bold', color='red')

    # Antenna ricevente 3 (sky wave)
    ax.plot([72, 72], [5, 9], 'b-', linewidth=2)
    ax.text(72, 10, 'RX2', ha='center', fontsize=9, color='blue')

    # Distanze
    ax.annotate('', xy=(35, 1), xytext=(15, 1),
                arrowprops=dict(arrowstyle='<->', color='gray'))
    ax.text(25, -1, '~200 km', ha='center', fontsize=9, color='gray')

    ax.annotate('', xy=(70, 1), xytext=(35, 1),
                arrowprops=dict(arrowstyle='<->', color='gray'))
    ax.text(52.5, -1, 'Skip ~500-2000 km', ha='center', fontsize=9, color='gray')

    # Legenda
    ax.plot([], [], 'g-', linewidth=2.5, label='Onda di terra')
    ax.plot([], [], 'b-', linewidth=2.5, label='Onda spaziale (ionosferica)')
    ax.legend(loc='upper right', fontsize=10)

    # Configurazione
    ax.set_xlim(0, 100)
    ax.set_ylim(-10, 35)
    ax.set_title('Zona di Skip: Onda di Terra vs Onda Spaziale', fontsize=14, fontweight='bold', pad=15)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'zona_skip.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'zona_skip.png'}")


def plot_muf_giornaliero():
    """
    Grafico MUF (Maximum Usable Frequency) durante le 24 ore.
    """
    fig, ax = plt.subplots(figsize=(12, 6))

    ore = np.arange(0, 25, 1)

    # MUF tipica (MHz) - variazione giornaliera per strato F2
    # Massimo nel pomeriggio, minimo di notte
    muf_estate = 12 + 8 * np.sin(np.pi * (ore - 6) / 12) * np.where((ore >= 6) & (ore <= 18), 1, 0.3)
    muf_estate = np.maximum(muf_estate, 5)  # Floor a 5 MHz

    muf_inverno = 8 + 5 * np.sin(np.pi * (ore - 7) / 10) * np.where((ore >= 7) & (ore <= 17), 1, 0.4)
    muf_inverno = np.maximum(muf_inverno, 4)

    # Plot
    ax.plot(ore, muf_estate, 'r-', linewidth=2.5, marker='o', markersize=4, label='Estate (alta attività solare)')
    ax.plot(ore, muf_inverno, 'b-', linewidth=2.5, marker='s', markersize=4, label='Inverno (bassa attività solare)')

    # Bande radioamatoriali
    bande = [
        (3.5, '80m'),
        (7, '40m'),
        (10.1, '30m'),
        (14, '20m'),
        (18, '17m'),
        (21, '15m'),
        (24.9, '12m'),
        (28, '10m'),
    ]

    for freq, nome in bande:
        if freq <= 22:
            ax.axhline(y=freq, color='gray', linestyle=':', alpha=0.5)
            ax.text(24.5, freq, nome, va='center', fontsize=9, color='gray')

    # Evidenzia periodo diurno
    ax.axvspan(6, 18, alpha=0.1, color='yellow', label='Ore diurne')
    ax.axvspan(0, 6, alpha=0.1, color='darkblue')
    ax.axvspan(18, 24, alpha=0.1, color='darkblue', label='Ore notturne')

    # Annotazioni
    ax.annotate('MUF massima\n(pomeriggio)', xy=(14, 20), xytext=(16, 23),
                fontsize=10, ha='center',
                arrowprops=dict(arrowstyle='->', color='red'))

    ax.annotate('MUF minima\n(pre-alba)', xy=(5, 5), xytext=(2, 8),
                fontsize=10, ha='center',
                arrowprops=dict(arrowstyle='->', color='blue'))

    # Configurazione
    ax.set_xlim(0, 24)
    ax.set_ylim(0, 30)
    ax.set_xlabel('Ora locale', fontsize=12, fontweight='bold')
    ax.set_ylabel('MUF (MHz)', fontsize=12, fontweight='bold')
    ax.set_title('Variazione Giornaliera della MUF (Frequenza Massima Utilizzabile)', fontsize=14, fontweight='bold')
    ax.set_xticks(range(0, 25, 2))
    ax.set_xticklabels([f'{h:02d}:00' for h in range(0, 25, 2)], rotation=45)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc='upper left', fontsize=10)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'muf_giornaliero.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'muf_giornaliero.png'}")


def plot_angolo_critico():
    """
    Diagramma angolo critico e rifrazione ionosferica.
    Mostra la relazione tra angolo di incidenza e riflessione.
    """
    fig, ax = plt.subplots(figsize=(12, 8))

    # Terra
    ax.fill_between([0, 100], [0, 0], [-5, -5], color='#8B4513', alpha=0.5)
    ax.axhline(y=0, color='brown', linewidth=2)
    ax.text(50, -3, 'TERRA', ha='center', fontsize=11, fontweight='bold', color='white')

    # Ionosfera
    ax.fill_between([0, 100], [40, 40], [45, 45], color='#FF6347', alpha=0.4)
    ax.axhline(y=40, color='red', linewidth=2, linestyle='--')
    ax.text(85, 42, 'IONOSFERA', ha='center', fontsize=11, fontweight='bold', color='darkred')

    # Antenna
    ax.plot([10, 10], [0, 5], 'k-', linewidth=3)
    ax.plot([8, 12], [5, 5], 'k-', linewidth=2)
    ax.text(10, 7, 'TX', ha='center', fontsize=10, fontweight='bold')

    # Raggio 1: Angolo verticale (frequenza critica) - NON riflesso
    ax.annotate('', xy=(10, 40), xytext=(10, 5),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.annotate('', xy=(10, 55), xytext=(10, 40),
                arrowprops=dict(arrowstyle='->', color='red', lw=2, linestyle='dashed'))
    ax.text(12, 25, 'f > fc\n(attraversa)', fontsize=9, color='red', ha='left')

    # Raggio 2: Angolo critico - riflessione al limite
    ax.annotate('', xy=(35, 40), xytext=(10, 5),
                arrowprops=dict(arrowstyle='->', color='orange', lw=2))
    ax.annotate('', xy=(60, 5), xytext=(35, 40),
                arrowprops=dict(arrowstyle='->', color='orange', lw=2))
    ax.plot(35, 40, 'o', color='orange', markersize=10)
    ax.text(35, 43, 'θc', fontsize=11, fontweight='bold', color='orange', ha='center')

    # Raggio 3: Angolo basso - riflessione normale
    ax.annotate('', xy=(50, 40), xytext=(10, 5),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.annotate('', xy=(90, 5), xytext=(50, 40),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.plot(50, 40, 'o', color='green', markersize=10)
    ax.text(55, 25, 'f < MUF\n(riflesso)', fontsize=9, color='green', ha='left')

    # Angoli
    arc1 = Arc((10, 5), 10, 10, angle=0, theta1=60, theta2=90, color='orange', lw=2)
    ax.add_patch(arc1)
    ax.text(13, 12, 'θc', fontsize=10, color='orange')

    arc2 = Arc((10, 5), 15, 15, angle=0, theta1=30, theta2=90, color='green', lw=2)
    ax.add_patch(arc2)
    ax.text(18, 14, 'θ < θc', fontsize=9, color='green')

    # Formule
    formula_box = dict(boxstyle='round', facecolor='lightyellow', alpha=0.9)
    ax.text(75, 30, 'Formule:\n\nfc = 9√N  (MHz)\n\nMUF = fc / cos(θ)\n\nθc = angolo critico',
            fontsize=10, ha='left', va='top', bbox=formula_box, family='monospace')

    # Legenda
    ax.plot([], [], 'r-', lw=2, label='f > fc (attraversa ionosfera)')
    ax.plot([], [], '-', color='orange', lw=2, label='f = MUF (angolo critico θc)')
    ax.plot([], [], 'g-', lw=2, label='f < MUF (riflessione)')
    ax.legend(loc='lower right', fontsize=10)

    # Configurazione
    ax.set_xlim(0, 100)
    ax.set_ylim(-8, 55)
    ax.set_title('Angolo Critico e Rifrazione Ionosferica', fontsize=14, fontweight='bold')
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'angolo_critico.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'angolo_critico.png'}")


def plot_propagazione_multihop():
    """
    Diagramma propagazione multi-hop per comunicazioni DX.
    """
    fig, ax = plt.subplots(figsize=(14, 6))

    # Terra (arco)
    theta = np.linspace(-0.1, np.pi + 0.1, 100)
    r_terra = 30
    x_terra = r_terra * np.cos(theta) * 3 + 50
    y_terra = r_terra * np.sin(theta) - 28

    ax.fill_between(x_terra, y_terra, -5, color='#8B4513', alpha=0.5)
    ax.plot(x_terra, y_terra, 'brown', linewidth=2)

    # Ionosfera
    r_iono = 40
    x_iono = r_iono * np.cos(theta) * 3 + 50
    y_iono = r_iono * np.sin(theta) - 28

    ax.fill_between(x_iono, y_iono, y_iono + 3, color='#FF6347', alpha=0.3)
    ax.plot(x_iono, y_iono, 'red', linewidth=2, linestyle='--')

    # Percorso multi-hop
    hops = [(5, 2), (20, 13), (35, 2), (50, 13), (65, 2), (80, 13), (95, 2)]

    for i in range(len(hops) - 1):
        x1, y1 = hops[i]
        x2, y2 = hops[i + 1]
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color='blue', lw=2,
                                    connectionstyle='arc3,rad=-0.3' if i % 2 == 0 else 'arc3,rad=0.3'))

    # Punti di riflessione
    for i, (x, y) in enumerate(hops):
        if y > 5:  # Riflessione ionosferica
            ax.plot(x, y, 'r*', markersize=12)
        else:  # Stazione o riflessione terra
            if i == 0:
                ax.plot([x, x], [y, y + 3], 'k-', linewidth=3)
                ax.text(x, y + 5, 'TX', ha='center', fontweight='bold')
            elif i == len(hops) - 1:
                ax.plot([x, x], [y, y + 3], 'k-', linewidth=3)
                ax.text(x, y + 5, 'RX', ha='center', fontweight='bold')
            else:
                ax.plot(x, y, 'ko', markersize=6)

    # Etichette hop
    ax.text(27, 8, '1° hop', fontsize=9, color='blue', ha='center')
    ax.text(57, 8, '2° hop', fontsize=9, color='blue', ha='center')
    ax.text(87, 8, '3° hop', fontsize=9, color='blue', ha='center')

    # Distanza totale
    ax.annotate('', xy=(95, -1), xytext=(5, -1),
                arrowprops=dict(arrowstyle='<->', color='gray', lw=1.5))
    ax.text(50, -3, 'Distanza totale: ~6000-10000 km (DX mondiale)', ha='center', fontsize=10, color='gray')

    # Annotazioni
    ax.text(50, 15, 'IONOSFERA', ha='center', fontsize=11, fontweight='bold', color='darkred')
    ax.text(50, -6, 'Propagazione Multi-Hop HF', ha='center', fontsize=12, fontweight='bold')

    # Configurazione
    ax.set_xlim(-5, 105)
    ax.set_ylim(-10, 20)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Comunicazioni DX Mondiali via Salti Multipli', fontsize=14, fontweight='bold', pad=15)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'propagazione_multihop.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'propagazione_multihop.png'}")


def main():
    """Genera tutti i diagrammi di propagazione ionosferica."""
    print("Generazione diagrammi propagazione ionosferica...")
    print(f"Directory output: {OUTPUT_DIR}\n")

    plot_strati_ionosferici()
    plot_zona_skip()
    plot_muf_giornaliero()
    plot_angolo_critico()
    plot_propagazione_multihop()

    print("\n✅ Tutti i diagrammi sono stati generati con successo!")


if __name__ == "__main__":
    main()
