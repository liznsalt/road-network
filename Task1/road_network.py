def creat_road_network(line_count):
    # 统计边
    road_count = 0
    # 点集
    points = set()
    # 可能成为路口的集合
    maybe_cross_roads = set()
    # 路口
    cross_roads = set()
    # 记录各点可连接的点集
    res = {}
    
    with open('Task1/edges.txt') as f:
        count = 0
        for line in f:
            # 各点信息
            _, *rest = line.split('|')

            # 在最后添加标记元素
            rest.append('#-,0,0')

            for i, data in enumerate(rest[:-1]):
                # 当前点的编号
                NO, _, _ = data.split(',')
                # 如果点的编号最后为'-'则去掉最后的'-'
                # 且不可能成为路口
                if NO[-1] == '-':
                    NO = NO[:-1]
                else:
                    maybe_cross_roads.add(NO)
                points.add(NO)

                # 没有过这个结点则为其创建空的点集
                if not NO in res:
                    res[NO] = set()
                
                no, _, _ = rest[i+1].split(',')
                if no[-1] == '-':
                    no = no[:-1]
                else:
                    maybe_cross_roads.add(no)

                if no != '#':
                    points.add(no)
                    # 下一个点没在当前点的点集里出现过
                    # 则边的数目加一
                    if not no in res[NO]:
                        road_count += 1
                        res[NO].add(no)
            
            count += 1
            if count >= line_count:
                break

    # 映射g:id->th
    g = {id: th+1 for th, id in enumerate(sorted(points))}

    # 在可能成为路口的点中，只有可以通往两各点以上的才成为路口
    for road in maybe_cross_roads:
        if len(res[road]) > 1:
            cross_roads.add(road)

    with open('Task1/road_network.txt', 'w', encoding='utf-8') as f:
        f.write('c BeiJing graph' + '\n')
        f.write('p edge {} {}'.format(len(points), road_count) + '\n')
            
        # for road in cross_roads:
            # f.write('n {} {}'.format(g[road], 1) + '\n')
        
        for key in res.keys():
            values = res[key]
            for value in values:
               f.write('e {} {}'.format(g[key], g[value]) + '\n')
    
    print('Done')

if __name__ == '__main__':
    # 只读20边
    creat_road_network(651748)
