import bisect

# 一天的秒数
one_day_seconds = 24 * 60 * 60

# 每5分钟为一个时段
breakpoints = [i * 5 * 60 for i in range(1, 289)]

# 返回时间l到r的时间段, 左闭右开区间
def g(l, r):
    return (bisect.bisect(breakpoints, l) + 1,
            bisect.bisect(breakpoints, r) + 2)

def creat_flow_network(d):
    # 以第d天统计
    base_day = d * 24 * 60 * 60
    
    res = {}
    
    with open('beijingTrajectory 6.2G/beijingTrajectory', 'r', encoding='utf-8') as f:
        for line in f:
            data = line.split(',')
            
            # 路段、进入路段的时间、结束时间
            _, _, _, _, link_sequence, _, _, _, \
            enter_time_sequence, *_, _, d_time, _, _ = data

            time_intervals = [int(i) - base_day for i in enter_time_sequence.split('|')]
            time_intervals.append(int(d_time) - base_day)
            
            for i, road_id in enumerate(link_sequence.split('|')):
                res.setdefault(road_id, dict())

                # 不在规定的日期内
                if time_intervals[i+1] < 0 or time_intervals[i] >= one_day_seconds:
                    continue

                l, r = g(time_intervals[i], time_intervals[i+1])

                for time_interval in range(l, r):
                    res[road_id].setdefault(time_interval, 0)
                    res[road_id][time_interval] += 1
    
    with open('flow_network.txt', 'w', encoding='utf-8') as f:
        for road_id, road_data in res.items():
            for t, car_count in road_data.items():
                f.write('${}_{},{}$'.format(car_count, '{'+road_id, str(t)+'}') + '\n')
    
    return None

if __name__ == '__main__':
    # 以1970年过后第16526天统计
    creat_flow_network(16526)
    print('Done')