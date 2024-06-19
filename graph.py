class Graph():
    def __init__(self):
        self.edges = {'X': ['A', 'B', 'C', 'E'],
                      'A': ['X', 'B', 'D'],
                      'B': ['X', 'A', 'D', 'H'],
                      'C': ['X', 'L'],
                      'E': ['X'],
                      'D': ['A', 'B', 'F'],
                      'F': ['D', 'H'],
                      'H': ['B', 'F', 'G'],
                      'G': ['H', 'Y'],
                      'L': ['C', 'I', 'J'],
                      'J': ['I', 'L'],
                      'I': ['L', 'J', 'K'],
                      'K': ['I', 'Y'],
                      'Y': ['G', 'K'],
                      }

        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        #Edges are bidirectional
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight