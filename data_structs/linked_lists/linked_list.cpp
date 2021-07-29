/*
A linked list is a structure that
store data in a sequence of linked nodes.
In a single linked list, each node has a point
to the next one. While in a double linked list
each node has a point to the next and the previous
one.

Unlike an array, a linked list does not have
instant access to a specific index, instead
you need to iterate over the linked list to
determine what is the k-th node.

the linked list advantage is that you can remove and
add item from the begin in constant time, besides there
are no fixed limit of size.
*/
#include <iostream>

using namespace std;

class Node
{
    public:
        int data;
        Node* next = NULL;
};

void append(Node** head, int data)
{
    // we create a new node who
    // houses the new node to be
    // inserted
    Node* newNode = new Node();

    // we add the value
    // to the node we've
    // just created
    newNode->data = data;

    if(*head == NULL){
        *head = newNode;
        return ;
    }

    // we wanna inserte at
    // the node whose next value == NULL
    // so we have to iterate through
    // the linked list
    Node* end = *head;

    while (end->next != NULL)
        end = end->next;
    
    // after the previously while
    // we know the end is the last
    // node, so we add at end.next
    end->next = newNode;
};

void delete_by_key(Node** head_ref, int key)
{
     
    // Store head node
    Node* temp = *head_ref;
    Node* prev = NULL;
     
    // If head node itself holds
    // the key to be deleted
    if (temp != NULL && temp->data == key)
    {
        *head_ref = temp->next; // Changed head
        delete temp;            // free old head
        return;
    }
 
    // Else Search for the key to be deleted,
    // keep track of the previous node as we
    // need to change 'prev->next' */
    while (temp != NULL && temp->data != key)
    {
        prev = temp;
        temp = temp->next;
    }
 
    // If key was not present in linked list
    if (temp == NULL)
        return;
 
    // Unlink the node from linked list
    prev->next = temp->next;
 
    // Free memory
    delete temp;
    
};

void del_k_node(Node** head, int k)
{
    // given an integer k
    // delete the k-th node
    // of the linked list

    // corner case for head == NULL
    if (*head == NULL){
        cout << "linked list empty!" << endl;
        return ;
    }

    Node* prev = NULL;
    Node* temp = *head;

    // corner case for del first node
    if (k == 1)
    {
        *head = temp->next;     // Changed head
        delete temp;            // free old head
        return;
    }

    while (k != 1 and temp != NULL){
        prev = temp;
        temp = temp->next;
        k--;
    }

    // corner case for k out of range
    // i.e, k bigger than the number of nodes
    if (k > 1){
        cout << "k out of range!" << endl;
        return ;
    }

    // this will affect the original linked list
    // remove at the middle
    prev->next = temp->next;
    delete temp;
};

void show(Node* head)
{
    if (head == NULL)
        cout << "NULL" << endl;

    while(head != NULL){
        cout << head->data << " -> ";
        head = head->next;
    }
    cout << endl;
};

bool isempty(Node** head)
{
    return *head == NULL;
};

/*
In the previous simple definition, we dont have
a linkedList, but a Node. The linked list
is accessable trought a head reference.

other specific aspect of the linked list is the head
points to the first element of the linked list
if you have multiple objects referencing to the linkedList
you must be a bit carefull when a objects intends to delete
the first element, in ordem to avoid the head point beeing
used while you delete it.
*/

/*
Delete node
*/

int main()
{
    // holds the pointe to the first
    // node of the list

    // this is not a good practice
    // Node* head = new Node();

    //instead use
    Node* head = NULL;

    append(&head, 0);
    append(&head, 1);
    append(&head, 2);

    /*
    show(head);
    del_k_node(&head, 4);
    show(head);

    del_k_node(&head, 2);
    show(head);

    del_k_node(&head, 1);
    show(head);

    del_k_node(&head, 1);
    show(head);
    */

    del_k_node(&head, 3);
    show(head);

    del_k_node(&head, 1);
    show(head);

    del_k_node(&head, 1);
    show(head);

    return 0;
}

