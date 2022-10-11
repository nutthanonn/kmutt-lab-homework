#include <iostream>
using namespace std;

class Customer
{
    public:
        int ID;
        string name;
        int age;
        char sex;
        int incomeRange;
        string segment;
        Customer(int id, string name, int age, char sex, int incomeRange, string segment)
        {
            this->ID = id;
            this->name = name;
            this->age = age;
            this->sex = sex;
            this->incomeRange = incomeRange;
            this->segment = segment;
        }
};

class Node
{
    public:
        Node *next;
        Customer *cust;
        Node(Node *next, Customer *c)
        {
            this->next = next;
            this->cust = c;
        }
        void insertionSort(Node *curr, Customer *cust, string sortby);
};


void Node::insertionSort(Node *curr, Customer *cust, string sortby)
{
    if(sortby == "next")
    {
        if(curr->next == NULL)
        {
            curr->next = new Node(NULL, cust);
            return;
        }else
            return this->insertionSort(curr->next, cust, sortby);
    }else if(sortby == "incomeIndex")
    {
        if(curr->next == NULL)
        {
            curr->next = new Node(NULL, cust);
            return;
        }else if(curr->next->cust->incomeRange > cust->incomeRange)
        {
            Node *new_node = new Node(curr->next, cust);
            curr->next = new_node;
            return;
        }else
            return this->insertionSort(curr->next, cust, sortby);
    }else if(sortby == "ageIndex")
    {
        if(curr->next == NULL)
        {
            curr->next = new Node(NULL, cust);
            return;
        }else if(curr->next->cust->age > cust->age)
        {
            Node *new_node = new Node(curr->next, cust);
            curr->next = new_node;
            return;
        }else
            return this->insertionSort(curr->next, cust, sortby);
    }
}

void printLinked(Node *curr, string id)
{
    Node *temp = curr;
    while (temp != NULL)
    {
        printf("%d ", temp->cust->ID);
        printf("%s ", temp->cust->name.c_str());
        printf("%d ", temp->cust->age);
        printf("%c ", temp->cust->sex);
        printf("%d ", temp->cust->incomeRange);
        printf("%s \n", temp->cust->segment.c_str());
        temp = temp->next;
    }
}



int main()
{
    Customer *c1 = new Customer(1, "Kiva", 58, 'F', 20000, "target");
    Customer *c2 = new Customer(2, "Ryu", 20, 'M', 18000, "nontarget");
    Customer *c3 = new Customer(3, "Ken", 18, 'M', 30000, "nontarget");
    Customer *c4 = new Customer(4, "Zio", 19, 'F', 16000, "nontarget");
    Customer *c5 = new Customer(5, "Fourze", 40, 'M', 40000, "target");
    Customer *c6 = new Customer(6, "Gaim", 22, 'F', 25000, "target");

    Customer *all_cust[6] = {c1, c2, c3, c4, c5, c6};

    Node *next_head = new Node(NULL, NULL);
    Node *income_head = new Node(NULL, NULL);
    Node *age_head = new Node(NULL, NULL);
    
    int n = sizeof(all_cust) / sizeof(all_cust[0]);
    for(int i=0;i<n;i++)
    {
        next_head->insertionSort(next_head, all_cust[i], "next");
        income_head->insertionSort(income_head, all_cust[i], "incomeIndex");
        age_head->insertionSort(age_head, all_cust[i], "ageIndex");
    }

    cout << "----Sort by Next----" << endl;
    printLinked(next_head->next, "next");

    cout << "\n----Sort by Income----" << endl;
    printLinked(income_head->next, "income");

    cout << "\n----Sort by Age----" << endl;
    printLinked(age_head->next, "age");

    return 0;
}