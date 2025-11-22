import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch

def create_directories():
    """Create necessary directories for Chapter 5 diagrams"""
    dirs = [
        'images/05_trasmettitori'
    ]
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"Directory {dir_path} pronta")

def draw_block_diagram(ax, blocks, connections, title):
    """Draw a block diagram with matplotlib"""
    ax.set_xlim(0, 15)
    ax.set_ylim(-2, 3)
    ax.axis('off')
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)

    # Draw blocks
    for block in blocks:
        x, y, w, h, label, color = block
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                             facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, label, ha='center', va='center',
               fontsize=10, fontweight='bold')

    # Draw connections
    for conn in connections:
        x1, y1, x2, y2 = conn
        ax.arrow(x1, y1, x2-x1, y2-y1, head_width=0.1, head_length=0.1,
                fc='black', ec='black', length_includes_head=True)

def generate_transmitter_diagrams():
    """Generate all transmitter block diagrams for Chapter 5"""

    print("Generazione diagrammi trasmettitori...")

    # 1. CW Transmitter
    fig, ax = plt.subplots(figsize=(14, 6))

    blocks = [
        (0.5, 0.5, 1.5, 1, 'Oscillatore\nCW\n📡', '#e6f3ff'),
        (2.5, 0.5, 1.5, 1, 'Chiave\nElettronica\n🔑', '#ffe6e6'),
        (4.5, 0.5, 1.5, 1, 'Buffer\nAmp\n📈', '#e6ffe6'),
        (6.5, 0.5, 1.5, 1, 'Filtro\nPassa-Banda\n🎯', '#fff2e6'),
        (8.5, 0.5, 1.5, 1, 'Amp\nPotenza\n⚡', '#ffffe6'),
        (10.5, 0.5, 1.5, 1, 'Antenna\n📡', '#e6f3ff'),
        (2.5, 2, 1.5, 0.8, 'Manipolazione\nMorse\n👆', '#f0f0f0')
    ]

    connections = [
        (2, 1, 2.5, 1), (4, 1, 4.5, 1), (6, 1, 6.5, 1), (8, 1, 8.5, 1), (10, 1, 10.5, 1),
        (4, 2.4, 4, 1.5), (4, 1.5, 2.5, 1.5)
    ]

    draw_block_diagram(ax, blocks, connections, 'Schema a Blocchi Trasmettitore CW (A1A)')
    plt.tight_layout()
    plt.savefig('images/05_trasmettitori/cw_transmitter_blocks.svg', dpi=150, bbox_inches='tight')
    plt.close()
    print("CW transmitter blocks generato")

    # 2. SSB Transmitter
    fig, ax = plt.subplots(figsize=(18, 6))

    blocks = [
        (0.5, 0.5, 1.2, 1, 'Oscillatore\nPortante\n📡', '#e6f3ff'),
        (2.2, 0.5, 1.2, 1, 'Modulatore\nBilanciato\n⚖️', '#ffe6e6'),
        (3.9, 0.5, 1.2, 1, 'Filtro\nLaterale\n🎯', '#fff2e6'),
        (5.6, 0.5, 1.2, 1, 'Amp\nLineare\n📈', '#e6ffe6'),
        (7.3, 0.5, 1.2, 1, 'Filtro\nUscita\n🎯', '#fff2e6'),
        (9.0, 0.5, 1.2, 1, 'Amp\nPotenza\n⚡', '#ffffe6'),
        (10.7, 0.5, 1.2, 1, 'Antenna\n📡', '#e6f3ff'),
        (2.2, 2, 1.2, 0.8, 'Audio\n300-3400Hz\n🎵', '#f0f0f0')
    ]

    connections = [
        (1.7, 1, 2.2, 1), (3.5, 1, 3.9, 1), (5.2, 1, 5.6, 1), (6.9, 1, 7.3, 1),
        (8.6, 1, 9.0, 1), (10.3, 1, 10.7, 1), (12.0, 1, 13, 1),
        (3.5, 2.4, 3.5, 1.5), (3.5, 1.5, 2.2, 1.5)
    ]

    draw_block_diagram(ax, blocks, connections, 'Schema a Blocchi Trasmettitore SSB (J3E)')
    plt.tight_layout()
    plt.savefig('images/05_trasmettitori/ssb_transmitter_blocks.svg', dpi=150, bbox_inches='tight')
    plt.close()
    print("SSB transmitter blocks generato")

    # 3. FM Transmitter
    fig, ax = plt.subplots(figsize=(18, 6))

    blocks = [
        (0.5, 0.5, 1.2, 1, 'Oscillatore\nFM\n📡', '#e6f3ff'),
        (2.2, 0.5, 1.2, 1, 'Modulatore\nFrequenza\n🔄', '#ffe6e6'),
        (3.9, 0.5, 1.2, 1, 'Amp\nRF\n📈', '#e6ffe6'),
        (5.6, 0.5, 1.2, 1, 'Moltiplicatore\n⚡', '#ffcccc'),
        (7.3, 0.5, 1.2, 1, 'Filtro\nPassa-Banda\n🎯', '#fff2e6'),
        (9.0, 0.5, 1.2, 1, 'Amp\nPotenza\n⚡', '#ffffe6'),
        (10.7, 0.5, 1.2, 1, 'Antenna\n📡', '#e6f3ff'),
        (2.2, 2, 1.2, 0.8, 'Audio\n50-15kHz\n🎵', '#f0f0f0'),
        (2.2, -1, 1.2, 0.8, 'Pre-Enfasi\n🎛️', '#e6e6ff')
    ]

    connections = [
        (1.7, 1, 2.2, 1), (3.5, 1, 3.9, 1), (5.2, 1, 5.6, 1), (6.9, 1, 7.3, 1),
        (8.6, 1, 9.0, 1), (10.3, 1, 10.7, 1), (12.0, 1, 13, 1),
        (3.5, 2.4, 3.5, 1.5), (3.5, 1.5, 2.2, 1.5),
        (3.5, -0.6, 3.5, -0.1), (3.5, -0.1, 2.2, -0.1)
    ]

    draw_block_diagram(ax, blocks, connections, 'Schema a Blocchi Trasmettitore FM (F3E)')
    plt.tight_layout()
    plt.savefig('images/05_trasmettitori/fm_transmitter_blocks.svg', dpi=150, bbox_inches='tight')
    plt.close()
    print("FM transmitter blocks generato")

    print("Tutti i diagrammi trasmettitori generati con successo!")

if __name__ == "__main__":
    create_directories()
    generate_transmitter_diagrams()