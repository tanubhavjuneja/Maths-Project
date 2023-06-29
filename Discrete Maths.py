import heapq
import networkx as nx
import matplotlib.pyplot as plt
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]
    def add_edge(self, u, v, weight):
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))
    def dijkstra(self, source):
        distance = [float('inf')] * self.vertices
        distance[source] = 0
        heap = [(0, source)]
        heapq.heapify(heap)
        while heap:
            dist, node = heapq.heappop(heap)
            if dist > distance[node]:
                continue
            for neighbor, weight in self.adjacency_list[node]:
                new_dist = dist + weight
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))
        return distance
    def second_best_path(self, source, destination):
        distance = self.dijkstra(source)
        shortest_path_distance = distance[destination]
        removed_edges = set()
        for node in range(self.vertices):
            for neighbor, weight in self.adjacency_list[node]:
                if distance[node] + weight + distance[neighbor] == shortest_path_distance:
                    removed_edges.add((node, neighbor))
                    removed_edges.add((neighbor, node))
        second_best_distance = float('inf')
        second_best_path = []
        for u, v, weight in self.get_edges():
            if (u, v) in removed_edges or (v, u) in removed_edges:
                continue
            self.remove_edge(u, v)
            self.remove_edge(v, u)
            distance = self.dijkstra(source)
            if distance[destination] < second_best_distance:
                second_best_distance = distance[destination]
                second_best_path = distance.copy()
            self.add_edge(u, v, weight)
            self.add_edge(v, u, weight)
        return second_best_distance, second_best_path
    def get_edges(self):
        edges = []
        for node in range(self.vertices):
            for neighbor, weight in self.adjacency_list[node]:
                if (node, neighbor, weight) not in edges and (neighbor, node, weight) not in edges:
                    edges.append((node, neighbor, weight))
        return edges
    def remove_edge(self, u, v):
        self.adjacency_list[u] = [(neighbor, weight) for neighbor, weight in self.adjacency_list[u] if neighbor != v]
    def __str__(self):
        graph_string = ""
        for node in range(self.vertices):
            graph_string += f"Node {node}: "
            for neighbor, weight in self.adjacency_list[node]:
                graph_string += f"(Neighbor: {neighbor}, Weight: {weight}) "
            graph_string += "\n"
        return graph_string
graph = Graph(31)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 2, 2)
graph.add_edge(1, 3, 6)
graph.add_edge(2, 3, 7)
graph.add_edge(0, 4, 2)
graph.add_edge(0, 5, 4)
graph.add_edge(1, 4, 6)
graph.add_edge(1, 5, 3)
graph.add_edge(2, 5, 1)
graph.add_edge(2, 6, 5)
graph.add_edge(3, 6, 8)
graph.add_edge(3, 7, 7)
graph.add_edge(4, 7, 3)
graph.add_edge(4, 8, 2)
graph.add_edge(5, 8, 6)
graph.add_edge(5, 9, 5)
graph.add_edge(6, 9, 4)
graph.add_edge(6, 10, 3)
graph.add_edge(7, 10, 7)
graph.add_edge(7, 11, 4)
graph.add_edge(8, 11, 6)
graph.add_edge(8, 12, 8)
graph.add_edge(9, 12, 5)
graph.add_edge(9, 13, 2)
graph.add_edge(10, 13, 4)
graph.add_edge(10, 14, 3)
graph.add_edge(11, 14, 7)
graph.add_edge(11, 15, 5)
graph.add_edge(12, 15, 6)
graph.add_edge(12, 16, 8)
graph.add_edge(13, 16, 4)
graph.add_edge(13, 17, 6)
graph.add_edge(14, 17, 3)
graph.add_edge(14, 18, 5)
graph.add_edge(15, 18, 7)
graph.add_edge(15, 19, 4)
graph.add_edge(16, 19, 6)
graph.add_edge(16, 20, 5)
graph.add_edge(17, 20, 4)
graph.add_edge(17, 21, 3)
graph.add_edge(18, 21, 7)
graph.add_edge(18, 22, 6)
graph.add_edge(19, 22, 8)
graph.add_edge(19, 23, 5)
graph.add_edge(20, 23, 4)
graph.add_edge(20, 24, 6)
graph.add_edge(21, 24, 3)
graph.add_edge(21, 25, 2)
graph.add_edge(22, 25, 7)
graph.add_edge(22, 26, 4)
graph.add_edge(23, 26, 6)
graph.add_edge(23, 27, 5)
graph.add_edge(24, 27, 8)
graph.add_edge(24, 28, 4)
graph.add_edge(25, 28, 6)
graph.add_edge(25, 29, 3)
graph.add_edge(26, 29, 7)
graph.add_edge(26, 30, 5)
print("Graph:")
print(graph)
source_vertex = 0
destination_vertex = 3
shortest_path_distance = graph.dijkstra(source_vertex)[destination_vertex]
print(f"Shortest path distance: {shortest_path_distance}")
second_best_distance, second_best_path = graph.second_best_path(source_vertex, destination_vertex)
print(f"Second-best path distance: {second_best_distance}")
print(f"Second-best path: {second_best_path}")
nx_graph = nx.Graph()
for node in range(graph.vertices):
    for neighbor, weight in graph.adjacency_list[node]:
        nx_graph.add_edge(node, neighbor, weight=weight)
pos = nx.spring_layout(nx_graph)
nx.draw(nx_graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray', width=1, alpha=0.7)
plt.savefig("graph_image.png")
plt.show()