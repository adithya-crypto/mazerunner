import os
from Display import Plot
from Algos import bfs, dfs, aStar
from Imagetostructure import image, TreeGeneration


def Start(choice, algo):
    display = False
    load = "maze" + choice + ".jpg"
    skel, img = image(load)
    T, tree = TreeGeneration(skel)
    # Default
    Start = 133
    End = 73
    if choice == "3":
        Start = 133
        End = 73
    elif choice == "2":
        Start = 101
        End = 4
        display = True
    elif choice == "1":
        Start = 3
        End = 20
        display = True
    if algo == "1":
        path, steps = bfs(
            Start,
            End,
            T,
            display,
        )
        Plot(img, tree, path, Start, End, steps, algo)
    elif algo == "2":
        path, steps = dfs(Start, End, T, display)
        Plot(img, tree, path, Start, End, steps, algo)
    elif algo == "3":
        path, steps = aStar(Start, End, T, display)
        Plot(img, tree, path, Start, End, steps, algo)


def menu():
    print("Select maze")
    print("Press 1 for easy")
    print("Press 2 for Medium")
    print("Press 3 for Hard")
    choice = input()
    if choice == "1" or choice == "2" or choice == "3":
        print("Select Algo")
        print("Press 1 for Bfs")
        print("Press 2 for Dfs")
        print("Press 3 for A*")
        algo = input()
        if algo == "1" or algo == "2" or algo == "3":
            os.system("clear")
            Start(choice, algo)
        else:
            print("Wrong Algo choice")
    else:
        print("Wrong Maze choice")


if __name__ == "__main__":
    menu()
