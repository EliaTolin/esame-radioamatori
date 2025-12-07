#!/usr/bin/env python3
"""
Generazione visualizzazioni comparative per tipi di modulazione.
AM, FM, SSB, e modi digitali (PSK, QAM).
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle
import numpy as np
from pathlib import Path

# Directory di output
OUTPUT_DIR = Path(__file__).parent.parent / "images" / "01_elettronica"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Configurazione stile
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3


def plot_waveform_comparison():
    """Confronto forme d'onda AM, FM, SSB nel dominio del tempo."""
    fig, axes = plt.subplots(4, 1, figsize=(14, 12))

    # Parametri comuni
    t = np.linspace(0, 0.1, 2000)
    fc = 100  # Frequenza portante (Hz per visualizzazione)
    fm = 10   # Frequenza modulante

    # Segnale modulante (audio)
    modulating = np.sin(2 * np.pi * fm * t)

    # Portante
    carrier = np.sin(2 * np.pi * fc * t)

    # 1. Segnale modulante (audio originale)
    axes[0].plot(t * 1000, modulating, 'b-', linewidth=1.5, label='Segnale audio')
    axes[0].fill_between(t * 1000, modulating, alpha=0.3)
    axes[0].set_ylabel('Ampiezza')
    axes[0].set_title('Segnale Modulante (Audio)', fontsize=14, fontweight='bold')
    axes[0].set_xlim(0, 100)
    axes[0].set_ylim(-1.5, 1.5)
    axes[0].legend(loc='upper right')

    # 2. AM - Modulazione di Ampiezza
    am_index = 0.8  # Indice di modulazione
    am_signal = (1 + am_index * modulating) * carrier
    axes[1].plot(t * 1000, am_signal, 'g-', linewidth=0.8)
    # Inviluppo
    axes[1].plot(t * 1000, 1 + am_index * modulating, 'r--', linewidth=1.5, label='Inviluppo')
    axes[1].plot(t * 1000, -(1 + am_index * modulating), 'r--', linewidth=1.5)
    axes[1].set_ylabel('Ampiezza')
    axes[1].set_title('AM - Modulazione di Ampiezza (m = 0.8)', fontsize=14, fontweight='bold')
    axes[1].set_xlim(0, 100)
    axes[1].set_ylim(-2.5, 2.5)
    axes[1].legend(loc='upper right')
    axes[1].annotate('Portante sempre presente', xy=(75, 1.8), fontsize=10, color='darkgreen')

    # 3. FM - Modulazione di Frequenza
    beta = 5  # Indice di modulazione FM
    fm_signal = np.sin(2 * np.pi * fc * t + beta * np.sin(2 * np.pi * fm * t))
    axes[2].plot(t * 1000, fm_signal, 'purple', linewidth=0.8)
    axes[2].set_ylabel('Ampiezza')
    axes[2].set_title('FM - Modulazione di Frequenza (beta = 5)', fontsize=14, fontweight='bold')
    axes[2].set_xlim(0, 100)
    axes[2].set_ylim(-1.5, 1.5)
    axes[2].annotate('Ampiezza costante\nFrequenza variabile', xy=(70, 1.1), fontsize=10, color='purple')

    # 4. SSB - Single Side Band (USB - Upper Side Band)
    # SSB = portante soppressa + una sola banda laterale
    ssb_signal = modulating * np.cos(2 * np.pi * fc * t)  # Semplificazione
    axes[3].plot(t * 1000, ssb_signal, 'orange', linewidth=0.8)
    axes[3].set_ylabel('Ampiezza')
    axes[3].set_xlabel('Tempo (ms)')
    axes[3].set_title('SSB - Banda Laterale Unica (portante soppressa)', fontsize=14, fontweight='bold')
    axes[3].set_xlim(0, 100)
    axes[3].set_ylim(-1.5, 1.5)
    axes[3].annotate('Nessuna portante\nSolo informazione', xy=(70, 1.1), fontsize=10, color='darkorange')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'confronto_forme_onda_modulazione.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'confronto_forme_onda_modulazione.png'}")


def plot_spectrum_comparison():
    """Confronto spettri di frequenza per AM, FM, SSB."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    fc = 1000  # Frequenza portante (kHz per visualizzazione)
    bw_audio = 3  # Larghezza banda audio (kHz)

    # Colori
    colors = {
        'carrier': '#e74c3c',
        'lsb': '#3498db',
        'usb': '#2ecc71',
        'fm': '#9b59b6'
    }

    # 1. AM-DSB (Double Side Band)
    ax = axes[0, 0]
    # Portante
    ax.bar([fc], [1], width=2, color=colors['carrier'], label='Portante', edgecolor='black')
    # Bande laterali
    for i in range(1, 4):
        height = 0.5 / i
        ax.bar([fc - i], [height], width=1, color=colors['lsb'], alpha=0.7)
        ax.bar([fc + i], [height], width=1, color=colors['usb'], alpha=0.7)
    ax.axvspan(fc - bw_audio, fc + bw_audio, alpha=0.1, color='gray')
    ax.set_xlim(fc - 6, fc + 6)
    ax.set_ylim(0, 1.3)
    ax.set_xlabel('Frequenza (kHz)')
    ax.set_ylabel('Ampiezza')
    ax.set_title('AM-DSB (Doppia Banda Laterale)', fontsize=13, fontweight='bold')
    ax.annotate(f'BW = 2 x {bw_audio} = {2*bw_audio} kHz', xy=(fc, 1.15), ha='center', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))
    ax.legend(['Portante', 'LSB', 'USB'], loc='upper right')

    # 2. SSB-USB (Upper Side Band)
    ax = axes[0, 1]
    # Solo USB, niente portante
    for i in range(1, 4):
        height = 0.8 / i
        ax.bar([fc + i], [height], width=1, color=colors['usb'], alpha=0.9)
    ax.axvspan(fc, fc + bw_audio, alpha=0.1, color='green')
    ax.axvline(fc, color='red', linestyle='--', alpha=0.5, label='Portante soppressa')
    ax.set_xlim(fc - 6, fc + 6)
    ax.set_ylim(0, 1.3)
    ax.set_xlabel('Frequenza (kHz)')
    ax.set_ylabel('Ampiezza')
    ax.set_title('SSB-USB (Banda Laterale Superiore)', fontsize=13, fontweight='bold')
    ax.annotate(f'BW = {bw_audio} kHz', xy=(fc + 1.5, 1.05), ha='center', fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
    ax.annotate('50% banda\n50% potenza', xy=(fc + 4, 0.6), fontsize=10, color='green')

    # 3. FM (Narrowband e Wideband)
    ax = axes[1, 0]
    # FM ha molte bande laterali (regola di Carson)
    deviation = 5  # kHz
    fm_bw = 2 * (deviation + bw_audio)  # Regola di Carson

    # Portante FM
    ax.bar([fc], [0.8], width=2, color=colors['fm'], label='Portante')
    # Bande laterali FM (decrescenti)
    for i in range(1, 8):
        height = 0.6 * np.exp(-i * 0.3)
        ax.bar([fc - i * 1.5], [height], width=1.2, color=colors['fm'], alpha=0.6)
        ax.bar([fc + i * 1.5], [height], width=1.2, color=colors['fm'], alpha=0.6)
    ax.axvspan(fc - fm_bw/2, fc + fm_bw/2, alpha=0.1, color='purple')
    ax.set_xlim(fc - 15, fc + 15)
    ax.set_ylim(0, 1.3)
    ax.set_xlabel('Frequenza (kHz)')
    ax.set_ylabel('Ampiezza')
    ax.set_title('FM - Modulazione di Frequenza', fontsize=13, fontweight='bold')
    ax.annotate(f'BW ≈ 2(Δf + fm) = {fm_bw:.0f} kHz\n(Regola di Carson)',
                xy=(fc, 1.1), ha='center', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='plum', alpha=0.8))

    # 4. Confronto larghezze di banda
    ax = axes[1, 1]
    modulations = ['AM-DSB', 'SSB', 'FM (NFM)', 'FM (WFM)']
    bandwidths = [6, 3, 16, 200]  # kHz tipici
    bar_colors = ['#e74c3c', '#2ecc71', '#9b59b6', '#8e44ad']

    bars = ax.barh(modulations, bandwidths, color=bar_colors, edgecolor='black', height=0.6)
    ax.set_xlabel('Larghezza di Banda (kHz)')
    ax.set_title('Confronto Larghezza di Banda', fontsize=13, fontweight='bold')
    ax.set_xlim(0, 250)

    # Etichette valori
    for bar, bw in zip(bars, bandwidths):
        ax.text(bw + 5, bar.get_y() + bar.get_height()/2, f'{bw} kHz',
               va='center', fontsize=11, fontweight='bold')

    # Note
    ax.annotate('NFM = Narrowband FM (radio PMR)\nWFM = Wideband FM (broadcast)',
                xy=(150, 0.3), fontsize=9, style='italic',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'confronto_spettri_modulazione.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'confronto_spettri_modulazione.png'}")


def plot_spectral_efficiency():
    """Tabella visuale efficienza spettrale per tipo di modulazione."""
    fig, ax = plt.subplots(figsize=(16, 12))

    # Dati efficienza spettrale
    modulations = [
        ('AM-DSB', '6 kHz', '25%', 'Bassa', 'Broadcast storico', '#FFCCCC'),
        ('AM-DSB-SC', '6 kHz', '50%', 'Media', 'Carrier soppressa', '#FFE5CC'),
        ('SSB', '3 kHz', '100%', 'Alta', 'Radioamatori HF', '#CCFFCC'),
        ('FM-NFM', '12-25 kHz', 'N/A', 'Bassa', 'PMR, ripetitori', '#CCE5FF'),
        ('FM-WFM', '150-200 kHz', 'N/A', 'Molto bassa', 'Broadcast FM', '#E5CCFF'),
        ('PSK31', '31 Hz', 'Alta', 'Molto alta', 'Digitale HF', '#CCFFCC'),
        ('FT8', '50 Hz', 'Alta', 'Molto alta', 'Weak signal', '#CCFFCC'),
        ('RTTY', '250-500 Hz', 'Media', 'Media', 'Telescrivente', '#FFFFCC'),
    ]

    # Intestazioni
    headers = ['Modulazione', 'Banda', 'Eff. Potenza', 'Eff. Spettrale', 'Uso Tipico']
    col_widths = [0.15, 0.15, 0.15, 0.15, 0.25]
    x_starts = [0.05]
    for w in col_widths[:-1]:
        x_starts.append(x_starts[-1] + w + 0.02)

    # Titolo
    ax.text(0.5, 0.96, 'Efficienza Spettrale per Tipo di Modulazione', fontsize=18, fontweight='bold',
            ha='center', transform=ax.transAxes)
    ax.text(0.5, 0.92, 'Confronto banda occupata e efficienza', fontsize=12,
            ha='center', transform=ax.transAxes, color='gray')

    # Header row
    y = 0.86
    for x, header, width in zip(x_starts, headers, col_widths):
        ax.add_patch(Rectangle((x, y - 0.025), width, 0.04, facecolor='#2c3e50',
                               edgecolor='black', linewidth=1, transform=ax.transAxes))
        ax.text(x + width/2, y, header, ha='center', va='center', fontsize=12,
               fontweight='bold', color='white', transform=ax.transAxes)

    # Dati
    row_height = 0.065
    for i, (mod, bw, eff_pow, eff_spec, use, color) in enumerate(modulations):
        y = 0.80 - i * row_height

        # Sfondo riga
        ax.add_patch(Rectangle((0.04, y - row_height/2 + 0.005), 0.92, row_height - 0.01,
                               facecolor=color, edgecolor='#ccc', linewidth=0.5,
                               transform=ax.transAxes))

        values = [mod, bw, eff_pow, eff_spec, use]
        for x, val, width in zip(x_starts, values, col_widths):
            fontweight = 'bold' if x == x_starts[0] else 'normal'
            ax.text(x + width/2, y, val, ha='center', va='center', fontsize=11,
                   fontweight=fontweight, transform=ax.transAxes)

    # Legenda colori
    legend_y = 0.12
    ax.text(0.1, legend_y, 'Legenda efficienza:', fontsize=11, fontweight='bold', transform=ax.transAxes)
    legend_items = [
        ('#CCFFCC', 'Alta efficienza'),
        ('#FFFFCC', 'Media efficienza'),
        ('#FFCCCC', 'Bassa efficienza'),
        ('#E5CCFF', 'Uso specifico'),
    ]
    x_leg = 0.28
    for color, label in legend_items:
        ax.add_patch(Rectangle((x_leg, legend_y - 0.012), 0.025, 0.024, facecolor=color,
                               edgecolor='black', transform=ax.transAxes))
        ax.text(x_leg + 0.03, legend_y, label, fontsize=10, va='center', transform=ax.transAxes)
        x_leg += 0.17

    # Note
    ax.text(0.5, 0.04, 'Efficienza Potenza: rapporto tra potenza informazione e potenza totale trasmessa\n'
                       'Efficienza Spettrale: quantita informazione per unita di banda (bit/s/Hz)',
           ha='center', fontsize=9, style='italic', transform=ax.transAxes, color='gray')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'efficienza_spettrale_modulazione.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'efficienza_spettrale_modulazione.png'}")


def plot_constellation_diagrams():
    """Diagrammi costellazione per modulazioni digitali PSK e QAM."""
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    # Configurazione comune
    for ax in axes.flat:
        ax.set_aspect('equal')
        ax.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)
        ax.axvline(x=0, color='gray', linestyle='-', linewidth=0.5)
        ax.set_xlabel('In-Phase (I)')
        ax.set_ylabel('Quadrature (Q)')
        ax.grid(True, alpha=0.3)

    # 1. BPSK (Binary PSK)
    ax = axes[0, 0]
    points = np.array([[-1, 0], [1, 0]])
    ax.scatter(points[:, 0], points[:, 1], s=200, c=['red', 'blue'], edgecolors='black', linewidth=2, zorder=5)
    ax.annotate('0', (points[0, 0], points[0, 1] + 0.3), ha='center', fontsize=12, fontweight='bold')
    ax.annotate('1', (points[1, 0], points[1, 1] + 0.3), ha='center', fontsize=12, fontweight='bold')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_title('BPSK (2 simboli)\n1 bit/simbolo', fontsize=12, fontweight='bold')

    # 2. QPSK (Quadrature PSK)
    ax = axes[0, 1]
    angles = np.array([np.pi/4, 3*np.pi/4, 5*np.pi/4, 7*np.pi/4])
    points = np.column_stack([np.cos(angles), np.sin(angles)])
    colors = ['red', 'blue', 'green', 'orange']
    ax.scatter(points[:, 0], points[:, 1], s=200, c=colors, edgecolors='black', linewidth=2, zorder=5)
    labels = ['00', '01', '11', '10']
    for p, label in zip(points, labels):
        ax.annotate(label, (p[0] * 1.4, p[1] * 1.4), ha='center', va='center', fontsize=11, fontweight='bold')
    # Cerchio unitario
    theta = np.linspace(0, 2*np.pi, 100)
    ax.plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.3)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_title('QPSK (4 simboli)\n2 bit/simbolo', fontsize=12, fontweight='bold')

    # 3. 8-PSK
    ax = axes[0, 2]
    angles = np.linspace(0, 2*np.pi, 9)[:-1]
    points = np.column_stack([np.cos(angles), np.sin(angles)])
    ax.scatter(points[:, 0], points[:, 1], s=150, c='purple', edgecolors='black', linewidth=2, zorder=5)
    labels = ['000', '001', '011', '010', '110', '111', '101', '100']
    for p, label in zip(points, labels):
        ax.annotate(label, (p[0] * 1.35, p[1] * 1.35), ha='center', va='center', fontsize=9, fontweight='bold')
    ax.plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.3)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_title('8-PSK (8 simboli)\n3 bit/simbolo', fontsize=12, fontweight='bold')

    # 4. 16-QAM
    ax = axes[1, 0]
    coords = [-3, -1, 1, 3]
    points = []
    for x in coords:
        for y in coords:
            points.append([x, y])
    points = np.array(points) / 3  # Normalizza
    ax.scatter(points[:, 0], points[:, 1], s=100, c='teal', edgecolors='black', linewidth=1.5, zorder=5)
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.8, 1.8)
    ax.set_title('16-QAM (16 simboli)\n4 bit/simbolo', fontsize=12, fontweight='bold')
    ax.annotate('Griglia 4x4', xy=(0, -1.5), ha='center', fontsize=10, style='italic')

    # 5. 64-QAM
    ax = axes[1, 1]
    coords = np.linspace(-7, 7, 8)
    points = []
    for x in coords:
        for y in coords:
            points.append([x, y])
    points = np.array(points) / 7
    ax.scatter(points[:, 0], points[:, 1], s=30, c='darkblue', edgecolors='black', linewidth=0.5, zorder=5)
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.8, 1.8)
    ax.set_title('64-QAM (64 simboli)\n6 bit/simbolo', fontsize=12, fontweight='bold')
    ax.annotate('Griglia 8x8', xy=(0, -1.5), ha='center', fontsize=10, style='italic')

    # 6. Confronto efficienza
    ax = axes[1, 2]
    modulations = ['BPSK', 'QPSK', '8-PSK', '16-QAM', '64-QAM', '256-QAM']
    bits_per_symbol = [1, 2, 3, 4, 6, 8]
    colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(modulations)))

    bars = ax.barh(modulations, bits_per_symbol, color=colors, edgecolor='black', height=0.6)
    ax.set_xlabel('Bit per Simbolo')
    ax.set_title('Efficienza Spettrale\nModulazioni Digitali', fontsize=12, fontweight='bold')
    ax.set_xlim(0, 10)

    for bar, bps in zip(bars, bits_per_symbol):
        ax.text(bps + 0.2, bar.get_y() + bar.get_height()/2, f'{bps} bit/sym',
               va='center', fontsize=10, fontweight='bold')

    ax.annotate('Maggiore efficienza =\nPiu sensibile al rumore', xy=(6.5, 1), fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.suptitle('Diagrammi a Costellazione - Modulazioni Digitali', fontsize=16, fontweight='bold', y=1.02)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'diagrammi_costellazione.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'diagrammi_costellazione.png'}")


def plot_modulation_overview():
    """Panoramica completa tipi di modulazione con caratteristiche."""
    fig, ax = plt.subplots(figsize=(16, 14))

    # Dati modulazioni
    modulations = [
        ('Modulazioni Analogiche', '#FFE5CC', [
            ('AM', 'Ampiezza', 'A1A/A3E', 'Semplice, broadcast', 'Bassa'),
            ('FM', 'Frequenza', 'F3E', 'Resistente rumore', 'Alta'),
            ('PM', 'Fase', 'G3E', 'Usata in FM indiretto', 'Alta'),
            ('SSB', 'Ampiezza', 'J3E', 'Efficiente, HF radio', 'Media'),
        ]),
        ('Modulazioni Digitali Base', '#CCFFCC', [
            ('ASK/OOK', 'Ampiezza', 'A1D', 'On/Off, semplice', 'Bassa'),
            ('FSK', 'Frequenza', 'F1D', 'Robusta, RTTY', 'Media'),
            ('PSK', 'Fase', 'G1D', 'Efficiente, WiFi', 'Alta'),
        ]),
        ('Modulazioni Digitali Avanzate', '#CCE5FF', [
            ('QPSK', 'Fase (4)', 'G1D', '2 bit/simbolo, DVB', 'Alta'),
            ('8-PSK', 'Fase (8)', 'G1D', '3 bit/simbolo', 'Molto Alta'),
            ('16-QAM', 'Ampiezza+Fase', 'D7D', '4 bit/simbolo, LTE', 'Molto Alta'),
            ('64-QAM', 'Ampiezza+Fase', 'D7D', '6 bit/simbolo, 5G', 'Altissima'),
        ]),
        ('Modi Radioamatoriali', '#E5CCFF', [
            ('CW', 'On/Off', 'A1A', 'Morse, DX', 'Bassissima'),
            ('FT8', 'GFSK', 'F1D', 'Weak signal, -24dB', 'Media'),
            ('PSK31', 'BPSK', 'G1D', 'Tastiera, QRP', 'Bassa'),
            ('RTTY', 'FSK', 'F1D', 'Contest, 45.45 baud', 'Bassa'),
        ]),
    ]

    # Titolo
    ax.text(0.5, 0.98, 'Panoramica Tipi di Modulazione', fontsize=20, fontweight='bold',
            ha='center', transform=ax.transAxes)
    ax.text(0.5, 0.95, 'Caratteristiche, designatori ITU e applicazioni', fontsize=12,
            ha='center', transform=ax.transAxes, color='gray')

    # Intestazioni colonne
    headers = ['Tipo', 'Parametro', 'Designatore', 'Caratteristiche', 'Complessita']
    col_widths = [0.10, 0.12, 0.10, 0.28, 0.12]
    x_starts = [0.05]
    for w in col_widths[:-1]:
        x_starts.append(x_starts[-1] + w + 0.02)

    y = 0.90
    row_height = 0.024
    header_height = 0.032

    for cat_name, cat_color, mods in modulations:
        # Header categoria
        ax.add_patch(Rectangle((0.03, y - header_height), 0.94, header_height,
                               facecolor=cat_color, edgecolor='black', linewidth=1.5,
                               transform=ax.transAxes))
        ax.text(0.04, y - header_height/2, cat_name, ha='left', va='center',
               fontsize=13, fontweight='bold', transform=ax.transAxes)

        y -= header_height + 0.005

        # Righe dati
        for i, (mod, param, desig, chars, compl) in enumerate(mods):
            bg_color = '#f8f9fa' if i % 2 == 0 else 'white'
            ax.add_patch(Rectangle((0.03, y - row_height), 0.94, row_height,
                                   facecolor=bg_color, edgecolor='#e0e0e0', linewidth=0.5,
                                   transform=ax.transAxes))

            values = [mod, param, desig, chars, compl]
            for x, val, width in zip(x_starts, values, col_widths):
                fontweight = 'bold' if x == x_starts[0] else 'normal'
                fontsize = 10 if x == x_starts[3] else 11
                ax.text(x + width/2, y - row_height/2, val, ha='center', va='center',
                       fontsize=fontsize, fontweight=fontweight, transform=ax.transAxes)

            y -= row_height

        y -= 0.015

    # Note in fondo
    ax.text(0.5, 0.03, 'Designatori ITU: prima lettera = tipo portante, seconda = tipo modulazione, terza = tipo informazione\n'
                       'A = Ampiezza, F = Frequenza, G = Fase, D = Dati, E = Voce',
           ha='center', fontsize=9, style='italic', transform=ax.transAxes, color='gray')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'panoramica_modulazioni.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'panoramica_modulazioni.png'}")


def main():
    """Genera tutte le visualizzazioni comparative modulazione."""
    print("Generazione visualizzazioni comparative modulazione...")
    print(f"Directory output: {OUTPUT_DIR}\n")

    plot_waveform_comparison()
    plot_spectrum_comparison()
    plot_spectral_efficiency()
    plot_constellation_diagrams()
    plot_modulation_overview()

    print("\n✅ Tutte le visualizzazioni sono state generate con successo!")


if __name__ == "__main__":
    main()
