import json

def creat_point_data():
    res = {}
    with open('Task1/edges.txt', 'r') as f:
        for line in f:
            _, *datas = line.split('|')
            for data in datas:
                node, j, w = data.split(',')
                if node[-1] == '-':
                    node = node[:-1]
                node = abs(int(node))
                j = float(j)
                w = float(w)
                res[node] = (j, w)
    return res

def write_to_file(res):
    with open('Task1/point_data.txt', 'w') as f:
        f.write(json.dumps(res, ensure_ascii=False, \
                            indent=4, separators=(',', ': ')))

if __name__ == '__main__':
    write_to_file(creat_point_data())
    print('Done')
