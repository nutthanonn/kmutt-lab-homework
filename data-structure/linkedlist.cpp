/*

    Time: O(n-neaerest + 9 + 7N + (n-nearest * N) + 7 + n-nearest + n-nearest + n-nearest + n-nearest*4)

        : O((7+n-nearest)*N + 8*n-nearest + 16)

if n-nearest = 3

    Time = O((7+3)*N + 8*3 + 16)
         = O(10N + 40 กว่าๆ)
         = O(N)

*/

#include <iostream>
using namespace std;


class Node {
    public:
        double val;
        Node *next;
};


void Insert(Node *head, double val)
{
    Node *curr = head;
    Node *new_node = new Node();
    new_node->val = val;
    while (curr->next != NULL)
    {
        curr = curr->next;
    }

    curr->next = new_node;
}


void getValLinkedlist(Node *head)
{   
    Node *curr = head;
    while (curr != NULL)
    {
        cout << curr->val << endl;
        curr = curr->next;
    }
    
}


int main() {

    Node *head = new Node();
    head->val = 0;
    Insert(head, 10);
    Insert(head, 20);
    Insert(head, 30);
    Insert(head, 40);
    getValLinkedlist(head);

    return 0;
}