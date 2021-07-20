# src: cracking the code interview 6yh edition page 67

# given an array of distinct integer values, count the number of pairs of integer
# that difference k. For example, given the array {1, 7, 5, 9, 2, 12, 3}
# and the difference  = 2, there are four pairs with difference 2:
# (1, 3) (3, 5) (5, 7) (7, 9)
import time


class KHash:
    ktable = {}

    def contains(self, key):
        return self.ktable.__contains__(key)

    def insert(self, key, value):
        self.ktable[key] = value


def main():
    arr = [1, 7, 5, 9, 2, 12, 3]
    k = 2
    myHashTable = KHash()
    output = 0

    for e in arr:
        if (not myHashTable.contains(e)):
            myHashTable.insert(e, e)
        if (myHashTable.contains(e+k)):
            output += 1
        if (myHashTable.contains(e-k)):
            output += 1

    print(output)  # the number of pairs

# this algorithm takes o(n) space and runtime
# once the dictionary {} is populated with in the max n elements
# and is traversed only one time


if __name__ == '__main__':
    begin = time.perf_counter()
    main()
    end = time.perf_counter()
    print('duration:', end-begin)
