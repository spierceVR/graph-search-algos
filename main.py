# import heapq for priority queue
import fileinput
from heapq import heappush, heappop

# Get edges from file
edges: dict[tuple[str, str], int] = {}
for edge in fileinput.input(files="edges.txt"):
    edge = edge.split()
    edges[(edge[0], edge[1])] = int(edge[2])

start: str = "start"
end: str = "goal"

# get heuristic values from file
heuristic: dict[str, int] = {}
for h in fileinput.input(files="heuristic.txt"):
    h = h.split()
    heuristic[h[0]] = int(h[1])


def total_cost(path: list[str], edges: dict[tuple[str, str], int]) -> int:
    """calculate total cost of path given a path and dictionary of edges"""
    cost = 0
    for i in range(len(path) - 1):
        cost += edges[(path[i], path[i + 1])]
    return cost

# uniform cost search


def uniform_cost_search(edges: dict[tuple[str, str], int], start: str, end: str) -> tuple[list, int]:
    # initialize queue
    queue = [(0, start, [])]
    # initialize visited nodes
    visited = set()
    # loop until queue is empty
    print("[UCS] Expanding nodes in order of cost")
    nodes_expanded = 0
    while queue:
        # get next node
        (cost, node, path) = heappop(queue)
        # check if node has been visited
        if node in visited:
            continue
        nodes_expanded += 1
        print("expanding node: " + node + "\twith cost: " + str(cost))
        # add node to visited
        visited.add(node)
        # check if node is end node
        if node == end:
            # return path
            return (path + [node], nodes_expanded)
        # add neighbors to queue
        print("successors of the node are:")
        for (edge, edge_cost) in edges.items():
            if edge[0] == node and edge[1] not in visited:
                g = cost + edge_cost
                heappush(queue, (g, edge[1], path + [node]))
                print(f"{edge[1]} with: g({edge[1]}) = {g}")
        print()
    # return empty path if no path found
    return ([], nodes_expanded)


# greedy best first search


def greedy_best_first(edges: dict[tuple[str, str], int], start: str, end: str, heuristic: dict[str, int]) -> tuple[list, int]:
    # initialize queue
    queue = [(0, start, [])]
    # initialize visited nodes
    visited = set()
    # loop until queue is empty
    print("[GBFS] Expanding nodes in order of heuristic")
    nodes_expanded = 0
    while queue:
        # get next node
        (cost, node, path) = heappop(queue)
        # check if node has been visited
        if node in visited:
            continue
        nodes_expanded += 1
        print("expanding node: " + node + "\twith heuristic: " + str(cost))
        # add node to visited
        visited.add(node)
        # check if node is end node
        if node == end:
            # return path
            return (path + [node], nodes_expanded)
        # add neighbors to queue
        print("successors of the node are:")
        for (edge, edge_cost) in edges.items():
            if edge[0] == node and edge[1] not in visited:
                h = heuristic[edge[1]]
                heappush(queue, (h, edge[1], path + [node]))
                print(f"{edge[1]} with: h({edge[1]}) = {h}")
        print()
    # return empty path if no path found
    return ([], nodes_expanded)

# a* search


def a_star(edges: dict[tuple[str, str], int], start: str, end: str, heuristic: dict[str, int]) -> tuple[list, int]:
    # initialize queue
    queue = [(0, start, [])]
    # initialize visited nodes
    visited = set()
    # loop until queue is empty
    nodes_expanded = 0
    print("[A*] Expanding nodes in order of cost + heuristic")
    while queue:
        # get next node
        (cost, node, path) = heappop(queue)
        # check if node has been visited
        if node in visited:
            continue
        nodes_expanded += 1
        print("expanding node: " + node +
                "\twith cost+heuristic: " + str(cost))
        # add node to visited
        visited.add(node)
        # check if node is end node
        if node == end:
            # return path
            return (path + [node], nodes_expanded)
        # add neighbors to queue
        print("successors of the node are:")
        for (edge, edge_cost) in edges.items():
            if edge[0] == node and edge[1] not in visited:
                g = total_cost(path + [node], edges) + edge_cost
                h = heuristic[edge[1]]
                heappush(queue, (g + h, edge[1], path + [node]))
                print(
                    f"{edge[1]} with: g({edge[1]}) = {g}, \t h({edge[1]}) = {h}, \t f({edge[1]}) = {g+h}")
        print()
    # return empty path if no path found
    return ([], nodes_expanded)


# run search algorithms
(UCS_path, UCS_nodes_expanded) = uniform_cost_search(edges, start, end)
print("------------------------------------")
(Greedy_path, Greedy_nodes_expanded) = greedy_best_first(
    edges, start, end, heuristic)
print("------------------------------------")
(A_star_path, A_star_nodes_expanded) = a_star(edges, start, end, heuristic)

# print solution paths and their total costs and nodes expanded
print("------------------------------------")
print("UCS Solution Path:\t" + str(UCS_path))
print("Cost:\t" + str(total_cost(UCS_path, edges)))
print("Nodes Expanded:\t" + str(UCS_nodes_expanded))

print("GBFS Solution Path:\t" + str(Greedy_path))
print("Cost:\t" + str(total_cost(Greedy_path, edges)))
print("Nodes Expanded:\t" + str(Greedy_nodes_expanded))

print("A* Solution Path:\t" + str(A_star_path))
print("Cost:\t" + str(total_cost(A_star_path, edges)))
print("Nodes Expanded:\t" + str(A_star_nodes_expanded))
