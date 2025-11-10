class Component:
    def __init__(self, name, n1, n2):
        self.name = name
        self.n1 = n1
        self.n2 = n2
        
    def stamp(self,G,I,node_map):
        """G: matriz de conductacias
        I: Vector corriente
        """
        raise NotImplementedError