/*
given a linked list write an algorithm
to check if a linked list is a palindrome

SOLUTION

a linked list is a data struct that store data in
a list of nodes manner, it's of fast insertion, delete or
lookup in the first element.

The linked list is accessible through a node
called head, that points to the first element

a palindrome is a word that read backward or forward
is the same.

a possible solution is run the linked list using
an auxiliary data struct pile, since would be usefull
to visit all the item again and because the data
stored in the pile is reversed retrived

then we traverse the linked list once more making pop and verifying 
if the data of both structs match, if don't, so it's not a palindrome

to have a better performance, we could store the number of elements (N)
in the linked list, and compare the first (N/2) nodes of the linked list
with the first (N/2) poped pile's items.
*/