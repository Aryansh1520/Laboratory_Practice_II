graph = {}
#graph_1 = {5: [3, 7], 3: [2, 4], 7: [8], 2: [], 4: [8], 8: []}

nodes = int(input("Enter Number Of Nodes : "))
for i in range (nodes):
    node = int(input("Enter Node : "))
    child_node = list(map(int,input("Enter its Children nodes seperated by space : ").split()))
    graph[node] = child_node

print(graph)
visited = []

def bfs(visited, Q):
    if not Q:                 
        return
    node=Q.pop(0)  
    print(node, end=' ')
    for i in graph[node]:           
        if i not in visited:
            Q.append(i)
            visited.append(i)
    bfs(visited, Q)

def dfs(visited,s):
    if not s:                 
        return
    node=s.pop(0)  
    print(node, end=' ')
    for i in graph[node]:           
        if i not in visited:
            s.append(i)
            visited.append(i)
        dfs(visited, s)

print("BFS")
q=[5]
bfs(visited,q)

visited = []
s=[5]
print("\nDFS\n")
dfs(visited,s)
print("\n")
