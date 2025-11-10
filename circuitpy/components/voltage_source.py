from .base import Component

class VoltageSource(Component):
    def __init__(self, name, n1, n2, voltage):
        super().__init__(name, n1, n2)
        self.V = voltage

    def stamp(self, G, I, node_map, B, E, source_index):
        n1 = node_map[self.n1]
        n2 = node_map[self.n2]

        if n1 != 0:
            B[n1-1, source_index] = 1
        if n2 != 0:
            B[n2-1, source_index] = -1

        E[source_index, 0] = self.V