import json
import osmium as osm
import pandas as pd


class OSMHandler(osm.SimpleHandler):
    
    def __init__(self):
        super(OSMHandler, self).__init__()
        # 每个点邻接点的映射
        self.rel = {}
        # 全部点（包括中间点，为了储存全部点的坐标）
        self.nodes = {}
        # 路段数
        self.ways = 0
        # 点的映射=>id: th
        self.g = {}

    def node(self, n):
        lon, lat = str(n.location).split('/')
        self.nodes[n.id] = (lon, lat)

    def way(self, w):
        nodes = w.nodes
        for i, n in enumerate(nodes):
            if n.ref not in self.rel:
                self.rel[n.ref] = set()

            if i == 0:
                self.rel[n.ref].add(nodes[1].ref)
            elif i == len(nodes) - 1:
                self.rel[n.ref].add(nodes[-2].ref)
            else:
                self.rel[n.ref].add(nodes[i+1].ref)
                self.rel[n.ref].add(nodes[i-1].ref)

    # 暂时不处理relation
    def relation(self, r):
        pass

    def update(self):
        # 映射
        self.g = {id: th+1 for th, id in enumerate(sorted(self.nodes))}
        # 路段数
        for v in self.rel.values():
            self.ways += len(v)


def write_to_file(osmhandler):
    # 存储点的坐标
    with open('Task3/nodes.json', 'w') as f:
        nodes = {i+1: osmhandler.nodes[key] 
                        for i, key in enumerate(sorted(osmhandler.nodes))}
        json.dump(nodes, f, ensure_ascii=False, \
                            indent=4, separators=(',', ': '))

    # 保存为DIMACS格式
    with open('Task3/xiamen_road.txt', 'w', encoding='utf-8') as f:
        f.write('c xiamen graph' + '\n')
        f.write('p edge {} {}'.format(len(osmhandler.nodes), osmhandler.ways)
                 + '\n')
        for node_id, ns in osmhandler.rel.items():
            for n in ns:
                f.write('e {} {}'.format(osmhandler.g[node_id], osmhandler.g[n])
                         + '\n')

def main():
    osmhandler = OSMHandler()
    osmhandler.apply_file('Task3/map.osm')
    osmhandler.update()
    write_to_file(osmhandler)

if __name__ == '__main__':
    main()
    print('Done!')
