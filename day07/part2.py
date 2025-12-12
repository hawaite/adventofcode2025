from networkx import DiGraph
import networkx as nx

def count_root_to_leaves(dag, root):
    # in this context, topological sort just sorts by row then column for us.
    topology = list(nx.topological_sort(dag))
    print(f"topology: {topology}")
    counts = {n: 0 for n in dag.nodes()}
    counts[root] = 1
    for current_node in topology:
        count_current_node = counts[current_node]
        if count_current_node == 0:
            continue
        for next_node in dag.successors(current_node):
            counts[next_node] += count_current_node
    leaves = [n for n, d in dag.out_degree() if d == 0]
    total = sum(counts[n] for n in leaves)
    return total, {n: counts[n] for n in leaves}

def main():
    with(open("./input.txt", "r")) as fp:
        lines = fp.readlines()

    processed = []
    for line_ix, line in enumerate(lines):
        line_as_list = list(line.strip())
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
    
    print(f"total: {count_root_to_leaves(graph, root)}")



if __name__ == "__main__":
    main()