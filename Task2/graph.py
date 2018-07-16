import matplotlib.pyplot as plt
import networkx as nx


def creat_graph():
    G = nx.Graph()
    with open('Task1/result.txt') as f:
        for line in f:
            data = line.split()
            if data[0] == 'e':
                _, e1, e2 = data
                G.add_edge(e1, e2)
    return G


def draw(G):
    nx.draw(G,
            node_color='green',
            with_labels=False,
            # font_size=8,
            # font_weight='bold',
            alpha=0.5,
            node_size=10)
    plt.show()
    # plt.savefig('Task2/graph.png')
    return None


if __name__ == '__main__':
    draw(creat_graph())
    print('Done')
