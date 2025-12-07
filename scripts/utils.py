#!/usr/bin/env python3
"""
Modulo utility per gli script di generazione immagini.
Fornisce funzioni comuni per path, stili e logging.
"""

import logging
import sys
from pathlib import Path
from typing import Optional, Dict, Any

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle


# =============================================================================
# PATH UTILITIES
# =============================================================================

# Root del progetto (due livelli sopra scripts/)
PROJECT_ROOT = Path(__file__).parent.parent

# Directory immagini base
IMAGES_DIR = PROJECT_ROOT / "images"


def get_output_dir(subdir: str) -> Path:
    """
    Restituisce il path della directory di output, creandola se necessario.

    Args:
        subdir: Sottodirectory in images/ (es. '01_elettronica', '04_ricevitori')

    Returns:
        Path della directory di output

    Example:
        >>> output_dir = get_output_dir('04_ricevitori')
        >>> output_dir
        PosixPath('/path/to/project/images/04_ricevitori')
    """
    output_path = IMAGES_DIR / subdir
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path


def get_image_path(subdir: str, filename: str) -> Path:
    """
    Restituisce il path completo per un'immagine.

    Args:
        subdir: Sottodirectory in images/
        filename: Nome del file (con estensione)

    Returns:
        Path completo del file
    """
    return get_output_dir(subdir) / filename


# =============================================================================
# LOGGING UTILITIES
# =============================================================================

def setup_logging(script_name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configura il logging per uno script.

    Args:
        script_name: Nome dello script (senza .py)
        level: Livello di logging (default: INFO)

    Returns:
        Logger configurato
    """
    logger = logging.getLogger(script_name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        formatter = logging.Formatter('[%(levelname)s] %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


# =============================================================================
# MATPLOTLIB STYLE UTILITIES
# =============================================================================

# Stile base per matplotlib
DEFAULT_STYLE = {
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 10,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'axes.grid': True,
    'grid.alpha': 0.3,
}


def setup_matplotlib_style(custom_style: Optional[Dict[str, Any]] = None) -> None:
    """
    Configura lo stile matplotlib con valori predefiniti.

    Args:
        custom_style: Dizionario con stili aggiuntivi da sovrascrivere
    """
    style = DEFAULT_STYLE.copy()
    if custom_style:
        style.update(custom_style)

    for key, value in style.items():
        plt.rcParams[key] = value


# =============================================================================
# COLOR PALETTES
# =============================================================================

# Palette Tailwind-inspired per diagrammi a blocchi
COLORS_BLOCK_DIAGRAM = {
    'audio': '#fef08a',      # yellow-200
    'rf': '#bbf7d0',         # green-200
    'mixer': '#bfdbfe',      # blue-200
    'filter': '#ddd6fe',     # violet-200
    'osc': '#fecaca',        # red-200
    'output': '#fed7aa',     # orange-200
    'control': '#fef08a',    # yellow-200
    'detector': '#fecaca',   # red-200
    'amp': '#bbf7d0',        # green-200
    'border': '#374151',     # gray-700
    'shadow': '#94a3b8',     # slate-400
}

# Palette per grafici scientifici
COLORS_SCIENTIFIC = {
    'primary': '#3b82f6',    # blue-500
    'secondary': '#22c55e',  # green-500
    'accent': '#ef4444',     # red-500
    'neutral': '#6b7280',    # gray-500
    'highlight': '#f59e0b',  # amber-500
}

# Sfondi per figure
BACKGROUNDS = {
    'light_blue': '#f0f9ff',
    'light_green': '#f0fdf4',
    'light_yellow': '#fef3c7',
    'light_slate': '#f8fafc',
    'white': 'white',
}


# =============================================================================
# DRAWING UTILITIES FOR BLOCK DIAGRAMS
# =============================================================================

def draw_block_with_shadow(
    ax,
    x: float,
    y: float,
    width: float,
    height: float,
    label: str,
    sublabel: str = '',
    color: str = '#bfdbfe',
    border_color: str = '#374151',
    shadow_color: str = '#94a3b8',
    fontsize: int = 9,
    shadow_offset: float = 0.002
) -> None:
    """
    Disegna un blocco con ombra per diagrammi a blocchi.

    Args:
        ax: Axes matplotlib
        x, y: Centro del blocco
        width, height: Dimensioni del blocco
        label: Etichetta principale
        sublabel: Etichetta secondaria (opzionale)
        color: Colore di riempimento
        border_color: Colore del bordo
        shadow_color: Colore dell'ombra
        fontsize: Dimensione font
        shadow_offset: Offset dell'ombra
    """
    # Ombra
    shadow = FancyBboxPatch(
        (x - width/2 + shadow_offset, y - height/2 - shadow_offset),
        width, height,
        boxstyle="round,pad=0.005,rounding_size=0.01",
        facecolor=shadow_color,
        edgecolor='none',
        zorder=1
    )
    ax.add_patch(shadow)

    # Blocco principale
    rect = FancyBboxPatch(
        (x - width/2, y - height/2),
        width, height,
        boxstyle="round,pad=0.005,rounding_size=0.01",
        facecolor=color,
        edgecolor=border_color,
        linewidth=1.5,
        zorder=2
    )
    ax.add_patch(rect)

    # Testo
    if sublabel:
        ax.text(x, y + 0.015, label, ha='center', va='center',
                fontsize=fontsize, fontweight='bold', color='#1e293b', zorder=3)
        ax.text(x, y - 0.015, sublabel, ha='center', va='center',
                fontsize=fontsize - 2, color='#475569', zorder=3)
    else:
        ax.text(x, y, label, ha='center', va='center',
                fontsize=fontsize, fontweight='bold', color='#1e293b', zorder=3)


def draw_arrow(
    ax,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    color: str = '#3b82f6',
    linewidth: float = 2,
    mutation_scale: int = 12
) -> None:
    """
    Disegna una freccia tra due punti.

    Args:
        ax: Axes matplotlib
        x1, y1: Punto di partenza
        x2, y2: Punto di arrivo
        color: Colore della freccia
        linewidth: Spessore linea
        mutation_scale: Dimensione punta freccia
    """
    ax.annotate(
        '',
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle='-|>',
            color=color,
            lw=linewidth,
            mutation_scale=mutation_scale
        )
    )


def draw_info_box(
    ax,
    x: float,
    y: float,
    text: str,
    text_color: str = '#1e40af',
    border_color: str = '#3b82f6',
    bg_color: str = 'white',
    fontsize: int = 9,
    padding: float = 0.4
) -> None:
    """
    Disegna un box informativo con testo.

    Args:
        ax: Axes matplotlib
        x, y: Posizione del box
        text: Testo da visualizzare
        text_color: Colore del testo
        border_color: Colore del bordo
        bg_color: Colore di sfondo
        fontsize: Dimensione font
        padding: Padding interno
    """
    ax.text(
        x, y, text,
        fontsize=fontsize,
        ha='center',
        va='center',
        color=text_color,
        linespacing=1.4,
        bbox=dict(
            boxstyle=f'round,pad={padding}',
            facecolor=bg_color,
            edgecolor=border_color,
            linewidth=2
        )
    )


def draw_legend(
    ax,
    x_start: float,
    y: float,
    items: list,
    fontsize: int = 9,
    spacing: float = 0.08
) -> None:
    """
    Disegna una legenda orizzontale.

    Args:
        ax: Axes matplotlib
        x_start: Posizione X iniziale
        y: Posizione Y
        items: Lista di tuple (colore, etichetta)
        fontsize: Dimensione font
        spacing: Spaziatura tra elementi
    """
    ax.text(x_start - 0.07, y, 'Legenda:', fontsize=fontsize, fontweight='bold', va='center')

    x = x_start
    for color, label in items:
        ax.add_patch(Rectangle(
            (x, y - 0.012),
            0.018, 0.024,
            facecolor=color,
            edgecolor='#374151',
            linewidth=1
        ))
        ax.text(x + 0.022, y, label, fontsize=fontsize - 1, va='center')
        x += spacing


# =============================================================================
# SAVE UTILITIES
# =============================================================================

def save_figure(
    fig,
    subdir: str,
    filename: str,
    dpi: int = 150,
    facecolor: Optional[str] = None,
    logger: Optional[logging.Logger] = None
) -> Path:
    """
    Salva una figura nella directory appropriata.

    Args:
        fig: Figura matplotlib
        subdir: Sottodirectory in images/
        filename: Nome del file
        dpi: Risoluzione
        facecolor: Colore di sfondo (opzionale)
        logger: Logger per messaggi (opzionale)

    Returns:
        Path del file salvato
    """
    filepath = get_image_path(subdir, filename)

    save_kwargs = {
        'dpi': dpi,
        'bbox_inches': 'tight',
        'edgecolor': 'none'
    }

    if facecolor:
        save_kwargs['facecolor'] = facecolor

    fig.savefig(filepath, **save_kwargs)
    plt.close(fig)

    if logger:
        logger.info(f"Salvato: {filepath}")
    else:
        print(f"[OK] Salvato: {filepath}")

    return filepath


# =============================================================================
# SCRIPT RUNNER UTILITIES
# =============================================================================

def run_with_error_handling(main_func, script_name: str) -> int:
    """
    Esegue una funzione main con gestione errori.

    Args:
        main_func: Funzione da eseguire
        script_name: Nome dello script per logging

    Returns:
        0 se successo, 1 se errore
    """
    logger = setup_logging(script_name)

    try:
        logger.info(f"Avvio {script_name}...")
        main_func()
        logger.info(f"{script_name} completato con successo!")
        return 0
    except Exception as e:
        logger.error(f"Errore in {script_name}: {e}")
        import traceback
        logger.debug(traceback.format_exc())
        return 1


if __name__ == "__main__":
    # Test delle utility
    print(f"PROJECT_ROOT: {PROJECT_ROOT}")
    print(f"IMAGES_DIR: {IMAGES_DIR}")
    print(f"Test get_output_dir: {get_output_dir('test')}")
