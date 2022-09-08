#include <iostream>
using namespace std;

class Node
{
    public:
        Node *next;
        int val;
    Node(int c, Node *nextVal=NULL):val(c)
    {
        next = nextVal;
    }
};



class Queue
{
    public:
        Node *front;
        Node *rear;
        int weight;
};

void Enqueue(Queue *q, int val)
{
    Node *temp = new Node(val, NULL);
    if(q->weight == 0)
    {
        q->rear = temp;
        q->front = temp;
    }
    else
    {
        q->rear->next = temp;
        q->rear = q->rear->next;
    }
    q->weight++;
}


int Dequeue(Queue *q)
{
    if(q->weight == 0)
        return 0;

    int ltemp = q->front->val;
    Node *temp = q->front;
    q->front = temp->next;
    if(q->rear == temp)
        q->rear = q->front;

    delete temp;
    q->weight--;
    return ltemp;
}


int main()
{
    Queue *q = new Queue();
    Enqueue(q, 10);
    Enqueue(q, 20);
    Enqueue(q, 30);

    cout << q->front->val << endl;
    cout << q->rear->val << endl;

    cout << Dequeue(q) << endl;
    cout << Dequeue(q) << endl;
    cout << Dequeue(q) << endl;
    return 0;
}