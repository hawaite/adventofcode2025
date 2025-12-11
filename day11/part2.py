from networkx import DiGraph
import networkx as nx

def path_count_between(source_node, dest_node, dag):
    # reset count attr
    nx.set_node_attributes(dag, 0, name="count")
    sorted_nodes = list(nx.topological_sort(dag))
    dag.nodes[source_node]["count"] = 1

    # need to drop nodes until we get to the source node
    while sorted_nodes[0] != source_node:
        sorted_nodes = sorted_nodes[1:]

    for node in sorted_nodes:
        for successor in dag.successors(node):
            dag.nodes[successor]["count"] += dag.nodes[node]["count"]

    return nx.get_node_attributes(dag, "count")[dest_node]

def main():
    with(open("./input.txt", "r")) as fp:
        lines = map(str.strip, fp.readlines())

    g = DiGraph()

    for line in lines:
        node_id, target_node_ids = line.split(": ")
        target_node_ids = target_node_ids.split(" ")
        g.add_edges_from([(node_id, target_node_id) for target_node_id in target_node_ids])
    nx.set_node_attributes(g, 0, name="count")

    # NOTE: From rendering the graph we know that there are no possible paths from dac to fft.
    # all paths go from fft to dac.
    # total is going to be (num paths from src to fft) * (num paths from fft to dac) * (num paths from dac to out)

    print(f"path count svr -> fft: {path_count_between("svr", "fft", g)}")
    print(f"path count fft -> dac: {path_count_between("fft", "dac", g)}")
    print(f"path count dac -> out: {path_count_between("dac", "out", g)}")

    print(f"total: {path_count_between("svr", "fft", g) * path_count_between("fft", "dac", g) * path_count_between("dac", "out", g)}")

if __name__ == "__main__":
    main()