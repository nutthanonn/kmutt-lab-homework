/*
    Example data: 
        64090500431	28.2	17.6	35	39	26	37	28	20	ESTJ

    Time: O(11N) = O(N)
*/


#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

typedef struct data
{
    string student_no;
    string type;
    double distance;
} d_node;


class Node
{
    public:
        Node *next;
        d_node data;
    Node(string student_no, string type, double distance)
    {
        this->data.student_no = student_no;
        this->data.type = type;
        this->data.distance = distance;
    }
};

void remove(Node *head)
{
    head = NULL;
}

int main()
{
    fstream fin;
    fin.open("./mbti.txt");
    d_node my_data;
    double my_scores[8] = {28.2, 17.6, 35, 39, 26, 37, 28, 20};
    Node *head = new Node("", "", 0);

    Node *ptr = head;
    for(int i=0;i<3;i++)
    {
        ptr->next = new Node("", "", MAXFLOAT);
        ptr = ptr->next;
    }

    while (fin.good())
    {
        d_node other_data;
        double scores[8];
        fin >> other_data.student_no >> scores[0] >> scores[1] 
        >> scores[2] >> scores[3]  >> scores[4] 
        >> scores[5] >> scores[6] >> scores[7] 
        >> other_data.type;

        if(other_data.student_no == "64090500431")
        {
            my_data = other_data;
            continue;
        }

        double distance = 0;
        for(int i=0;i<8;i++)
            distance += pow((scores[i] - my_scores[i]), 2);

        other_data.distance = sqrt(distance);
        

        Node *p = head;
        for(int i=0;i<3;i++)
        {
            if(p->next->data.distance > other_data.distance)
            {
                Node *temp = new Node(other_data.student_no, other_data.type, other_data.distance);
                temp->next = p->next;
                p->next = temp;
                break;
            }
            p = p->next;
        }
    }

    Node *res = head;
    string other_type[3];
    for(int i=0;i<3;i++)
    {
        res = res->next;
        cout << res->data.student_no << " - " << res->data.type << endl;
        other_type[i] = res->data.type;
    }

    int mbti_type = 4;
    int count = 0;
    string max_char[2] = {"",""};
    string my_type = "";


    Node *temp = head;
    for(int i=0;i<3 * mbti_type;i++)
    {
        int target = i%3;
        char c = other_type[target][count];
        switch (c)
        {
            case 'I':
            case 'S':
            case 'T':
            case 'P':
                max_char[0] += c;
                break;
            default:
                max_char[1] += c;
                break;
        }

        if(target == 0)
        {
            count++;
            if(max_char[0].length() > max_char[1].length()) my_type += max_char[0][0];
            else my_type += max_char[1][0];
            max_char[0] = "";
            max_char[1] = "";
        }
    }

    cout << "Vote: " << my_type << endl;
    remove(head);
    fin.close();

    return 0;
}