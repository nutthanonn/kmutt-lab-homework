/*

64090500431 Nutthanon Thongcharoen

*/


#include <iostream>
using namespace std;

class Node
{
    public:
        Node *next;
        Node *prev;
        string name;
        float score;
};


void insertSort(string name, float val, Node *head)
{
    Node *curr = head;
    Node *new_node = new Node();
    new_node->score = val;
    new_node->name = name;

    while (curr->next != NULL)
    {
        if(curr->next->score < val)
            break;
        curr = curr->next;
    }
    
    // check if val less than all of leaderboard scores
    if(curr->next == NULL)
        return;

    curr->next->prev = new_node;
    new_node->prev = curr;
    new_node->next = curr->next;
    curr->next = new_node;

    Node *temp = head;
    while (temp->next != NULL)
        temp = temp->next;
    cout << temp->name << " was remove from the score board with score " << temp->score << endl;
    temp->prev->next = NULL;
    delete temp;
}

void getLinkedlist(Node *head)
{
    Node *curr = head->next;
    while (curr != NULL)
    {
        cout << curr->name << " - " << curr->score << endl;
        curr = curr->next;
    }
}

void removeAll(Node *head)
{
    while (head != NULL)
    {
        Node *frence = head;
        head = head->next;
        delete frence;
    }
    
}

int main()
{
    int amount_leaderboard = 4;
    string name;
    float score;
    Node *head = new Node();
    
    string names[4] = {"Ryu", "Ken", "Chuli", "Sagat"};
    int scores[4] = {100, 98, 95, 94};

    Node *temp = head;
    for(int i=0;i<amount_leaderboard;i++)
    {
        if(temp->next == NULL)
        {
            Node *data = new Node();
            data->name = names[i];
            data->score = scores[i];

            data->prev = temp;
            temp->next = data;
        }
        temp = temp->next;
    }

    cout << "\t --- leaderboard --- " << endl;
    getLinkedlist(head);

    cout << "Enter name and score: ";
    cin >> name >> score;

    cout << "\n\t --- remove score ---\n" << endl;
    insertSort(name, score, head);

    cout << "\n\t --- Update Leaderboard ---" << endl;
    getLinkedlist(head);

    removeAll(head);

    return 0;
}