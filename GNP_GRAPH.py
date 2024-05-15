import networkx as nx
import random
import matplotlib.pyplot as plt


def random_coloring(G, num_colors):
    colors = {}
    for node in G.nodes():
        colors[node] = random.randint(0, num_colors - 1)
    return colors

def count_conflicts(G, colors):
    conflicts = 0
    for edge in G.edges():
        if colors[edge[0]] == colors[edge[1]]:
            conflicts += 1
    return conflicts

def visualize_graph(G, colors):
    node_color_list = [colors[node] for node in G.nodes()]
    nx.draw(G, with_labels=True, node_color=node_color_list, cmap=plt.cm.rainbow)
    plt.show()

def greedy_coloring(G, num_colors):
    colors = {}
    for node in G.nodes():
        available_colors = set(range(num_colors))
        for neighbor in G.neighbors(node):
            if neighbor in colors:
                available_colors.discard(colors[neighbor])
        if available_colors:
            colors[node] = min(available_colors)
        else:
            raise ValueError("No available colors for node {}".format(node))
    return colors
def main():
    num_nodes = 10
    edge_prob = .5
    num_colors = 4
    num_edges = 16

    G = nx.gnp_random_graph(num_nodes,edge_prob)
    colors = random_coloring(G, num_colors)
    initial_conflicts = count_conflicts(G, colors)
    conflicts_after=count_conflicts(G,colors)
    print("Initial coloring conflicts (Gnm Graph):", initial_conflicts)


    return initial_conflicts,G,colors
    # Perform experiments here, e.g., using a simple greedy coloring algorithm
    # and count conflicts over time


if __name__ == "__main__":
    conflicts=[]
    experi=[]
    counter = 0
    iterations=0
    num_noConflict = 0;
    while counter<=150:
        initial,G,colours,=main()
        conflicts.append(initial)
        experi.append((len(conflicts)))
        print('Iteration number:',counter)
        counter+=1
        if(initial==0):
            num_noConflict+=1


    print('Number of Graphs with no Conflicts:', num_noConflict)
    print('Total Number of Conflicts:', sum(conflicts))
    plt.plot(experi,conflicts,linewidth=.5,marker='.',markersize=4)
    plt.xlabel('Number of Experiments')
    plt.ylabel('Number of Conflicts')
    plt.title('Number of Conflicts vs Number of Experiments')
    plt.show()