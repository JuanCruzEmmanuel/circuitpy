## Modelado de resistencia (res) lo mas preciso que se pueda realizar

from .base import * #Importo todo los elementos de base

class Resistor(Component): #Importo las caracteristicas de Component
    
    
    def __init__(self, name, n1, n2, resistance, alpha=0.0039, t0=20.0, pot_max = 0.25):
        """
        Modelado de resistencia
        
        -alpha: Coeficiente de temperatura en 1/ºC; si no me equivoco 0.0039 es la del cobre
        -t0: Temperatura de referencia en ºC
        -pot_max: potencia maxima que soporta la resistencia
        
        """
        super().__init__(name, n1, n2)
        self.R = resistance #Si se agrega un valor a alpha la resistencia debe modificarse en funcion a la temperatura
        self.alpha = alpha
        self.t0 = t0
        self.Tt = t0 #temperatura en tiempo inicia igual que la que se estima "nominal"
        self.pot_max = pot_max
        self.burned = False #variable que va a controlar si el componente se quema, tal vez es mejor ponerle failure
        
    def stamp(self, G, I, node_map):
        g = 1.0/self.R #la conductancia es la inversa de la resistencia
        n1 = node_map[self.n1]
        n2 = node_map[self.n2]
        if n1 != 0: G[n1-1, n1-1] += g
        if n2 != 0: G[n2-1, n2-1] += g
        if n1 != 0 and n2 != 0:
            G[n1-1, n2-1] -= g
            G[n2-1, n1-1] -= g