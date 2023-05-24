import sys

def min_key(key, mst_set, V):
    min_val = sys.maxsize
    min_idx = -1
    for v in range(V):
        if key[v] < min_val and not mst_set[v]:
            min_val = key[v]
            min_idx = v
    return min_idx

def print_mst(parent, graph, V):
    print("Edge   Weight")
    for i in range(1, V):
        print(parent[i], "-", i, "   ", graph[i][parent[i]])

def prim_mst(graph, V):
    print(V)
    key = [sys.maxsize] * V
    parent = [None] * V
    key[0] = 0
    mst_set = [False] * V
    parent[0] = -1

    for _ in range(V):
        u = min_key(key, mst_set, V)
        mst_set[u] = True

        for v in range(V):
            if graph[u][v] > 0 and not mst_set[v] and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    print_mst(parent, graph, V)


# Driver code
V = int(input("Enter the number of vertices: "))

graph = []

print("Enter the adjacency matrix (space-separated):")
for i in range(V):
    row = list(map(int, input().split()))
    graph.append(row)

print(graph)
prim_mst(graph, V)
