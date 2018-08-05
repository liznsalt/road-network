import json
import osmium as osm
import pandas as pd


class OSMHandler(osm.SimpleHandler):
    def __init__(self):
        super(OSMHandler, self).__init__()
        # 每个点邻接点的映射
        self.rel = {}
        # 路口
        self.crossings = set()
        # 全部点（包括中间点，为了储存全部点的坐标）
        self.nodes = {}
        # 路段数
        self.ways = 0

    def node(self, n):
        lon, lat = str(n.location).split('/')
        self.nodes[n.id] = (lon, lat)

    def way(self, w):
        self.ways += 1

        nodes = w.nodes
        for i, n in enumerate(nodes):
            if n not in self.rel:
                self.rel[n] = set()

            if i == 0:
                self.rel[n].add(nodes[1].ref)
            elif i == len(nodes) - 1:
                self.rel[n].add(nodes[-2].ref)
            else:
                self.rel[n].add(nodes[i+1].ref)
                self.rel[n].add(nodes[i-1].ref)

        # 将起点、终点加入路口
        # self.crossings.add(start)
        # self.crossings.add(end)

    # 暂时不处理relation
    def relation(self, r):
        pass


def write_to_file(osmhandler):
    # 存储点的坐标
    with open('Task3/nodes.json', 'w') as f:
        json.dump(osmhandler.nodes, f, ensure_ascii=False, \
                            indent=4, separators=(',', ': '))

    # 保存为DIMACS格式
    with open('Task3/result.txt', 'w', encoding='utf-8') as f:
        f.write('c xiamen graph' + '\n')
        f.write('p edge {} {}'.format(len(osmhandler.crossings), osmhandler.ways) + '\n')
        for node_id, ns in osmhandler.rel.items():
            for n in ns:
                f.write('e {} {}'.format(node_id, n) + '\n')

def main():
    osmhandler = OSMHandler()
    osmhandler.apply_file('Task3/map.osm')
    write_to_file(osmhandler)

if __name__ == '__main__':
    main()
    print('Done!')
