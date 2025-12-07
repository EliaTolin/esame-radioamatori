#!/usr/bin/env python3
"""
Genera il grafico della modulazione AM.
Mostra segnale modulante e segnale modulato.
"""

import matplotlib.pyplot as plt
import numpy as np

from utils import get_output_dir, setup_matplotlib_style, save_figure, run_with_error_handling


def plot_modulazione_am():
    """Genera il grafico della modulazione AM."""
    setup_matplotlib_style()

    # Parametri
    t = np.linspace(0, 4*np.pi, 1000)
    f_c = 10  # frequenza portante
    f_m = 1   # frequenza modulante
    A_c = 1   # ampiezza portante
    m = 0.5   # indice di modulazione

    # Segnale modulante
    modulating = np.sin(2*np.pi*f_m*t)

    # AM: s(t) = (A_c + m*modulating) * cos(2*pi*f_c*t)
    am_signal = (A_c + m * modulating) * np.cos(2*np.pi*f_c*t)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    # Segnale modulante
    ax1.plot(t, modulating, color='blue')
    ax1.set_title('Segnale Modulante')
    ax1.grid(True)

    # Segnale AM
    ax2.plot(t, am_signal, color='red')
    ax2.set_title('Segnale Modulato AM')
    ax2.grid(True)

    plt.tight_layout()
    save_figure(fig, '01_elettronica', 'grafico_modulazione_am.png')


def main():
    """Funzione principale."""
    plot_modulazione_am()


if __name__ == "__main__":
    exit(run_with_error_handling(main, "plot_modulazione_am"))
