from Task5.get_distance import get_distance
import json


with open('../Task3/nodes.json', 'r') as f:
    pos = json.load(f)

base_length = 70


# 得到原来的路段数据
def get_data(file_name):
    way_count = 0
    node_count = 0
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            if line[0] == 'p':
                _, _, node_count, way_count = line.split()
            if line[0] == 'e':
                _, e1, e2 = line.split()
                data.append((e1, e2))
    return int(node_count), int(way_count), data


# 切割路段得到的新的经纬度列表
def create_new_positions(e1, e2, begin_id, add_num):
    # 起终点经纬度
    lon1, lat1 = pos[e1]
    lon2, lat2 = pos[e2]
    lon1 = float(lon1)
    lon2 = float(lon2)
    lat1 = float(lat1)
    lat2 = float(lat2)
    a_x = (lon2 - lon1) / (add_num + 1)
    a_y = (lat2 - lat1) / (add_num + 1)
    for i in range(1, add_num+1):
        pos[str(begin_id+i-1)] = (lon1+i*a_x, lat1+i*a_y)


# 生成新的nodes.json和road.txt
def main():
    node_count, way_count, data = get_data('../Task3/xiamen_road.txt')
    res = []
    # print(node_count, way_count)
    for d in data:
        e1, e2 = d
        dis = get_distance(e1, e2) * 1000
        # 处理长路段
        if dis >= 140:
            split_num = int(dis) // base_length
            # 增加新的点的坐标
            create_new_positions(e1, e2, node_count+1, split_num-1)
            # 增加新的`e e1 e2`
            res.append((e1, node_count+1))
            for i in range(1, split_num-1):
                res.append((node_count+i, node_count+i+1))
            res.append((node_count+split_num-1, e2))
            # 更新点数和路段数
            node_count += split_num-1
            way_count += split_num-1
        else:
            res.append((e1, e2))

    # 存储新的点的坐标
    with open('nodes.json', 'w') as file:
        json.dump(pos, file, ensure_ascii=False,
                  indent=4, separators=(',', ': '))

    # 保存为DIMACS格式
    with open('road.txt', 'w', encoding='utf-8') as file:
        file.write('c new xiamen graph' + '\n')
        file.write('p edge {} {}'.format(node_count, way_count) + '\n')
        for r in res:
            e1, e2 = r
            file.write('e {} {}'.format(e1, e2) + '\n')


if __name__ == '__main__':
    main()
    print('All done!')
