from heapq import heappop, heappush

# cats, mice, boat
state: tuple[int] = (3, 3, 0)


def goal_test(state: tuple[int, int, int]):
    return state == (0, 0, 1)


def heuristic(state: tuple[int]):
    return state[0] + state[1]


def valid_actions(state) -> list[str]:
    actions: list[str] = ['1,0', '2,0', '0,1', '0,2', '1,1']
    valid_actions = []
    if state[2] == 0:
        for action in actions:
            # if there are enough cats and mice on the left side to take this action
            if int(action[0]) <= state[0] and int(action[2]) <= state[1]:
                valid_actions.append(action)
    else:
        for action in actions:
            # if there are enough cats and mice on the right side to take this action
            if int(action[0]) <= 3 - state[0] and int(action[2]) <= 3 - state[1]:
                valid_actions.append(action)
    return valid_actions


def valid_states(state) -> list[tuple[int]]:
    valid_states = []
    actions = valid_actions(state)
    if actions == None:
        return []
    for action in actions:
        if state[2] == 0:
            valid_states.append(
                (state[0] - int(action[0]), state[1] - int(action[2]), 1))
        else:
            valid_states.append(
                (state[0] + int(action[0]), state[1] + int(action[2]), 0))
    return [x for x in valid_states if valid_combination(x)]


def valid_combination(state) -> bool:
    if state[0] > 0 and state[1] > 0:
        if state[0] > state[1]:
            return False  # mice outnumbered by cats on the left side
    cats_right = 3 - state[0]
    mice_right = 3 - state[1]
    if cats_right > 0 and mice_right > 0:
        if cats_right > mice_right:
            return False  # mice outnumbered by cats on the right side
    if state[0] < 0 or state[1] < 0:
        return False  # negative number of cats or mice
    if state[0] > 3 or state[1] > 3:
        return False  # more cats or mice than allowed
    return True


def uniform_cost_search(state: tuple[int]) -> tuple[list[tuple[int]], int] or None:
    queue = [(0, state, [])]
    nodes_expanded = 0
    seen = set()
    while queue:
        (cost, node, path) = heappop(queue)
        nodes_expanded += 1
        print("expanding node: " + str(node) + "\twith cost: " + str(cost))
        if goal_test(node):
            print(f"node {node} is the goal")
            return (path + [node], nodes_expanded)
        successors = valid_states(node)
        print("successors are:")
        for new_state in successors:
            if new_state in seen:
                continue
            seen.add(new_state)
            g = cost + 1
            heappush(queue, (g, new_state, path + [node]))
            print(f"{new_state} with: g({new_state}) = {g}")
        print()
    return (None, nodes_expanded)



(UCS_path, nodes_expanded) = uniform_cost_search(state)
# (greedy_path, greedy_nodes_expanded) = greedy_best_first_search(state, actions)
# (depth_path, depth_nodes_expanded) = depth_first_search(state, actions)

print(UCS_path)
print(nodes_expanded)
# print(greedy_path)
# print(greedy_nodes_expanded)
# print(depth_path)
# print(depth_nodes_expanded)