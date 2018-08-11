import matplotlib.pyplot as plt


def main():
    distance_data = []
    with open('distance.txt', 'r') as f:
        for line in f:
            distance_data.append(float(line))

    plt.hist(distance_data, bins=1000)
    plt.xlabel('Distance(m)')
    plt.ylabel('Probability')
    plt.title('Histogram of Xiamen roads\' distance')

    plt.ylim(0, 200)
    plt.show()


if __name__ == '__main__':
    main()
    print('Done!')
