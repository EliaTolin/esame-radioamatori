#!/usr/bin/env python3
"""
Genera il grafico di un segnale sinusoidale.
Mostra ampiezza, periodo e frequenza.
"""

import matplotlib.pyplot as plt
import numpy as np

from utils import get_output_dir, setup_matplotlib_style, save_figure, run_with_error_handling


def plot_segnale_sinusoidale():
    """Genera il grafico del segnale sinusoidale."""
    setup_matplotlib_style()

    # Parametri
    t = np.linspace(0, 4*np.pi, 1000)  # Due periodi
    omega = 1  # pulsazione
    V_m = 1  # ampiezza

    # Segnale sinusoidale
    v_t = V_m * np.sin(omega * t)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(t, v_t, color='blue', linewidth=2)
    ax.set_xlabel('Tempo (t)')
    ax.set_ylabel('v(t)')
    ax.set_title('Segnale Sinusoidale: v(t) = sin(wt)')
    ax.grid(True)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    # Annotazioni per periodo
    ax.annotate('T = 2pi', xy=(2*np.pi, 0), xytext=(2*np.pi + 0.5, 0.5),
                arrowprops=dict(arrowstyle='->', color='red'))
    ax.annotate('f = 1/T', xy=(np.pi, 0.8), xytext=(np.pi + 0.5, 0.9),
                fontsize=10, color='green')

    plt.tight_layout()
    save_figure(fig, '01_elettronica', 'grafico_segnale_sinusoidale.png')


def main():
    """Funzione principale."""
    plot_segnale_sinusoidale()


if __name__ == "__main__":
    exit(run_with_error_handling(main, "plot_segnale_sinusoidale"))
