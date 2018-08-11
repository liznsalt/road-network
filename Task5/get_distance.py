import math
import json

EARTH_REDIUS = 6378.137
with open('../Task3/nodes.json', 'r') as f:
    data = json.load(f)


def rad(d):
    return d * math.pi / 180.0


def get_distance(e1, e2):
    lon1, lat1 = data[e1]
    lon2, lat2 = data[e2]

    radLat1 = rad(float(lat1))
    radLat2 = rad(float(lat2))
    a = radLat1 - radLat2
    b = rad(float(lon1)) - rad(float(lon2))
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a/2), 2)
                     + math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b/2), 2)))
    s = s * EARTH_REDIUS
    return s


if __name__ == '__main__':
    print(get_distance('1', '2'))