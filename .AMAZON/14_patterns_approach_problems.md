# 1.	Sliding Window (janela deslizante)

used to perform a required operation on a specific window size
in array or linked list

**usually indicators of a sliding window approach**
-	linear data struct such as array, linked list or array
-	longest/shortest substring, subarray, desired value

**Exs**
-	maximum sum subarray of size K
-	longest substring with K distinct chars
-	String anagrams (hard)

# 2.	Two Pointers or Iterators

Usually used to perform an Iteration through an Array or Linked List. Two pointers is a pattern where two pointers iterate through the data structure in tandem until a condition be satisfied.
Two pointers is needed because on pointers would require iterate back and forth over the data many times, what would produce a time and space complexity along the lines of O(n^2).

**usually indicators**
-	given a sorted array/linked list, find any set of elements that satisfy a certains condition

**Exs**
-	Squaring a sorted array
-	Triplets that sum to zero
-	Comparing strings that contain backspaces

# 3.	Fast and Slow pointers

Approach that consists of use, in general, two pointers to iterate over a data structure such as array or linked list. Where the pointers iterate in different speeds.

**usually indicators**
-	scenario of a linked list problem
-	need to know the position of a certain element or the overall length of the linked list
-	**do not** use in single linked lists where is not possible move in backward directions


**Exs**
-	Determine if a linked list is a palindrome.
-	Linked List Cycle
-	Palindrome Linked List
-	Cycle in a Cicular Array

# 4.	Merge Intervals

An efficient technique to deal with overlapping intervals.

**usually indicators**
-	you were asked to produce a list with only mutually exclusive intervals
-	if you hear the term "overlapping intervals".

**Exs**
-	intervals intersection (medium)
-	maximum CPU load (hard)
