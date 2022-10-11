/*

queue ที่สร้างจาก stack แพงกว่าเดิม 2 เท่า เนื่องจากใช้ stack 2 ตัวในการทำ
enqueue - o(1)
dequeue - o(n)

*/



#include <iostream>
using namespace std;

class Node
{
    public:
        Node* next;
        int value;
        Node(Node *next, int val) 
        {
            this->next = next;
            this->value = val;
        };
};


class Queue
{
    public:
        int size;
        Node* inStack;
        Node* outStack;
        Queue(int val) {
            this->inStack = new Node(NULL, val);
            this->size = 1;
        }
        void enqueue(int val);
        void dequeue();
        void SwitchStack(Node *inStack, bool isPop, string in);
};

void Queue::SwitchStack(Node *stack, bool isPop, string in)
{
    if(stack->next == NULL && isPop) 
    {
        cout << stack->value << endl;
        return;
    }
    else if(stack->next == NULL && !isPop) 
    {
        Node *new_node = new Node(this->inStack, stack->value);
        inStack = new_node;
        return;
    }

    Node *temp = stack;

    if(in == "outstack") 
    {
        Node *new_node = new Node(this->outStack, temp->value);
        outStack = new_node;
    } else 
    {
        Node *new_node = new Node(this->inStack, temp->value);
        inStack = new_node;
    }

    return SwitchStack(temp->next, isPop, in); // resurcive
}

void Queue::enqueue(int val) 
{
    this->size++;
    Node *new_node = new Node(this->inStack, val);
    this->inStack = new_node;
}

void Queue::dequeue()
{
    this->size--;
    if(this->size == 0)
    {
        cout << this->inStack->value << endl;
        this->inStack = NULL;
        return;
    }

    if(this->size < 0) {
        cout << "Empty queue" << endl;
        this->size = 0;
        return;
    }

    SwitchStack(this->inStack, true, "outstack");
    this->inStack = NULL;

    SwitchStack(this->outStack, false, "instack");
    this->outStack = NULL;
}


void printLinked(Node *curr)
{
    if(curr == NULL)
    {
        cout << endl;
        return;
    }

    cout << curr->value << " ";
    printLinked(curr->next);
}


int main()
{
    Queue *q = new Queue(1);
    q->enqueue(2);
    q->enqueue(3);
    q->enqueue(4);
    q->enqueue(5);

    cout << "------Queue------" << endl;
    printLinked(q->inStack);

    cout << "------POP------" << endl;
    q->dequeue();
    q->dequeue();
    q->dequeue();

    cout << "------Queue after pop------" << endl;
    printLinked(q->inStack);

    return 0;
}