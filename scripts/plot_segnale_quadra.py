import matplotlib.pyplot as plt
import numpy as np

# Segnale quadra
t = np.linspace(0, 4*np.pi, 1000)
freq = 1 / (2*np.pi)  # frequenza per periodo 2pi
square_wave = np.sign(np.sin(2*np.pi * freq * t))

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(t, square_wave, color='red', linewidth=2)
ax.set_xlabel('Tempo (t)')
ax.set_ylabel('Ampiezza')
ax.set_title('Segnale Rettangolare (Quadra)')
ax.grid(True)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_yticks([-1, 0, 1])
ax.set_yticklabels(['-1', '0', '1'])

plt.tight_layout()
plt.savefig('images/01_elettronica/grafico_segnale_quadra.png', dpi=150)
plt.close()