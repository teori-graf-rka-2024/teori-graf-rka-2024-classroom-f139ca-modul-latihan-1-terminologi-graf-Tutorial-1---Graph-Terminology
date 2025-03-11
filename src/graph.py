import networkx as nx
import matplotlib.pyplot as plt

#soal 1
def create_graph(edges):
  G = nx.Graph()
  for edge in edges:
    G.add_edge(edge[0], edge[1])
  return G

#soal 2
def get_degree(graph, node):
  degrees = dict(graph.degree())
  print(degrees[node])

#soal 3
def dfs_traversal(graph, start, visited=set(), result=[]):

    visited.add(start)
    result.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_traversal(graph, neighbor, visited, result)

    return result

#soal 4
def bfs_traversal(graph, start):
    visited = set()
    queue = [start]
    result = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            result.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return result

#soal 5
def find_shortest_path(graph, node1, node2):
  path = nx.shortest_path(graph, source= node1, target= node2)
  print(path)

#soal 6
def visualize_graph(H):
    pos = nx.spring_layout(H)
    edge_labels = nx.get_edge_attributes(H, 'weight')

    nx.draw(H, pos, with_labels=True, node_color='lightblue', edge_color='green', node_size=800)
    nx.draw_networkx_edge_labels(H, pos, edge_labels=edge_labels)
    plt.title("Visualisasi Graf")
    plt.show()
