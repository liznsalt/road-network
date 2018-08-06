import json

def creat_point_data(line_count):
    res = {}
    with open('Task1/edges.txt', 'r') as f:
        count = 0

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
        
            count += 1
            if count >= line_count:
                break

    g = {i+1: res[key] for i, key in enumerate(sorted(res))}
    return g

def write_to_file(content):
    with open('Task1/point_data.json', 'w') as f:
        json.dump(content, f, ensure_ascii=False, \
                            indent=4, separators=(',', ': '))

if __name__ == '__main__':
    write_to_file(creat_point_data(651748))
    print('Done')
