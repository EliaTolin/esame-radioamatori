import matplotlib.pyplot as plt
import numpy as np

# Dati per il grafico: Campo magnetico B = μ0 * I / (2 * π * r)
mu0 = 4 * np.pi * 1e-7  # Permeabilità del vuoto
I = 10  # Corrente in A
r = np.linspace(0.001, 0.1, 100)  # Distanza da 0.001 m a 0.1 m
B = (mu0 * I) / (2 * np.pi * r)  # Induzione magnetica in T

# Crea il grafico
plt.figure(figsize=(8, 6))
plt.plot(r, B, label='B = μ₀ I / (2π r)', color='blue', linewidth=2)
plt.xlabel('Distanza r (m)')
plt.ylabel('Induzione Magnetica B (T)')
plt.title('Campo Magnetico attorno a un Conduttore')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Salva l'immagine
plt.savefig('/Users/giangio/Documents/GitHub/giangio/esame-radioamatori/images/grafico_campo_magnetico.png', dpi=150)
print("Grafico salvato in images/grafico_campo_magnetico.png")