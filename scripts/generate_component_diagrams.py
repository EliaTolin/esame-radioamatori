#!/usr/bin/env python3
"""
Script per generare diagrammi elettrici dei componenti usando schemadraw
"""

import schemdraw
import schemdraw.elements as elm
from schemdraw import flow
import matplotlib.pyplot as plt
import os

def setup_output_directory():
    """Crea la directory images se non esiste"""
    if not os.path.exists('../images'):
        os.makedirs('../images')
    print("Directory images pronta")

def draw_resistor():
    """Disegna un resistore con simbolo europeo e americano"""
    # Simbolo europeo (rettangolo)
    d = schemdraw.Drawing(unit=2.5)
    d += elm.Resistor().label('R')
    d += elm.Line().length(1).right()
    d.save('../images/simbolo_resistore_europeo.svg')
    
    # Simbolo americano (zigzag)
    d2 = schemdraw.Drawing(unit=2.5)
    d2 += elm.ResistorIEEE().label('R')
    d2 += elm.Line().length(1).right()
    d2.save('../images/simbolo_resistore_americano.svg')
    
    print("Resistor generato")

def draw_capacitor():
    """Disegna un condensatore non polarizzato e polarizzato"""
    # Condensatore non polarizzato
    d = schemdraw.Drawing(unit=2.5)
    d += elm.Capacitor().label('C')
    d += elm.Line().length(1).right()
    d.save('../images/simbolo_condensatore.svg')
    
    # Condensatore polarizzato (usiamo un condensatore standard con indicazione)
    d2 = schemdraw.Drawing(unit=2.5)
    d2 += elm.Capacitor().label('C+')
    d2 += elm.Line().length(1).right()
    d2.save('../images/simbolo_condensatore_polarizzato.svg')
    
    print("Condensatore generato")

def draw_inductor():
    """Disegna un induttore"""
    d = schemdraw.Drawing(unit=2.5)
    d += elm.Inductor().label('L')
    d += elm.Line().length(1).right()
    d.save('../images/simbolo_induttore.svg')
    
    print("Induttore generato")

def draw_diode():
    """Disegna un diodo e LED"""
    # Diodo standard
    d = schemdraw.Drawing(unit=2.5)
    d += elm.Diode().label('D')
    d += elm.Line().length(1).right()
    d.save('../images/simbolo_diodo.svg')
    
    # LED
    d2 = schemdraw.Drawing(unit=2.5)
    d2 += elm.LED().label('LED')
    d2 += elm.Line().length(1).right()
    d2.save('../images/simbolo_led.svg')
    
    print("Diodo generato")

def draw_transistor_bjt():
    """Disegna transistor BJT NPN e PNP"""
    # Transistor NPN
    d = schemdraw.Drawing(unit=2.5)
    d += elm.BjtNpn().label('Q')
    d += elm.Line().length(1).right()
    d.save('../images/simbolo_transistor_npn.svg')
    
    print("Transistor BJT generato")

def draw_transistor_mosfet():
    """Disegna transistor MOSFET"""
    d = schemdraw.Drawing(unit=2.5)
    d += elm.NMos().label('Q')
    d += elm.Line().length(1).right()
    d.save('../images/simbolo_transistor_mosfet.svg')
    
    print("Transistor MOSFET generato")

def draw_transformer():
    """Disegna un trasformatore"""
    d = schemdraw.Drawing(unit=3)
    d += elm.Transformer().label('T')
    d += elm.Line().length(1).right()
    d.save('../images/simbolo_trasformatore.svg')
    
    print("Trasformatore generato")

def draw_valve():
    """Disegna una valvola termoionica (triodo) - usando un IC generico come rappresentazione"""
    d = schemdraw.Drawing(unit=3)
    d += elm.Ic().label('V').label('TRIODE', loc='bottom')
    d += elm.Line().length(1).right()
    d.save('../images/simbolo_valvola_triodo.svg')
    
    print("Valvola generata")

def draw_circuit_examples():
    """Disegna circuiti di esempio"""
    # Circuito serie RC
    d = schemdraw.Drawing(unit=3)
    d += elm.SourceV().label('V')
    d += elm.Resistor().label('R').right()
    d += elm.Capacitor().label('C').down()
    d += elm.Line().left()
    d += elm.Line().up()
    d.save('../images/circuito_serie_rc.svg')
    
    # Circuito raddrizzatore a ponte
    d2 = schemdraw.Drawing(unit=2.5)
    d2 += elm.SourceV().label('AC')
    d2.push()
    d2 += elm.Diode().right().label('D1')
    d2 += elm.Diode().down().label('D2')
    d2 += elm.Line().left()
    d2 += elm.Diode().up().label('D3')
    d2 += elm.Diode().right().label('D4')
    d2.pop()
    d2 += elm.Line().down()
    d2 += elm.Line().right()
    d2 += elm.Resistor().label('Load').down()
    d2 += elm.Line().left()
    d2.save('../images/circuito_ponte_raddrizzatore.svg')
    
    print("Circuiti di esempio generati")

def main():
    """Funzione principale che genera tutti i diagrammi"""
    print("Inizio generazione diagrammi elettrici...")
    
    setup_output_directory()
    
    # Simboli dei componenti
    draw_resistor()
    draw_capacitor()
    draw_inductor()
    draw_diode()
    draw_transistor_bjt()
    draw_transistor_mosfet()
    draw_transformer()
    draw_valve()
    
    # Circuiti di esempio
    draw_circuit_examples()
    
    print("Tutti i diagrammi sono stati generati con successo!")
    print("File salvati nella directory ../images/")

if __name__ == "__main__":
    main()