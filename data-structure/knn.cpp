
/*

fetch data ช้า ไม่่ใช้ๆ


*/

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

typedef struct MBTI
{
    string student_no;
    string Name;
    string Sex;
    int Score[8];
    string Type;
    string Enneagram;
    string Nick;
    double distance;
} child_node;


int Insert(child_node node[100], int count, int index_node, string item)
{
    if(count == 0 && index_node == 0) node[index_node].student_no = item;

    if(count == 1) node[index_node].Name = item;
    else if(count == 2) node[index_node].Sex = item;
    else if (count > 2 && count <= 10) node[index_node].Score[count-3] = stoi(item);
    else if(count == 11) node[index_node].Type = item;
    else if(count == 12) node[index_node].Enneagram = item;
    else if(count == 13) 
    {
        int pos = item.find("\n");
        node[index_node].Nick = item.substr(0, pos);
        node[index_node].distance = 0;
        node[index_node+1].student_no = item.substr(pos+1);
        return index_node+1;
    }
    return index_node;
}




int main()
{
    fstream fin;
    string item;
    fin.open("CSS223.csv");
    int count = 0;
    int index_node = 0;
    int amount = 58;
    child_node node[amount];
    // int my_data[8] = {28.2, 17.6, 35, 39, 26, 37, 28, 20};

    if (fin.is_open()) 
    {
        while(fin.good())
        {
            getline(fin, item, ',');
            if(item.empty())
            {
                count++;
                continue;
            }
            

            index_node = Insert(node, count, index_node, item);

            if(count == 13)
                count = 0;
                
            // if(count == 0 && index_node == 0) node[index_node].student_no = item;

            // if(count == 1) node[index_node].Name = item;
            // else if(count == 2) node[index_node].Sex = item;
            // else if (count > 2 && count <= 10) node[index_node].Score[count-3] = stoi(item);
            // else if(count == 11) node[index_node].Type = item;
            // else if(count == 12) node[index_node].Enneagram = item;
            // else if(count == 13) 
            // {
            //     int pos = item.find("\n");
            //     node[index_node].Nick = item.substr(0, pos);
            //     node[index_node].distance = 0;
            //     count = 0;
            //     index_node++;
            //     node[index_node].student_no = item.substr(pos+1);
            // }
            
            count++;

        }
        fin.close();
    } else 
    {
        cout << "Failed To Open File" << endl;
    }

    for(int i=0;i<amount;i++)
        cout << node[i].Name << endl;

    return 0;
}