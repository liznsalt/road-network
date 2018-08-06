import math
import json

EARTH_REDIUS = 6378.137

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


# 利用闭包求平均值
def make_averager():
    count = 0
    total = 0
    def averager(new_value=None):
        nonlocal count, total
        if new_value != None:
            count += 1
            total += new_value
        return total/count
    return averager


def main():
    # 提取经纬度信息
    with open('Task3/nodes.json', 'r') as f:
        data = json.load(f)
    
    # 储存两点的id和之间距离
    res = []
    max_dis = 0
    min_dis = 1
    avg = make_averager()

    # 读取厦门路段并储存各路段距离
    with open('Task3/xiamen_road.txt', 'r') as f:
        for line in f:
            if line[0] == 'e':
                _, e1, e2 = line.split()
                lon1, lat1 = data[e1]
                lon2, lat2 = data[e2]
                dis = getDistance(float(lat1), float(lon1), float(lat2), float(lon2))
                # 保存最大、最小、平均值
                max_dis = max(max_dis, dis)
                min_dis = min(min_dis, dis)
                avg(dis)
                # 保存id和之间距离
                res.append((e1, e2, dis))

    # 写入文件
    with open('Task3/distance.txt', 'w', encoding='utf-8') as f:
        f.write('平均值：{}'.format(avg()) + '\n')
        f.write('最大值：{}'.format(max_dis) + '\n')
        f.write('最小值：{}'.format(min_dis) + '\n')
        f.write('ID1  ID2  DISTANCE(km)\n')
        for r in res:
            e1, e2, dis = r
            f.write('{} {} {}'.format(e1, e2, dis) + '\n')


if __name__ == '__main__':
    main()
    print('Distance statistic done!')
