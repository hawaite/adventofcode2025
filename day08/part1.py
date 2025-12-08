import networkx as nx
from itertools import combinations
from dataclasses import dataclass

@dataclass(frozen=True)
class Edge:
    p1:     tuple
    p2:     tuple
    weight: int

def calc_distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**0.5

def main():
    input_file = "./input.txt"
    with(open(input_file, "r")) as fp:
        lines = map(str.strip, fp.readlines())

    edges_to_take = 10 if input_file == "./example.txt" else 1000

    nodes = [tuple(map(int,line.split(","))) for line in lines]
    all_edges = combinations(nodes, 2)
    
    g = nx.Graph()
    g.add_nodes_from(nodes)
    
    edges_with_weights = [Edge(p1=x[0], p2=x[1], weight=calc_distance(x[0], x[1])) for x in all_edges]
    sorted_edges_with_weights = sorted(edges_with_weights, key=lambda edge: edge.weight)
    for i in range(edges_to_take):
        e = sorted_edges_with_weights[i]
        g.add_edge(e.p1, e.p2, weight=e.weight)

    circuits = sorted(map(len, list(nx.connected_components(g))), reverse=True)
    print(f"answer: {circuits[0] * circuits[1] * circuits[2]}")

if __name__ == "__main__":
    main()