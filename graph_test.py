import networkx as nx
import matplotlib.pyplot as plt
G=nx.watts_strogatz_graph(10,4,.5)
G1 = nx.random_regular_graph(4, 10)
G2 = nx.gnm_random_graph(10,18)

plt.show()
print('Clustering Watts:',nx.average_clustering(G))
print('Clustering reg',nx.average_clustering(G1))
print('Clustering ran',nx.average_clustering(G2))
print('path Watts:',nx.average_shortest_path_length(G))
print('path reg',nx.average_shortest_path_length(G1))
print('path ran',nx.average_shortest_path_length(G2))