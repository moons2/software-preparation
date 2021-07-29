/*
write a code to remove duplicates from a unsorted linked
list

RESOLUTION

a linked list is a data struct that stores
data in a list of nodes, where this nodes
are dinamically linked.

the linked list is accessible through a head reference

first the minimum conceiveble runtime is O(N), once
all the nodes of the listNode should be visited.

next we need to traverse the linked list once assigning
each key to a hashtable, of the form <key, frequency>
since we can have multiples repetitions, otherwise, in case
we have at the maximum one repetition we could use a Set struct
that is a data struct likely hash table, but that only stores
the key, without value associated.

the bigger bottleneck could be the deletion of a likedlist
*/

#include <iostream>
#include <unordered_map>

using namespace std;

class Node
{
    public:
        int key;
        Node* next = NULL;
};

void append(Node** head, int key)
{
    // we create a new node who
    // houses the new node to be
    // inserted
    Node* newNode = new Node();

    // we add the value
    // to the node we've
    // just created
    newNode->key = key;

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

void del_node_by_key(Node** head, int key)
{
    if(*head == NULL)
        return ;
    
    Node* prev = NULL;
    Node* tmp = *head;

    if(tmp->key == key)
    {
        *head = tmp->next;
        delete tmp;
        return ;
    }

    while(tmp != NULL and tmp->key != key)
    {
        prev = tmp;
        tmp = tmp->next;
    }

    if( tmp == NULL)
        return ;
    
    prev->next = tmp->next;

    delete tmp;
}

void remove_dups(Node** head)
{
    if(*head == NULL)
        return ;
    
    unordered_map<int, int> map;

    Node* tmp = *head;
    
    while(tmp != NULL)
    {
        int key = tmp->key;
        if(map.find(key) != map.end())
        {
            map[key]++;
        }
        else
            map[key] = 1;
        tmp = tmp->next;
    }

    tmp = *head;
    Node* prev = NULL;
    Node* neew = prev;

    while(tmp != NULL)
    {
        if(map[tmp->key] > 1)
        {
            map[tmp->key]--;
            tmp = tmp->next;
        }
        else
        {
            prev = tmp;
            prev = prev->next;
            //Node* newNode = new Node();
            /*
            if(prev == NULL)
            {
                prev = tmp;
                prev = prev->next;
            }
            else
            {
                prev->next = tmp;
                prev = prev->next;
            }*/
            tmp = tmp->next;
        }
    }

    *head = neew;

    /*
    for(const auto& item: map)
    {
        while (item.second > 1)
        {
            del_node_by_key(head, item.first);
            map[item.first]--;
        }
    }*/

};

void show(Node* head)
{
    while(head != NULL)
    {
        cout << head->key << " -> ";
        head = head->next;
    }
    cout << endl;
}

int main()
{
    Node* head = NULL;

    int in;

    while (cin >> in and in != -1)
        append(&head, in);
    
    show(head);
    remove_dups(&head);
    show(head);


    return 0;
};