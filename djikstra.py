import sys

def dijkstra(graph, source):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    distance = [sys.maxsize] * num_vertices
    distance[source] = 0

    for _ in range(num_vertices):
        u = min_distance(distance, visited)
        visited[u] = True

        for v in range(num_vertices):
            if not visited[v] and graph[u][v] > 0 and distance[u] + graph[u][v] < distance[v]:
                distance[v] = distance[u] + graph[u][v]

    return distance


def min_distance(distance, visited):
    min_val = sys.maxsize
    min_idx = -1

    for v in range(len(distance)):
        if not visited[v] and distance[v] < min_val:
            min_val = distance[v]
            min_idx = v

    return min_idx


# Driver code
num_vertices = int(input("Enter the number of vertices: "))
source = int(input("Enter the source vertex: "))

graph = []
print("Enter the adjacency matrix (space-separated):")
for _ in range(num_vertices):
    row = list(map(int, input().split()))
    graph.append(row)

distances = dijkstra(graph, source)

print("Vertex\tDistance")
for v in range(num_vertices):
    print(v, "\t\t", distances[v])
