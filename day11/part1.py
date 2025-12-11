from networkx import DiGraph
import networkx as nx

def main():
    with(open("./input.txt", "r")) as fp:
        lines = map(str.strip, fp.readlines())

    g = DiGraph()

    for line in lines:
        node_id, target_node_ids = line.split(": ")
        target_node_ids = target_node_ids.split(" ")
        g.add_edges_from([(node_id, target_node_id) for target_node_id in target_node_ids])

    print("total: ", len(list(nx.all_simple_paths(g, "you", "out"))))

if __name__ == "__main__":
    main()