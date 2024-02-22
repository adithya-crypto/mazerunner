from queue import PriorityQueue
from Display import display_steps


def bfs(Start, End, T, display):
    step = 0
    Visited = {node: False for node in T.nodes}
    Queue = [Start]
    Visited[Start] = True
    bpath = {}
    while Queue:
        step += 1
        current_node = Queue.pop(0)
        if current_node == End:
            break
        for node in T.neighbors(current_node):
            if not Visited[node]:
                Queue.append(node)
                Visited[node] = True
                bpath[node] = current_node
                if display:
                    display_steps(Queue, Visited, "B")
    return bpath, step


def dfs(Start, End, T, display):
    step = 0
    Visited = {node: False for node in T.nodes}
    Stack = [Start]
    Visited[Start] = True
    dpath = {}
    while Stack:
        step += 1
        current_node = Stack.pop()
        if current_node == End:
            break
        for node in T.neighbors(current_node):
            if not Visited[node]:
                Stack.append(node)
                Visited[node] = True
                dpath[node] = current_node
                if display:
                    display_steps(Stack, Visited, "D")
    return dpath, step


def h(node1, node2):
    x1 = node1["pts"][0][0]
    y1 = node1["pts"][0][1]
    x2 = node2["pts"][0][0]
    y2 = node2["pts"][0][1]
    # Distance
    return abs(x1 - x2) + abs(y1 - y2)


def aStar(Start, End, T, display):
    step = 0
    g = {}
    f = {}
    for node in T.nodes:
        g[node] = float("inf")

    for node in T.nodes:
        f[node] = float("inf")

    if Start not in T.nodes or End not in T.nodes:
        print("Start or End node not found in the graph.")
        return None, None

    f[Start] = h(T.nodes[Start], T.nodes[End])
    g[Start] = 0

    P_Queue = PriorityQueue()
    P_Queue.put(
        (h(T.nodes[Start], T.nodes[End]), h(T.nodes[Start], T.nodes[End]), Start)
    )
    path = {}
    while not P_Queue.empty():
        step += 1
        current_node = P_Queue.get()[2]
        if current_node == End:
            break
        for children in T.neighbors(current_node):
            temp_g = g[current_node] + 1
            temp_f = temp_g + h(T.nodes[children], T.nodes[End])

            if temp_f < f[children]:
                g[children] = temp_g
                f[children] = temp_f
                P_Queue.put((temp_f, h(T.nodes[children], T.nodes[End]), children))
                path[children] = current_node
                if display:
                    display_steps(current_node, P_Queue.queue, "E")
    return path, step
