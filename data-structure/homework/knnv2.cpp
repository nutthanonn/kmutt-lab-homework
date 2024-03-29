#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

typedef struct data
{
    string student_no;
    string fname;
    string lname;
    string sex;
    double scores[8];
    string type;
    string enneagram;
    string nick;
} d_node;

class Node 
{
    public:
        string name;
        string type;
        double distance;
        string student_no;
        Node* next;
};

// find distance using Euclidean
double find_distance(d_node other_data, d_node my_data)
{
    double dis = 0;
    for(int i=0;i<8;i++)
        dis += pow(my_data.scores[i] - other_data.scores[i], 2);
    return sqrt(dis);
}


// insert node to linkedlist
void Insert(Node *curr, double distance, int index, string nick, string type, string student_no)
{   
    Node *new_node = new Node();
    new_node->distance = distance;
    new_node->name = nick;
    new_node->type = type;
    new_node->student_no = student_no;
    
    new_node->next = curr->next;
    curr->next = new_node;
}

int main()
{
    int n_nearest = 3;

    fstream fin;
    fin.open("CSS223-MBTI.tsv");
    
    d_node my_data;
    double my_scores[8] = {28.2, 17.6, 35, 39, 26, 37, 28, 20};

    Node *head = new Node();
    head->distance = 0;
    Node *curr = head;
    
    for(int i=0;i<n_nearest+1;i++)
    {
        if(curr->next == NULL)
        {
            Node *temp = new Node();
            temp->distance = MAXFLOAT;
            curr->next = temp;
            delete temp;
        }
        curr = curr->next;
    }

    for(int i=0;i<9;i++) 
        my_data.scores[i] = my_scores[i];


    while (fin.good())
    {
        d_node other_data;
        fin >> other_data.student_no >> other_data.fname >> other_data.lname >> other_data.sex 
        >> other_data.scores[0] >> other_data.scores[1] >> other_data.scores[2] >> other_data.scores[3] 
        >> other_data.scores[4] >> other_data.scores[5] >> other_data.scores[6] >> other_data.scores[7] 
        >> other_data.type >> other_data.enneagram >> other_data.nick;

        if(other_data.student_no == "64090500431")
            continue;

        double distance = find_distance(other_data, my_data);

        Node *curr = head;
        for(int i=0;i<n_nearest;i++)
        {   
            if(curr->next->distance > distance) 
            {
                Insert(curr, distance, i, other_data.nick, other_data.type, other_data.student_no);
                break;
            }
            curr = curr->next;
        }


        // cout << other_data.student_no << " - " << other_data.fname << endl;
        // cout << other_data.nick << " - " << distance << endl;
    }

    // O(n-nearest)
    Node *temp = head;
    for(int i=0;i<n_nearest+1;i++)
    {
        cout << temp->student_no << " - " << temp->distance << " - " << temp->type << endl;
        temp = temp->next;
    }
    delete temp;


    
    string other_type[n_nearest];

    // O(n-nearest)
    // คืน memory ตรงนี้ได้
    for(int i=0;i<n_nearest+1;i++)
    {
        Node *fence = head;
        if(i==0)
            continue;
        head = head->next;
        other_type[i-1] = head->type;
        delete fence;
    }

    string max_char[2] = {"",""};
    int size_type = 4;
    string my_type = "";

    

    for(int i=0;i<size_type;i++)
    {
        for(int j=0;j<n_nearest;j++)
        {
            switch (other_type[j][i])
            {
                case 'I':
                case 'S':
                case 'T':
                case 'P':
                    max_char[0] += other_type[j][i];
                    break;
                default:
                    max_char[1] += other_type[j][i];
                    break;
            }
        }
        if(max_char[0].length() > max_char[1].length()) my_type += max_char[0][0];
        else my_type += max_char[1][0];
        // cout << max_char[0] << " - " << max_char[1] << endl;
        max_char[0] = "";
        max_char[1] = "";
    }

    cout << endl;
    cout << "MY_TYPE: " << my_type << endl;

    fin.close();

    return 0;
}