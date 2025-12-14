from itertools import combinations
import heapq

def calc_distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**0.5

def main():
    input_file = "./input.txt"
    with(open(input_file, "r")) as fp:
        lines = map(str.strip, fp.readlines())

    nodes = [tuple(map(int,line.split(","))) for line in lines]
    unconnected_node_set = set(nodes)
    all_edges = combinations(nodes, 2)
    
    # format (weight, p1, p2)
    # heapify will use the first element of a tuple for comparisons
    # This used to be a "sorted" but using cProfile highlighted that all the sortedlist[1:] was killing performance
    # Using sorted and naively chopping the first element was taking 4 minutes.
    # min-heap takes less than a second
    edges_with_weights = [(calc_distance(x[0], x[1]), x[0], x[1]) for x in all_edges]
    heapq.heapify(edges_with_weights)

    # # while there are still unconnected nodes, connect the two closest point
    while len(unconnected_node_set) > 0:
        shortest_length_edge = heapq.heappop(edges_with_weights)
        unconnected_node_set.discard(shortest_length_edge[1])
        unconnected_node_set.discard(shortest_length_edge[2])

    # everything connected
    print(f"answer: {shortest_length_edge[1][0] * shortest_length_edge[2][0]}")

if __name__ == "__main__":
    main()