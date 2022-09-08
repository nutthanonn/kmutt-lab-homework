#include <iostream>
using namespace std;


class Node
{
    public:
        Node *next;
        int val;
    Node(int c, Node *nextVal):val(c)
    {
        next = nextVal;
    }
};

class Stack
{
    public:
        Node *top;
        int weight;


    ~Stack()
    {
        clear();
    }

    void clear(){
        while (top != NULL)
        {
            Node *temp = top;
            top = top->next;
            delete temp;
        }
        weight = 0;
    }
};



void Push(Stack *s, int val)
{
    s->top = new Node(val, s->top);
    s->weight++;
}

int Pop(Stack *s)
{
    if(s->top == NULL)
        return 0;
    int temp = s->top->val;
    Node *ltemp = s->top->next;
    delete s->top;
    s->top = ltemp;
    s->weight--;

    return temp;
}


int topVal(Stack *s)
{
    if(s->weight == 0)
    {
        return 0;
    }
    return s->top->val;
}

int main()
{
    Stack *s = new Stack();
    Push(s, 10);
    Push(s, 20);
    Push(s, 30);
    Push(s, 40);
    cout << Pop(s) << endl;
    cout << Pop(s) << endl;
    cout << Pop(s) << endl;
    cout << Pop(s) << endl;
    cout << Pop(s) << endl;
    cout << topVal(s) << endl;

    return 0;
}