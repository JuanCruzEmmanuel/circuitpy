from circuitpy.core.circuit import Circuit
from circuitpy.components.resistor import Resistor
from circuitpy.components.voltage_source import VoltageSource

ckt = Circuit()
ckt.add(VoltageSource("V1", "0", "1", 10)) #Nombre, nodo 1, nodo 2, valor V{dc}
ckt.add(Resistor("R1", "1", "2", 5))  #Nombre, nodo 1, nodo 2 y valor de resistencia
ckt.add(Resistor("R2", "2", "0", 5))

"""

0- -----GND----- ---V{dc}---- --1-- ----R----- 0 ----- GND

Simple circuito serie fuente, resistencia y calcula la corriente resultante
"""

res = ckt.solve()
print(res)

