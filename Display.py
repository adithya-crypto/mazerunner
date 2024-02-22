import numpy as np
import matplotlib.pylab as plt


def SetCreator(path, Start, End):
    fpath = {}
    current_node = End
    while current_node != Start:
        if current_node in path:
            fpath[path[current_node]] = current_node
            current_node = path[current_node]
        else:
            # Handle the case where the key doesn't exist in the path dictionary
            print("Error: Key not found in path dictionary")
            return None

    # Add the start node to the path
    fpath[Start] = Start

    fpath = list(fpath.values())
    fpath.append(Start)
    set1 = [(x, y) for x, y in zip(fpath, fpath[1:])]
    fpath.reverse()
    set2 = [(x, y) for x, y in zip(fpath, fpath[1:])]
    set1.extend(set2)
    fpath.reverse()
    return set1


def Plot(img, tree, path, Start, End, steps, algo):
    algo_string = ""
    if algo == "1":
        algo_string = "BFS"
    if algo == "2":
        algo_string = "DFS"
    if algo == "3":
        algo_string = "A*"

    if path is None:
        print("Error: Path not found")
        return

    total_step = str(steps)
    set = SetCreator(path, Start, End)
    if set is None:
        print("Error: Set creation failed")
        return

    plt.imshow(img, cmap="gray")
    for s, e in set:
        ps = tree[s][e]["pts"]
        plt.plot(ps[:, 1], ps[:, 0], "red")
    plt.title("Final output " + "Algorithm: " + algo_string + " Steps " + total_step)
    plt.show()


def display_steps(A1, A2, C):
    if C == "B":
        print(
            "**********************************************************************************"
        )
        print("Current Elemenet in Queue: ", A1)
        print("Visited Nodes: ", A2)
        print(
            "**********************************************************************************"
        )
    elif C == "D":
        print(
            "**********************************************************************************"
        )
        print("Current Elemenet in Stack: ", A1)
        print("Visited Nodes: ", A2)
        print(
            "**********************************************************************************"
        )

    else:
        print(
            "**********************************************************************************"
        )
        print("Current node: ", A1)
        print("Current Queue Status:", A2)
        print(
            "**********************************************************************************"
        )
