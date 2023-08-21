import sys

class Graph():
    def __init__(self):
        self.edges = {'X':['A','B','C','E'],
                      'A':['X','B','D'],
                      'B':['X','A','D','H'],
                      'C':['X','L'],
                      'E':['X'],
                      'D':['A','B','F'],
                      'F':['D','H'],
                      'H':['B','F','G'],
                      'G':['H','Y'],
                      'L':['C','I','J'],
                      'J':['I','L'],
                      'I':['L','J','K'],
                      'K':['I','Y'],
                      'Y':['G','K'],
        }

        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        #Edges are bidirectional
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
        
edges = [
    ('X', 'A', 7),
    ('X', 'B', 2),
    ('X', 'C', 3),
    ('X', 'E', 4),
    ('A', 'B', 3),
    ('A', 'D', 4),
    ('B', 'D', 4),
    ('B', 'H', 5),
    ('C', 'L', 2),
    ('D', 'F', 1),
    ('F', 'H', 3),
    ('G', 'H', 2),
    ('G', 'Y', 2),
    ('I', 'J', 6),
    ('I', 'K', 4),
    ('I', 'L', 4),
    ('J', 'L', 1),
    ('K', 'Y', 5),
]

graph = Graph()
for edge in edges:
    graph.add_edge(*edge)        


def dijsktra(graph, start, goal):
    # TODO implement dijsktra's algorithm here
    # solve graph with dijsktra's algorithm to find the shortest path
    # between initial and end nodes
    # params:
    #   graph: Graph object
    #   initial: starting node ex: 'X'
    #   end: ending node ex: 'Y'
    # returns:
    #   path: list of nodes in the path from initial to end nodes
    unvisitedNodes = list(graph.edges.keys()) 
    maxVal = sys.maxsize #maximum possible value
    shortestPath = {}
    prevNode = {}   # Last node that leads to current Node
   
    for count in unvisitedNodes:
        shortestPath[count] = maxVal 
    shortestPath[start] = 0

    # Then iterate until lowest cost from the initial node and the goal node is found
    while unvisitedNodes:
        current_n = None
        for currentNode in unvisitedNodes:
            if current_n == None:
                current_n = currentNode
            elif shortestPath[currentNode] < shortestPath[current_n]:
                current_n = currentNode

        neighbors = graph.edges[current_n]
        for neighbor in neighbors:
            temp_shortest_path = shortestPath[current_n] + graph.weights[(current_n, neighbor)]
            if temp_shortest_path < shortestPath[neighbor]:
                shortestPath[neighbor] = temp_shortest_path
                prevNode[neighbor] = current_n

        unvisitedNodes.remove(current_n) #remove the node after the operation to prevent an inifinit loop
    path = []
    node = goal

    while node != start:
        path.append(node)
        node = prevNode[node]

    path.append(start)
    
    print(" - ".join(reversed(path)))  
    print("Cost from" ,initial_node,"to",goal_node,"is",shortestPath[goal])

initial_node = input("Enter Initial Node -> ")
goal_node = input("Enter Goal Node -> ")
print(initial_node,goal_node)

dijsktra(graph = graph,start = initial_node,goal = goal_node)

   