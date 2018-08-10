import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    distance_data = []
    with open('../Task3/distance.txt', 'r') as f:
        for line in f:
            distance_data.append(float(line))

    plt.hist(distance_data, bins=1000)
    plt.xlabel('Distance(m)')
    plt.ylabel('Probability')
    plt.title('Histogram of Xiamen roads\' distance')

    plt.ylim(0, 400)
    plt.show()


if __name__ == '__main__':
    main()
    print('Done!')
