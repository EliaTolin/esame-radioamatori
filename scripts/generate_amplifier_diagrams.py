#!/usr/bin/env python3
"""
Script per generare diagrammi di amplificatori per il Capitolo 3.
Amplificatori transistor, op-amp, RF, differenziali e push-pull.
"""

import schemdraw
import schemdraw.elements as elm

from utils import get_output_dir, run_with_error_handling


# Directory di output
OUTPUT_DIR = get_output_dir('03_circuiti')


def draw_simple_amplifiers():
    """Disegna circuiti di amplificatori semplici."""
    # Amplificatore base con transistor
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceV().label('V_cc')
    d1 += elm.Resistor().label('R_c').right()
    d1 += elm.BjtNpn().label('Q1').right()
    d1 += elm.Resistor().label('R_e').down()
    d1 += elm.Ground()
    d1 += elm.Line().right()
    d1 += elm.Label('V_out')
    d1 += elm.Resistor().label('R_L').down()
    d1 += elm.Ground()
    d1.save(OUTPUT_DIR / 'amplificatore_base_transistor.svg')

    # Amplificatore con op-amp
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.Opamp().label('U1').right()
    d2 += elm.Resistor().label('R_in').left()
    d2 += elm.Line().right()
    d2 += elm.Label('V_out')
    d2 += elm.Resistor().label('R_f').up()
    d2 += elm.Line().left()
    d2 += elm.Ground()
    d2.save(OUTPUT_DIR / 'amplificatore_opamp.svg')

    # Amplificatore RF
    d3 = schemdraw.Drawing(unit=3)
    d3 += elm.SourceSin().label('V_in')
    d3 += elm.Capacitor().label('C_in').right()
    d3 += elm.BjtNpn().label('Q_RF').right()
    d3 += elm.Capacitor().label('C_out').right()
    d3 += elm.Label('V_out')
    d3 += elm.Resistor().label('R_L').down()
    d3 += elm.Ground()
    d3.save(OUTPUT_DIR / 'amplificatore_rf.svg')

    print("[OK] Amplificatori semplici generati")


def draw_amplifier_configurations():
    """Disegna configurazioni di amplificatori."""
    # Amplificatore differenziale
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.Opamp().label('U1').right()
    d1 += elm.Resistor().label('R1').left()
    d1 += elm.Line().up()
    d1 += elm.SourceSin().label('V_in+').left()
    d1 += elm.Resistor().label('R2').down()
    d1 += elm.Ground()
    d1 += elm.Line().right()
    d1 += elm.Label('V_out')
    d1 += elm.Resistor().label('R_L').down()
    d1 += elm.Ground()
    d1.save(OUTPUT_DIR / 'amplificatore_differenziale.svg')

    # Amplificatore push-pull
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceV().label('V_in')
    d2 += elm.BjtNpn().label('Q1').right()
    d2 += elm.BjtPnp().label('Q2').down()
    d2 += elm.Line().right()
    d2 += elm.Label('V_out')
    d2 += elm.Resistor().label('R_L').down()
    d2 += elm.Ground()
    d2.save(OUTPUT_DIR / 'amplificatore_push_pull.svg')

    print("[OK] Configurazioni amplificatori generate")


def main():
    """Funzione principale che genera tutti i diagrammi di amplificatori."""
    print(f"Generazione diagrammi amplificatori in: {OUTPUT_DIR}\n")

    draw_simple_amplifiers()
    draw_amplifier_configurations()

    print(f"\nTutti i diagrammi salvati in: {OUTPUT_DIR}")


if __name__ == "__main__":
    exit(run_with_error_handling(main, "generate_amplifier_diagrams"))
