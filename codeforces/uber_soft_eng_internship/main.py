'''

'''

INDX_BEGIN = 0
INDX_END = 1


def easyCountUber(coordinates):

    # a hash representing the road
    road = set()

    for coordinate in coordinates:
        for mark in range(coordinate[INDX_BEGIN], coordinate[INDX_END] + 1):
            road.add(mark)

    return len(road)


if __name__ == '__main__':
    coords = [[-3, 0], [-2, -1], [1, 2], [2, 3], [5, 5]]

    print(easyCountUber(coords))
