#include <iostream>
using namespace std;


class Node
{
    public:
        int coef;
        int expo;
        Node *next;
    Node(int c, int e): coef(c),expo(e) {}
};


void append(Node *p, int coef, int expo)
{
    Node *curr = p;
    Node *new_node = new Node(coef, expo);
    while (curr->next != NULL)
        curr = curr->next;

    curr->next = new_node;
}


Node *addition(Node *p1, Node *p2)
{
    Node *res = new Node(0, 0);
    Node *p = res;

    while (p1 != NULL && p2 != NULL)
    {
        int sum = 0;
        int expo = 0;
        if(p1->expo > p2->expo)
        {
            sum = p1->coef;
            expo = p1->expo;
            p1 = p1->next;
        }
        else if(p1->expo < p2->expo) 
        {
            sum = p2->coef;
            expo = p2->expo;
            p2 = p2->next;
        }
        else
        {
            sum = p1->coef + p2->coef;
			expo = p1->expo;
            p2 = p2->next;
            p1 = p1->next;
        }

        Node *temp = new Node(sum, expo);
        p->next = temp;
        p = p->next;
    }

	if(p1 != NULL)
		p->next = p1;

	if(p2 != NULL)
		p->next = p2;

    return res->next;
}


void mul(Node *p1, Node *p2)
{
    p1 = p1->next;
    p2 = p2->next;
    int size = p1->expo + p2->expo + 1;
    int res[size];
    for(int i=0;i<size;i++) res[i] = 0;

    Node *ptr1 = p1;
    Node *ptr2 = p2;
    while (ptr1 != NULL)
    {
        while (ptr2 != NULL)
        {
            int temp, e;
            temp = ptr1->coef * ptr2->coef;
            e = ptr1->expo + ptr2->expo;
            res[e] += temp;
            ptr2 = ptr2->next;
        }
        ptr2 = p2;
  
        ptr1 = ptr1->next;
    }

    for(int i=size-1;i>-1;i--)
        if(res[i] != 0)
            cout << res[i] << "x^" << i << " + ";
}



void printLinked(Node *head)
{
    Node *curr = head;
    curr = curr->next;
    while (curr != NULL)
    {
        cout << curr->coef << "x^" << curr->expo << " + ";
        curr = curr->next;
    }
    cout << endl;
}


int main()
{
    Node *p1 = new Node(0, 0);
    append(p1, 8, 3);
    append(p1, -5, 1);
    append(p1, 6, 0);

    Node *p2 = new Node(0, 0);
    append(p2, 5, 2);
    append(p2, 2, 1);
    append(p2, 1, 0);

    printLinked(p1);
    printLinked(p2);

    cout << endl;
    Node *p_add = addition(p1, p2);
    printLinked(p_add);
    
    cout << endl;
    mul(p1, p2);

    return 0;
}