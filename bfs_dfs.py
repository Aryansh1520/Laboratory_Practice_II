graph = {}
graph_1 = {5: [3, 7], 3: [2, 4], 7: [8], 2: [], 4: [8], 8: []}

nodes = int(input("Enter Number Of Nodes : "))
for i in range (nodes):
    node = int(input("Enter Node : "))
    child_node = list(map(int,input("Enter its Children nodes seperated by space : ").split()))
    graph[node] = child_node

print(graph)


def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited



def dfs(graph, start):
    visited = set()
    def _dfs(node):
        visited.add(node)
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                _dfs(neighbor)
    _dfs(start)

print("BFS")
bfs(graph_1,5)
print("\n")

print("DFS")
dfs(graph_1,5)
