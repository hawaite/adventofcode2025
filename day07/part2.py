from networkx import DiGraph
import networkx as nx

def count_root_to_leaves(dag:DiGraph, root):
    # dynamic programming over a topological sort of the directed-acylic graph
    # to count all possible paths to the leaf nodes
    topology = list(nx.topological_sort(dag))
    nx.set_node_attributes(dag, 0, name="count")
    dag.nodes[root]["count"] = 1

    for current_node in topology:
        count_current_node = dag.nodes[root]["count"]
        if count_current_node == 0:
            continue # bail. Nothing entered this node.
        for next_node in dag.successors(current_node):
            dag.nodes[next_node]["count"] += dag.nodes[current_node]["count"]
    
    # get all the leaf nodes on, get the count attribute on them and sum them.
    leaves = [n for n, d in dag.out_degree() if d == 0]
    return sum([nx.get_node_attributes(dag, "count")[x] for x in leaves])

def populate_grid_with_beams(lines):
    processed = []
    for line_ix, line in enumerate(lines):
        line_as_list = list(line)
        # move first line to output unconditionally
        if line_ix == 0:
            processed.append(line_as_list)
            continue
        
        # otherwise, iterate cells and apply rules based on previous row
        prev_row = processed[-1]
        for cell_ix, cell in enumerate(line_as_list):
            # if cell above is a pipe or an S, replace current cell with a beam
            if cell == "." and prev_row[cell_ix] in ["|", "S"]:
                line_as_list[cell_ix] = "|"
            # if a cell is a splitter with a beam above, split it
            elif cell == "^" and prev_row[cell_ix] == "|":
                line_as_list[cell_ix-1] = "|"
                line_as_list[cell_ix+1] = "|"
        processed.append(line_as_list)    
    return processed

def build_graph(lines) -> tuple[DiGraph, tuple[int,int]]:
    processed = populate_grid_with_beams(lines)

    # build a Directed Acyclic Graph (DAG) from the grid above
    graph = DiGraph()
    root = None
    for line_ix, line in enumerate(processed):
        for cell_ix, cell in enumerate(line):
            # for source, go straight down until we find a splitter
            if cell == "S":
                root = (line_ix, cell_ix)
                line_to_check = line_ix+1
                while processed[line_to_check][cell_ix] != "^":
                    line_to_check += 1
                graph.add_edge((line_ix, cell_ix), (line_to_check, cell_ix))
            # for splitters, they MUST have a beam above them or they werent used
            # iterate down the left column until you hit another splitter, then do the same on the right
            elif cell == "^" and processed[line_ix-1][cell_ix] == "|":
                # left check
                line_to_check = line_ix+1
                # need to check if we fall off the bottom. If we do, just pretend thats another leaf
                while line_to_check < len(processed) and processed[line_to_check][cell_ix-1] == "|":
                    line_to_check += 1
                graph.add_edge((line_ix, cell_ix), (line_to_check, cell_ix-1))

                # right check
                line_to_check = line_ix+1
                while line_to_check < len(processed) and processed[line_to_check][cell_ix+1] == "|":
                    line_to_check += 1
                graph.add_edge((line_ix, cell_ix), (line_to_check, cell_ix+1))
    return (graph, root)

def main():
    with(open("./input.txt", "r")) as fp:
        lines = list(map(str.strip, fp.readlines()))

    dag, root = build_graph(lines)
    
    print(f"total: {count_root_to_leaves(dag, root)}")
if __name__ == "__main__":
    main()