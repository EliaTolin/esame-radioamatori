#!/usr/bin/env python3
"""
Generazione tabella visuale dell'alfabeto fonetico NATO/ICAO.
Produce un'immagine PNG con la tabella completa per lo studio.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

# Directory di output
OUTPUT_DIR = Path(__file__).parent.parent / "images" / "b_operativa"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Configurazione stile
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['figure.facecolor'] = 'white'

# Alfabeto fonetico NATO/ICAO completo
ALFABETO = [
    ('A', 'Alfa'),    ('B', 'Bravo'),   ('C', 'Charlie'),
    ('D', 'Delta'),   ('E', 'Echo'),    ('F', 'Foxtrot'),
    ('G', 'Golf'),    ('H', 'Hotel'),   ('I', 'India'),
    ('J', 'Juliet'),  ('K', 'Kilo'),    ('L', 'Lima'),
    ('M', 'Mike'),    ('N', 'November'), ('O', 'Oscar'),
    ('P', 'Papa'),    ('Q', 'Quebec'),  ('R', 'Romeo'),
    ('S', 'Sierra'),  ('T', 'Tango'),   ('U', 'Uniform'),
    ('V', 'Victor'),  ('W', 'Whiskey'), ('X', 'X-Ray'),
    ('Y', 'Yankee'),  ('Z', 'Zulu'),
]

# Colori alternati per le righe
COLORE_CHIARO = '#E8F4FD'
COLORE_SCURO = '#D0E8F2'
COLORE_HEADER = '#2C3E50'
COLORE_LETTERA = '#E74C3C'
COLORE_TESTO = '#2C3E50'


def genera_tabella_alfabeto():
    """Genera una tabella visuale dell'alfabeto fonetico NATO."""
    fig, ax = plt.subplots(figsize=(10, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 32)
    ax.axis('off')

    # Titolo
    ax.text(5, 31.2, 'ALFABETO FONETICO NATO / ICAO',
            ha='center', va='center', fontsize=18, fontweight='bold',
            color=COLORE_HEADER)
    ax.text(5, 30.5, 'Standard internazionale per le comunicazioni radioamatoriali',
            ha='center', va='center', fontsize=10, color='#7F8C8D',
            style='italic')

    # Intestazioni colonne (3 colonne)
    col_positions = [1.5, 5, 8.5]
    header_y = 29.5
    for col_x in col_positions:
        ax.text(col_x - 0.5, header_y, 'Lettera', ha='center', va='center',
                fontsize=10, fontweight='bold', color='white',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORE_HEADER))
        ax.text(col_x + 0.8, header_y, 'Fonetico', ha='center', va='center',
                fontsize=10, fontweight='bold', color='white',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORE_HEADER))

    # Disposizione in 3 colonne da 9 righe
    righe_per_colonna = 9
    y_start = 28.5
    row_height = 0.95

    for i, (lettera, fonetico) in enumerate(ALFABETO):
        col = i // righe_per_colonna
        row = i % righe_per_colonna

        col_x = col_positions[col]
        y = y_start - row * row_height

        # Sfondo alternato
        bg_color = COLORE_CHIARO if row % 2 == 0 else COLORE_SCURO
        rect = mpatches.FancyBboxPatch(
            (col_x - 1.4, y - 0.35), 3.0, 0.7,
            boxstyle='round,pad=0.05',
            facecolor=bg_color, edgecolor='#BDC3C7', linewidth=0.5
        )
        ax.add_patch(rect)

        # Lettera (in rosso, grassetto)
        ax.text(col_x - 0.5, y, lettera, ha='center', va='center',
                fontsize=16, fontweight='bold', color=COLORE_LETTERA,
                fontfamily='monospace')

        # Separatore
        ax.text(col_x + 0.1, y, '=', ha='center', va='center',
                fontsize=12, color='#95A5A6')

        # Parola fonetica
        ax.text(col_x + 0.8, y, fonetico, ha='center', va='center',
                fontsize=12, fontweight='bold', color=COLORE_TESTO)

    # Nota in basso
    ax.text(5, 1.5, 'Fonte: Sub Allegato D (art. 3, comma 1, dell\'Allegato n. 26)',
            ha='center', va='center', fontsize=8, color='#95A5A6',
            style='italic')
    ax.text(5, 1.0, 'D.Lgs. 1 agosto 2003, n. 259 - Programma di Esame Radioamatore',
            ha='center', va='center', fontsize=8, color='#95A5A6',
            style='italic')

    plt.tight_layout()
    output_path = OUTPUT_DIR / 'alfabeto_fonetico_nato.png'
    fig.savefig(output_path, dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"Generato: {output_path}")


if __name__ == '__main__':
    genera_tabella_alfabeto()
