from heapq import heappop, heappush


state: list[int] = [3, 3, 0]
actions: list[str] = ['1,0', '2,0', '0,1', '0,2', '1,1']


def goal_test(state: list[int]):
    return state == [0, 0, 1]


def is_valid(state: list[int]):
    if state[0] < 0 or state[1] < 0 or state[0] > 3 or state[1] > 3:
        return False
    elif state[0] > 0 and state[0] < state[1]:
        return False
    elif state[0] < 3 and state[0] > state[1]:
        return False
    else:
        return True


def heuristic(state: list[int]):
    return state[0] + state[1]


def uniform_cost_search(state: list[int], actions: list[str]):
    queue = [(0, state, [])]
    nodes_expanded = 0
    while queue:
        (cost, node, path) = heappop(queue)
        nodes_expanded += 1
        print("expanding node: " + str(node) + "\twith cost: " + str(cost))
        if goal_test(node):
            return (path + [node], nodes_expanded)
        for action in actions:
            action = action.split(',')
            action = [int(action[0]), int(action[1])]
            new_state = [node[0] - action[0], node[1] - action[1], node[2]]
            if node[2] == 0:
                new_state[0] += action[0]
                new_state[1] += action[1]
                new_state[2] = 1
            else:
                new_state[2] = 0
            if is_valid(new_state):
                g = cost + 1
                heappush(queue, (g, new_state, path + [node]))
                print(f"{new_state} with: g({new_state}) = {g}")
        print()


def greedy_best_first_search(state: list[int], actions: list[str]):
    queue = [(0, state, [])]
    nodes_expanded = 0
    while queue:
        (cost, node, path) = heappop(queue)
        nodes_expanded += 1
        print("expanding node: " + str(node) +
              "\twith heuristic: " + str(cost))
        if goal_test(node):
            return (path + [node], nodes_expanded)
        for action in actions:
            action = action.split(',')
            action = [int(action[0]), int(action[1])]
            new_state = [node[0] - action[0], node[1] - action[1], node[2]]
            if node[2] == 0:
                new_state[0] += action[0]
                new_state[1] += action[1]
                new_state[2] = 1
            else:
                new_state[2] = 0
            if is_valid(new_state):
                h = heuristic(new_state)
                heappush(queue, (h, new_state, path + [node]))
                print(f"{new_state} with: h({new_state}) = {h}")
        print()


def depth_first_search(state: list[int], actions: list[str]):
    stack = [(state, [])]
    nodes_expanded = 0
    while stack:
        (node, path) = stack.pop()
        nodes_expanded += 1
        print("expanding node: " + str(node))
        if goal_test(node):
            return (path + [node], nodes_expanded)
        for action in actions:
            action = action.split(',')
            action = [int(action[0]), int(action[1])]
            new_state = [node[0] - action[0], node[1] - action[1], node[2]]
            if node[2] == 0:
                new_state[0] += action[0]
                new_state[1] += action[1]
                new_state[2] = 1
            else:
                new_state[2] = 0
            if is_valid(new_state):
                stack.append((new_state, path + [node]))
                print(f"{new_state} added to stack")
        print()


(UCS_path, nodes_expanded) = uniform_cost_search(state, actions)
(greedy_path, greedy_nodes_expanded) = greedy_best_first_search(state, actions)
(depth_path, depth_nodes_expanded) = depth_first_search(state, actions)

print(UCS_path)
print(nodes_expanded)
print(greedy_path)
print(greedy_nodes_expanded)
print(depth_path)
print(depth_nodes_expanded)
