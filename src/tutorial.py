import networkx as nx
import matplotlib.pyplot as plt

list_penerbangan = [("Indonesia", "Singapura"), ("Indonesia", "Jepang"), ("Indonesia", "Uni Emirat Arab"), ("Singapura", "Uni Emirat Arab"), ("Singapura", "Inggris"), 
                    ("Singapura", "Amerika"), ("Jepang", "Singapura"), ("Jepang", "Amerika"), ("Jepang", "Uni Emirat Arab"), ("Jepang", "Inggris"), ("Uni Emirat Arab", "Amerika"),
                    ("Uni Emirat Arab", "Inggris"), ("Amerika", "Inggris")]

J = create_graph(list_penerbangan)
get_degree(J, "Singapura")
dfs_traversal(J, "Indonesia")
bfs_traversal(J, "Indonesia")
find_shortest_path(J, "Indonesia", "Amerika")
visualize_graph(J)
