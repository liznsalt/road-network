# 只画出长的路段

import json
import matplotlib.pyplot as plt
import networkx as nx
import math

EARTH_REDIUS = 6378.137
edge_color = []


def rad(d):
    return d * math.pi / 180.0

def getDistance(lat1, lng1, lat2, lng2):
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a/2), 2)
                     + math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b/2), 2)))
    s = s * EARTH_REDIUS
    return s

def get_point_data():
    with open('../Task3/nodes.json', 'r') as f:
        res = json.load(f)
    return res


def creat_graph():
    G = nx.Graph()
    with open('../Task3/nodes.json', 'r') as f:
        data = json.load(f)
    with open('../Task3/xiamen_road.txt', 'r') as f:
        for line in f:
            d = line.split()
            if d[0] == 'e':
                _, e1, e2 = d
                lon1, lat1 = data[e1]
                lon2, lat2 = data[e2]
                dis = getDistance(float(lat1), float(lon1), float(lat2), float(lon2))
                G.add_edge(e1, e2)
                if dis*1000 <= 1000:
                    edge_color.append('white')
                else:
                    edge_color.append('black')
    return G


def draw(G):
    # 得到点的信息
    pos = get_point_data()
    nx.draw(G,
            pos=pos,
            edge_color=edge_color,
            with_labels=False
            )
    plt.xlim(118.066, 118.197)#设置首界面X轴坐标范围
    plt.ylim(24.424, 24.561)#设置首界面Y轴坐标范围
    plt.show()
    # plt.savefig('Task3/xiamen_graph.png', dpi=300)


if __name__ == '__main__':
    draw(creat_graph())
    print('Draw done!')
