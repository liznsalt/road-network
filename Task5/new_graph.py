import json
import matplotlib.pyplot as plt
import networkx as nx


def get_point_data():
    with open('nodes.json', 'r') as f:
        res = json.load(f)
    return res


def creat_graph():
    G = nx.Graph()
    with open('road.txt', 'r') as f:
        for line in f:
            data = line.split()
            if data[0] == 'e':
                _, e1, e2 = data
                G.add_nodes_from([e1, e2])
                G.add_edge(e1, e2)
    return G


# 画出新的graph，并标出各点
def draw(G):
    # 得到点的信息
    pos = get_point_data()
    nx.draw(G, pos=pos, with_labels=False)
    # 设置首界面X轴坐标范围
    plt.xlim(118.066, 118.197)
    # 设置首界面Y轴坐标范围
    plt.ylim(24.424, 24.561)
    plt.show()
    # plt.savefig('new_graph.png', dpi=300)


if __name__ == '__main__':
    draw(creat_graph())
    print('Draw done!')
