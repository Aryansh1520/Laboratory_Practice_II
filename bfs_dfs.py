graph = {}
nodes = int(input("Enter Number Of Nodes : "))
for i in range (nodes):
    node = str(input("Enter Node : "))
    child_node = list(map(int,input("Enter its Children nodes seperated by space : ").split()))
    graph[node] = child_node
#print(graph.keys())
#print(graph['5'])

def bfs(graph,node):#root node
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)
    while queue:
        m = str(queue.pop(0))
        print(m,end=" ")
        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


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

