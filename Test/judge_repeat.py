# 判断是否有重复路段
def main():
    emm = set()
    with open('../Task3/xiamen_road.txt', 'r') as f:
        for line in f:
            if line[0] == 'e':
                _, e1, e2 = line.split()
                if int(e1) > int(e2):
                    e1, e2 = e2, e1
                s = e1+e2
                if s not in emm:
                    emm.add(s)
                else:
                    print('还有相同的:' + e1 + ' ' + e2)

if __name__ == '__main__':
    main()