graph = {}
nodes = int(input("Enter Number Of Nodes : "))
for i in range (nodes):
    node = str(input("Enter Node : "))
    child_node = list(map(int,input("Enter its Children nodes seperated by space : ").split()))
    graph[node] = child_node
#print(graph.keys())
#print(graph['5'])

def bfs(graph, node):
    visited = set()
    def _bfs(node):
        visited.add(node)
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                _bfs(neighbor)
    _bfs(node)


def dfs(graph,root):
    visited = []
    if root not in visited:
        print(root)
        root = str(root)
        visited.append(root)
        for neighbor in graph[root]:
            dfs(graph,neighbor)
    return

print("BFS")
dfs(graph,'5')

