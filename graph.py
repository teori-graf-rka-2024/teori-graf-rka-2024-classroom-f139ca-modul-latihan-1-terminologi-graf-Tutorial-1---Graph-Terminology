import networkx as nx 
import matplotlib.pyplot as plt

def create_graph(edges: list[tuple[int, int]]) -> nx.Graph : 
    G= nx.Graph ()
    G.add_edges_from(edges)
    return G
def get_degree(G: nx.Graph, node: int) -> int: 
    return G.degree[node]
def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    return list(nx.dfs_preorder_nodes (G,start,depth_limit=5))
def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    return list(nx.bfs_layers(G,start))
def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    return list(nx.shortest_path(G,source,target))
def visualize_graph(G: nx.Graph): 
    nx.draw(G)
    plt.figure(figsize=(6, 6))
    titik = nx.spring_layout(G) 
    nx.draw(G, titik, with_labels=True, node_color="yellow", edge_color="black", node_size=400, font_size=11)
    plt.savefig("visualisasi_graph.png")
    plt.show()
    