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
                e1 = int(e1)
                e2 = int(e2)
                G.add_edge(e1, e2)
    return G

# TODO: 正确找到点的信息
def draw(G):
    # 得到点的信息
    point_data = get_point_data()
    pos = [point_data[str(node)] for node in point_data.keys()]
    # TODO: color

    nx.draw(G,
            pos=pos,
            node_color='green',
            with_labels=False,
            # font_size=8,
            # font_weight='bold',
            alpha=0.5,
            node_size=10
            )

    # plt.xlim(115, 117)
    # plt.ylim(38, 41)
    plt.show()
    # plt.savefig('Task2/graph.png')

    return None


if __name__ == '__main__':
    draw(creat_graph())
    print('Done')
