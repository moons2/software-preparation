'''

'''
from collections import deque
# this manner, this algorithm takes O(n^2) ;(


def largestRectArea(vec):
    vec_size = len(vec)

    if not vec_size:
        return 0

    largest_area = float('-inf')

    # this takes O(N), where N = length(vec)
    for i in range(vec_size):
        h = 1
        # this loop takes O(N/2)
        for j in range(i+1, vec_size):
            if (vec[j] < vec[i]):
                break
            h += 1
        if (h * vec[i] >= largest_area):
            largest_area = h * vec[i]

    return largest_area

# the second way is more robust and performatic


def largestRectArea2(histogram):

    stack = deque()

    max = i = 0


if __name__ == '__main__':
    vec = [int(i) for i in input().split(' ')]
    print(largestRectArea(vec))
