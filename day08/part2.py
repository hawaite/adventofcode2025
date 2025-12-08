import networkx as nx
from networkx import Graph
from itertools import combinations
from dataclasses import dataclass

@dataclass(frozen=True)
class Edge:
    p1:     tuple
    p2:     tuple
    weight: int

def calc_distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**0.5

# hacky fast-escape thing for testing if the number of isolates is something greater than 0
# without identifying ALL isolates like the nx functions appear to do
def has_isolates(graph:Graph, nodes):
    for node in nodes:
        if graph.degree[node] == 0:
            return True
    return False

def main():
    input_file = "./input.txt"
    with(open(input_file, "r")) as fp:
        lines = map(str.strip, fp.readlines())

    nodes = [tuple(map(int,line.split(","))) for line in lines]
    all_edges = combinations(nodes, 2)

    g = nx.Graph()
    g.add_nodes_from(nodes)
    
    edges_with_weights = [Edge(p1=x[0], p2=x[1], weight=calc_distance(x[0], x[1])) for x in all_edges]
    sorted_edges_with_weights = sorted(edges_with_weights, key=lambda edge: edge.weight)
    
    # this is an absurdly inefficient way of doing this that takes single digit minutes to complete
    while has_isolates(g, nodes):
        
        e = sorted_edges_with_weights[0]
        sorted_edges_with_weights = sorted_edges_with_weights[1:]
        g.add_edge(e.p1, e.p2, weight=e.weight)

    print(f"answer: {e.p1[0] * e.p2[0]}")

if __name__ == "__main__":
    main()