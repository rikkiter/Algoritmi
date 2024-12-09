# graph = {"start": {"a": 2, "b": 5}, "a": {"b": 8, "d": 7},"b": {"c": 4, "d": 2},
#          "c": {"end": 3, "d": 6}, "d": {"end": 1}, "end": {}}
# infinity = float("inf")
# costs = {"a": 2, "b": 5, "c": infinity, "d": infinity, "end": infinity}
# parents = {"a": "start", "b": "start", "c": "b", "d": None, "end": None}
# processed = []

# graph = {"start": {"a": 10}, "a": {"b": 20}, "b": {"c": 1, "end": 30},
#          "c": {"a": 1}, "end": {}}
# infinity = float("inf")
# costs = {"a": 10, "b": infinity, "c": infinity, "end": infinity}
# parents = {"a": None, "b": "a", "c": "b", "end": "b"}
# processed = []

graph = {"start": {"a": 2, "b": 2}, "a": {"c": 2, "end": 2}, "b": {"a": 2},
         "c": {"b": -1, "end": 2}, "end": {}}
infinity = float("inf")
costs = {"a": 2, "b": 2, "c": infinity, "end": infinity}
parents = {"a": None, "b": None, "c": "a", "end": None}
processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs["end"])