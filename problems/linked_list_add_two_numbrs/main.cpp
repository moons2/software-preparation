#include <iostream>

using namespace std;

class Node {
    public:
        int data;
        Node* next = NULL;
};

int main()
{
    // points to the first item
    Node* head = new Node();
    Node* tail = new Node();

    int n;

    // populating my list
    // read an input and verify if it is
    // bigger than 0
    while (cin >> n and n){
        Node* node = new Node();
        node->data = n;

        if(head->next == NULL){
            head->next = node;
        }

        tail->next = node;
        tail = tail->next;
    }

    Node* iterator = head->next;

    while (iterator != NULL)
    {
        cout << iterator->data << endl;
        iterator = iterator->next;
    }
    
    return 0;
}