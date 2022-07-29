def BinarySearch(alist, item):
	l = 0
	r = len(alist) - 1

	while l <= r:
		mid = (r+l) // 2
		if alist[mid] == item:
			return True
		if alist[mid] > item:
			r = mid
		else:
			l = mid
	return False
