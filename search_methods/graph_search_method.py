from collections import deque


# Depth First Search (DFS)


def depth_first_search(start_node, target_node, graph):

    stack = [start_node]
    visited = []

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            visited.append(current_node)

            if current_node == target_node:
                print("Target found:", current_node)
                return visited

            neighbours = graph[current_node]

            for new_node in neighbours:
                stack.append(new_node)

    print("Target not found")
    return visited


# Graph definition
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

# Start and target nodes
start_node = "A"
target_node = "E"

result = depth_first_search(start_node, target_node, graph)
print("Visited nodes:", result)


# Breadth First Search (BFS)

def breadth_first_search(start_node, target_node, graph):

    queue = deque([start_node])
    visited = []

    while queue:
        current_node = queue.popleft()

        if current_node not in visited:
            visited.append(current_node)

            if current_node == target_node:
                print("Target found:", current_node)
                return visited

            neighbours = graph[current_node]

            for new_node in neighbours:
                queue.append(new_node)

    print("Target not found")
    return visited


# Graph definition
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

# Start and target
start_node = "A"
target_node = "E"

result = breadth_first_search(start_node, target_node, graph)

print("Visited nodes:", result)