import networkx as nx
from graph import create_graph, get_degree, dfs_traversal, bfs_traversal, find_shortest_path, visualize_graph

def main():
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 0)]
    G = create_graph(edges)
    node = 3
    degree = get_degree(G, node)
    print(f"Degree dari simpul {node}: {degree}")

    start_node = 0
    dfs_result = dfs_traversal(G, start_node)
    print(f"DFS Traversal dari simpul {start_node}: {dfs_result}")

    bfs_result = bfs_traversal(G, start_node)
    print(f"BFS Traversal dari simpul {start_node}: {bfs_result}")
    
    source, target = 0, 4
    shortest_path = find_shortest_path(G, source, target)
    print(f"Jalur terpendek dari {source} ke {target}: {shortest_path}")

    visualize_graph(G)
    
if __name__ == "__main__":
    main()
