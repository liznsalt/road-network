import json
import matplotlib.pyplot as plt
import networkx as nx


def get_point_data():
    with open('Task3/nodes.json', 'r') as f:
        res = json.load(f)
    return res


def creat_graph():
    G = nx.Graph()
    with open('Task3/xiamen_road.txt', 'r') as f:
        for line in f:
            data = line.split()
            if data[0] == 'e':
                _, e1, e2 = data
                e1 = int(e1) - 1
                e2 = int(e2) - 1
                G.add_edge(e1, e2)
    return G


def draw(G):
    # 得到点的信息
    point_data = get_point_data()
    pos = [point_data[str(node)] for node in point_data.keys()]
    nx.draw(G,
            pos=pos,
            # node_color='green',
            # node_shape='o',
            width=10,
            # style='solid',
            with_labels=False,
            # font_size=8,
            # font_weight='bold',
            # alpha=0.5,
            node_size=0.1
            )
    # plt.show()
    plt.savefig('Task3/xiame_graph.png', dpi=300)


if __name__ == '__main__':
    draw(creat_graph())
    print('Draw done!')
