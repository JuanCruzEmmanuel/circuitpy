import numpy as np

class Circuit:
    def __init__(self):
        self.components = []
        self.voltage_sources = []
        self.nodes = set(["0"])  # incluir tierra por defecto

    def add(self, component):
        self.components.append(component)
        self.nodes.update([component.n1, component.n2])
        if component.__class__.__name__ == "VoltageSource":
            self.voltage_sources.append(component)

    def solve(self):
        node_list = list(self.nodes - {"0"})
        node_map = {name: i+1 for i, name in enumerate(node_list)}
        node_map["0"] = 0

        n = len(node_list)
        m = len(self.voltage_sources)

        # Matrices del sistema MNA
        G = np.zeros((n, n))
        I = np.zeros((n, 1))
        B = np.zeros((n, m))
        E = np.zeros((m, 1))

        # Primer barrido: resistencias y otros componentes pasivos
        for c in self.components:
            if c.__class__.__name__ != "VoltageSource":
                c.stamp(G, I, node_map)

        # Segundo barrido: fuentes de voltaje
        for i, src in enumerate(self.voltage_sources):
            src.stamp(G, I, node_map, B, E, i)

        # Construir el sistema extendido
        if m > 0:
            C = B.T
            D = np.zeros((m, m))
            A = np.block([[G, B], [C, D]])
            Z = np.vstack((I, E))
        else:
            A = G
            Z = I

        # Resolver el sistema
        X = np.linalg.solve(A, Z)

        # Extraer resultados
        V_nodes = X[:n]
        result = {node_list[i]: float(V_nodes[i]) for i in range(n)}
        result["0"] = 0.0

        if m > 0:
            I_sources = X[n:]
            for i, src in enumerate(self.voltage_sources):
                result[f"I({src.name})"] = float(I_sources[i])

        return result