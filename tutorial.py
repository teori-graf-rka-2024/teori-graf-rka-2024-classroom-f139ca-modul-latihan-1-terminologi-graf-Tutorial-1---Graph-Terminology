from graph import *
edges = {(1,4),(1,3),(2,4),(2,5),(2,3),(3,1),(3,2),(3,4),(3,5),(4,1),(4,2),(4,3),(5,2),(5,3)}

G = create_graph(edges)

for nodes in G.nodes : 
    print ("degree : ",(get_degree(G,nodes)))

print ("inii bfs ",(bfs_traversal(G,1)))
print ("nahh klo ini dfsnyaa", (dfs_traversal(G,1)))
print(find_shortest_path(G,1,5))

visualize_graph(G)