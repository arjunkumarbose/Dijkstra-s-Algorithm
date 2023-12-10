from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def dijkstra(self, src):
        # Initialize distances with infinity and source vertex with 0
        distances = {v: float('inf') for v in self.graph}
        distances[src] = 0

        # Set to keep track of visited vertices
        visited = set()

        while len(visited) != len(self.graph):
            # Find the vertex with the minimum distance
            min_vertex = min((v for v in self.graph if v not in visited), key=distances.get)

            # Mark the minimum vertex as visited
            visited.add(min_vertex)

            # Update distances for adjacent vertices
            for v in self.graph[min_vertex]:
                if v not in visited:
                    distances[v] = min(distances[v], distances[min_vertex] + self.graph[min_vertex][v])

        return distances

# Creating the graph
g = Graph()
print("Enter edges for the graph with weights (format: 'source destination weight'). Enter '#' to stop:")

while True:
    edge = input()
    if edge == '#':
        break
    u, v, weight = map(int, edge.split())
    g.add_edge(u, v, weight)

source_vertex = int(input("Enter the source vertex to find shortest paths from: "))

shortest_distances = g.dijkstra(source_vertex)

print("\nShortest distances from vertex {}:".format(source_vertex))
for vertex, distance in shortest_distances.items():
    print("Vertex {}: Distance from source = {}".format(vertex, distance))
