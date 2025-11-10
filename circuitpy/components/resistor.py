## Modelado de resistencia (res) lo mas preciso que se pueda realizar

from .base import * #Importo todo los elementos de base

class Resistor(Component): #Importo las caracteristicas de Component
    def __init__(self, name, n1, n2, resistance, rho=0, temp=20, pot = 0.25):
        super().__init__(name, n1, n2)
        self.R = resistance #Si se agrega un valor a rho la resistencia debe modificarse en funcion a la temperatura
        self.rho = rho
        self.t0 = temp
        self.pot = pot
        
    def stamp(self, G, I, node_map):
        g = 1.0/self.R #la conductancia es la inversa de la resistencia
        n1 = node_map[self.n1]
        n2 = node_map[self.n2]
        if n1 != 0: G[n1-1, n1-1] += g
        if n2 != 0: G[n2-1, n2-1] += g
        if n1 != 0 and n2 != 0:
            G[n1-1, n2-1] -= g
            G[n2-1, n1-1] -= g