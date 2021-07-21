'''
AMDOCS
Given a list of integers, write an algorithm
to determine if two any items differ, at leat
of 1

IN: [1]
OUT: False

IN: [5, 5, 5, 5]
OUT: False

IN: [1, 2, 5, 2, 5]
OUT: True, (1,2) and (5,1) and (2,5)

RESOLUTION:

this is ridiculously simple
the minimum conceivable runtime is O(N)
once all the items must be visited
once. The only answer required is if
two elements differ from the minimum of one
i.e, if they are different!
what we need to do is to traverse the
array keep tracking of the minimum and
the maximum element found
if they are equal, so all the elements are equal
otherwise its guarateed that at leat
on pair differ from at least one
'''


def solution(array):

    if(len(array) < 2):
        return False

    mini = maxi = array[0]

    for item in array:
        if item >= maxi:
            maxi = item
        if item <= mini:
            mini = item

    # if they are equal, so I want
    # return false, because I know
    # all elements in the array are equals
    # othewise I know at least on pair
    # of elements differ between each other
    return mini != maxi

    # this algorithm runs on O(N)


if __name__ == '__main__':
    arr = [int(i) for i in input().split(' ')]
    print(solution(arr))
