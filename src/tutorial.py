import networkx as nx
import matplotlib.pyplot as plt
import src.graph as g

list_penerbangan = [("Indonesia", "Singapura"), ("Indonesia", "Jepang"), ("Indonesia", "Uni Emirat Arab"), ("Singapura", "Uni Emirat Arab"), ("Singapura", "Inggris"), 
                    ("Singapura", "Amerika"), ("Jepang", "Singapura"), ("Jepang", "Amerika"), ("Jepang", "Uni Emirat Arab"), ("Jepang", "Inggris"), ("Uni Emirat Arab", "Amerika"),
                    ("Uni Emirat Arab", "Inggris"), ("Amerika", "Inggris")]

J = g.create_graph(list_penerbangan)
g.get_degree(J, "Singapura")
g.dfs_traversal(J, "Indonesia")
g.bfs_traversal(J, "Indonesia")
g.find_shortest_path(J, "Indonesia", "Amerika")
g.visualize_graph(J)
