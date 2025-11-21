#!/usr/bin/env python3
"""
Script per verificare gli elementi disponibili in schemadraw
"""

import schemdraw.elements as elm
import schemdraw.flow as flow

def print_available_elements():
    """Stampa tutti gli elementi disponibili"""
    print("Elementi disponibili in schemdraw.elements:")
    for attr in dir(elm):
        if not attr.startswith('_'):
            print(f"  - {attr}")
    
    print("\nElementi disponibili in schemdraw.flow:")
    for attr in dir(flow):
        if not attr.startswith('_'):
            print(f"  - {attr}")

if __name__ == "__main__":
    print_available_elements()