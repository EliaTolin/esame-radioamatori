import matplotlib.pyplot as plt
import numpy as np

# Dati per il grafico: Curva V-I di un resistore (Legge di Ohm)
R = 1000  # Resistenza di 1kΩ
V = np.linspace(0, 10, 100)  # Tensione da 0 a 10V
I = V / R  # Corrente secondo la Legge di Ohm

# Crea il grafico
plt.figure(figsize=(8, 6))
plt.plot(V, I, label=f'R = {R} Ω', color='red', linewidth=2)
plt.xlabel('Tensione (V)')
plt.ylabel('Corrente (A)')
plt.title('Curva Caratteristica V-I di un Resistore')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Salva l'immagine
plt.savefig('/Users/giangio/Documents/GitHub/giangio/esame-radioamatori/images/grafico_resistore_vi.png', dpi=150)
print("Grafico salvato in images/grafico_resistore_vi.png")