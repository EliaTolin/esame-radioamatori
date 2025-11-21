#!/usr/bin/env python3
"""
Script per generare diagrammi elettrici per il Capitolo 3 - Circuiti (versione semplificata)
"""

import schemdraw
import schemdraw.elements as elm
import os

def setup_output_directory():
    """Crea la directory images/03_circuiti se non esiste"""
    if not os.path.exists('../images/03_circuiti'):
        os.makedirs('../images/03_circuiti')
    print("Directory images/03_circuiti pronta")

def draw_circuit_combinations():
    """Disegna circuiti di combinazione di componenti"""
    
    # Circuito con trasformatore accoppiato
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceV().label('V_in')
    d1 += elm.Resistor().label('R1').right()
    d1 += elm.Capacitor().label('C1').right()
    d1 += elm.Transformer().label('T1').right()
    d1 += elm.Resistor().label('R2').down()
    d1 += elm.Capacitor().label('C2').down()
    d1 += elm.Ground()
    d1 += elm.Line().right()
    d1 += elm.Label('V_out')
    d1 += elm.Resistor().label('R_L').down()
    d1 += elm.Ground()
    d1.save('../images/03_circuiti/circuito_trasformatore_accoppiamento.svg')
    
    # Circuito RLC parallelo
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceSin().label('V_in')
    d2 += elm.Resistor().label('R').right()
    d2.push()
    d2 += elm.Inductor().label('L').down()
    d2 += elm.Ground()
    d2.pop()
    d2 += elm.Capacitor().label('C').down()
    d2 += elm.Ground()
    d2 += elm.Line().right()
    d2 += elm.Label('V_out')
    d2 += elm.Resistor().label('R_L').down()
    d2 += elm.Ground()
    d2.save('../images/03_circuiti/circuito_rlc_parallelo.svg')
    
    # Ponte di Wheatstone semplificato
    d3 = schemdraw.Drawing(unit=3)
    d3 += elm.SourceV().label('V_in')
    d3.push()
    d3 += elm.Resistor().label('R1').right()
    d3 += elm.Resistor().label('R2').down()
    d3 += elm.Ground()
    d3.pop()
    d3 += elm.Resistor().label('R3').right()
    d3 += elm.Resistor().label('R4').down()
    d3 += elm.Ground()
    d3 += elm.Line().right()
    d3 += elm.Label('V_out')
    d3 += elm.Resistor().label('R_L').down()
    d3 += elm.Ground()
    d3.save('../images/03_circuiti/circuito_ponte_wheatstone.svg')
    
    print("Circuiti di combinazione generati")

def draw_filter_circuits():
    """Disegna circuiti di filtri"""
    
    # Filtro passa-basso RC dettagliato
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceSin().label('V_in')
    d1 += elm.Resistor().label('R').right()
    d1 += elm.Capacitor().label('C').down()
    d1 += elm.Ground()
    d1 += elm.Line().right()
    d1 += elm.Label('V_out')
    d1 += elm.Resistor().label('R_L').down()
    d1 += elm.Ground()
    d1.save('../images/03_circuiti/filtro_passa_basso_rc_dettagliato.svg')
    
    # Filtro passa-alto CR
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceSin().label('V_in')
    d2 += elm.Capacitor().label('C').right()
    d2 += elm.Resistor().label('R').down()
    d2 += elm.Ground()
    d2 += elm.Line().right()
    d2 += elm.Label('V_out')
    d2 += elm.Resistor().label('R_L').down()
    d2 += elm.Ground()
    d2.save('../images/03_circuiti/filtro_passa_alto_cr_dettagliato.svg')
    
    # Filtro passa-banda RLC
    d3 = schemdraw.Drawing(unit=3)
    d3 += elm.SourceSin().label('V_in')
    d3 += elm.Resistor().label('R_s').right()
    d3 += elm.Inductor().label('L').right()
    d3 += elm.Capacitor().label('C').down()
    d3 += elm.Ground()
    d3 += elm.Line().right()
    d3 += elm.Label('V_out')
    d3 += elm.Resistor().label('R_L').down()
    d3 += elm.Ground()
    d3.save('../images/03_circuiti/filtro_passa_banda_rlc.svg')
    
    print("Circuiti di filtri generati")

def draw_resonant_circuits():
    """Disegna circuiti risonanti"""
    
    # Circuito risonante serie
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceSin().label('V_in')
    d1 += elm.Resistor().label('R').right()
    d1 += elm.Inductor().label('L').right()
    d1 += elm.Capacitor().label('C').right()
    d1 += elm.Line().down()
    d1 += elm.Line().left()
    d1.save('../images/03_circuiti/circuito_risonante_serie.svg')
    
    # Circuito risonante parallelo
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceSin().label('I_in')
    d2 += elm.Resistor().label('R').right()
    d2.push()
    d2 += elm.Inductor().label('L').down()
    d2 += elm.Ground()
    d2.pop()
    d2 += elm.Capacitor().label('C').down()
    d2 += elm.Ground()
    d2 += elm.Line().right()
    d2 += elm.Label('V_out')
    d2.save('../images/03_circuiti/circuito_risonante_parallelo.svg')
    
    # Circuito tank
    d3 = schemdraw.Drawing(unit=3)
    d3 += elm.SourceSin().label('V_in')
    d3.push()
    d3 += elm.Inductor().label('L').down()
    d3 += elm.Ground()
    d3.pop()
    d3 += elm.Capacitor().label('C').down()
    d3 += elm.Ground()
    d3 += elm.Line().right()
    d3 += elm.Label('V_out')
    d3.save('../images/03_circuiti/circuito_tank.svg')
    
    print("Circuiti risonanti generati")

def draw_impedance_circuits():
    """Disegna circuiti per calcolo di impedenza"""
    
    # Circuito complesso misto
    d1 = schemdraw.Drawing(unit=2.5)
    d1 += elm.SourceSin().label('V_in')
    d1 += elm.Resistor().label('R1').right()
    d1.push()
    d1 += elm.Inductor().label('L1').right()
    d1 += elm.Capacitor().label('C1').down()
    d1 += elm.Ground()
    d1.pop()
    d1 += elm.Resistor().label('R2').right()
    d1 += elm.Capacitor().label('C2').down()
    d1 += elm.Ground()
    d1 += elm.Line().right()
    d1 += elm.Label('V_out')
    d1 += elm.Resistor().label('R_L').down()
    d1 += elm.Ground()
    d1.save('../images/03_circuiti/circuito_impedenza_complesso.svg')
    
    # Circuito di matching
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceV().label('V_source')
    d2 += elm.Resistor().label('R_s').right()
    d2 += elm.Inductor().label('L_match').right()
    d2 += elm.Capacitor().label('C_match').down()
    d2 += elm.Ground()
    d2 += elm.Line().right()
    d2 += elm.Resistor().label('R_load').down()
    d2 += elm.Ground()
    d2.save('../images/03_circuiti/circuito_matching_impedenza.svg')
    
    print("Circuiti di impedenza generati")

def main():
    """Funzione principale che genera tutti i diagrammi per il capitolo 3"""
    print("Inizio generazione diagrammi per il Capitolo 3 - Circuiti...")
    
    setup_output_directory()
    draw_circuit_combinations()
    draw_filter_circuits()
    draw_resonant_circuits()
    draw_impedance_circuits()
    
    print("Tutti i diagrammi del Capitolo 3 sono stati generati con successo!")

if __name__ == "__main__":
    main()