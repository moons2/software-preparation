'''

'''
from queue import LifoQueue
# this manner, this algorithm takes O(n^2) ;(


class Stack:
    def __init__(self):
        self.stack = LifoQueue()
        self.seek = None

    def push(self, item):
        self.seek = item
        self.stack.put_nowait(item)

    def pop(self):
        poped = self.stack.get_nowait()
        if not self.empty():
            self.seek = self.stack.get_nowait()
            self.stack.put_nowait(self.seek)
        else:
            self.seek = None
        return poped

    def empty(self):
        return self.stack.empty()

    def gseek(self):
        return self.seek


def largestRectangleAreaBestApproach(heights):
    stack = []
    max_area = 0
    index = 0
    while index < len(heights):
        # If this bar is higher
        # than the bar on top
        # stack, push it to stack ]
        if (not stack) or (heights[stack[-1]] <= heights[index]):
            stack.append(index)
            index += 1
        # If this bar is lower than top of stack,
        # then calculate area of rectangle with
        # stack top as the smallest (or minimum
        # height) bar.'i' is 'right index' for
        # the top and element before top in stack
        # is 'left index'
        else:
            # pop the top
            top_of_stack = stack.pop()
            # Calculate the area with
            # heights[top_of_stack] stack
            # as smallest bar
            area = (heights[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index))
            # update max area, if needed
            max_area = max(max_area, area)
    print(index)
    # Now pop the remaining bars from
    # stack and calculate area with
    # every popped bar as the smallest bar
    while stack:
        # pop the top
        top_of_stack = stack.pop()
        # Calculate the area with
        # heights[top_of_stack]
        # stack as smallest bar
        area = (heights[top_of_stack] *
                ((index - stack[-1] - 1)
                 if stack else index))
        # update max area, if needed
        max_area = max(max_area, area)
    # Return maximum area under
    # the given histogram
    return max_area


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

    stack = Stack()

    max = i = 0

    while(i < len(histogram)):
        if(stack.empty() or histogram[stack.seek()] <= histogram[i]):
            stack.push(i)
            i += 1
        else:
            currMax = stack.get_nowait()
            area = histogram[currMax] * \
                (i - 1 if stack.empty() else (i-1-stack.qsize()-1))
            if(area > max):
                max = area
    while not stack.empty():
        currMax = stack.get_nowait()
        area = histogram[currMax] * \
            (i - 1 if stack.empty() else (i-1-stack.qsize()-1))
        if(area > max):
            max = area

    return max


if __name__ == '__main__':
    vec = [int(i) for i in input().split(' ')]
    print(largestRectangleAreaBestApproach(vec))
