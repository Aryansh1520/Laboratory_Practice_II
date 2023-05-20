import math

class Node:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def heuristic(node, goal):
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def a_star(maze, start, goal):
    open_set = set([start])
    closed_set = set()

    while open_set:
        current = min(open_set, key=lambda node: node.cost + heuristic(node, goal))
        open_set.remove(current)
        closed_set.add(current)

        if current == goal:
            return current.cost

        for neighbor in maze[current.x][current.y]:
            if neighbor not in closed_set:
                neighbor.cost = current.cost + neighbor.cost
                open_set.add(neighbor)

    return None

def main():
    maze = [[
        [Node(0, 0, 0), Node(1, 0, 1), Node(2, 0, 2)],
        [Node(0, 1, 3), Node(1, 1, 4), Node(2, 1, 5)],
        [Node(0, 2, 6), Node(1, 2, 7), Node(2, 2, 8)],
    ]]

    start = Node(0, 0, 0)
    goal = Node(2, 2, 0)

    cost = a_star(maze, start, goal)

    print("The cost of the shortest path is", cost)

if __name__ == "__main__":
    main()
