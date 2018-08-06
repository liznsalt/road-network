import json
import matplotlib.pyplot as plt
import networkx as nx


def get_point_data():
    with open('Task1/point_data.json', 'r') as f:
        res = json.load(f)
    return res


def creat_graph():
    G = nx.Graph()
    with open('Task1/road_network.txt', 'r') as f:
        for line in f:
            data = line.split()
            if data[0] == 'e':
                _, e1, e2 = data
                G.add_edge(e1, e2)
    return G


def draw(G):
    # 得到点的信息
    pos = get_point_data()
    nx.draw(G,
            pos=pos,
            # node_color='green',
            node_shape='o',
            width=0.0001,
            style='solid',
            with_labels=False,
            # font_size=8,
            # font_weight='bold',
            # alpha=0.5,
            node_size=0.0001
            )
    # plt.show()
    plt.savefig('Task2/graph.png', dpi=300)


if __name__ == '__main__':
    draw(creat_graph())
    print('Done')
