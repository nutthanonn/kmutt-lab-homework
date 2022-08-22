#include <iostream>
#include <cstring>
#include <cmath>
#include <ctime>
using namespace std;

typedef struct Student
{
    char name[50];
    int score;
} s_node;

string MaxStudent(s_node student[10])
{   
    string max_student_name;
    int max_score=INT_MIN;
    for(int i=0;i<10;i++)
    {
        if(student[i].score > max_score)
        {
            max_score = student[i].score;
            max_student_name = student[i].name;
        }
    }
    return max_student_name;
}

string MinStudent(s_node student[10])
{   
    string min_student_name;
    int min_score=INT_MAX;
    for(int i=0;i<10;i++)
    {
        if(student[i].score < min_score)
        {
            min_score = student[i].score;
            min_student_name = student[i].name;
        }
    }
    return min_student_name;
}

float AvrScore(s_node student[10])
{
    float av;
    for(int i=0;i<10;i++)
        av += student[i].score;
    av /= 10.0;
    return av;
}

void selection_sort(int scores[10])
{
    for(int i=0;i<10;i++)
        for(int j=0;j<10;j++)
            if(scores[i] < scores[j])
                swap(scores[j], scores[i]);
}


int ModeScore(s_node student[10])
{
    int number = student[0].score;
    int mode = number;
    int count = 1;
    int countMode = 1;

    for (int i=1; i<10; i++)
    {
        if(student[i].score == number)
            count++;
        else
        {
            if (count > countMode)
            {
                countMode = count;
                mode = number;
            }
            count = 1;
            number = student[i].score;
        }
    }

    if (count > countMode)
        mode = number;

    return mode;
}

bool compare(s_node a, s_node b)
{
    return a.score < b.score;
}

double MedianScore(s_node student[10])
{
    double med = (student[4].score + student[5].score) / 2.0;
    return med;
}


double SDScore(s_node student[10])
{
    float standardDeviation = 0.0;
    for(int i=0; i<10; i++)
        standardDeviation += pow(student[i].score - AvrScore(student), 2);

    double sd = sqrt(standardDeviation / 10);
    return sd;
}

char get_grade(double avr, double SD, int score)
{   
    if(score > avr + 2*SD) return 'A';
    else if(score > avr+SD) return 'B';
    else if(score > avr) return 'C';
    else if(score > avr - SD) return 'D';
    else return 'F';
}


int main()
{
    char names[10][50] = {
        "Barbara", "Ginger", "Larry", "Mary", "Diane", "Robert", "Michael", "Arturo", "Rodolfo", "Deborah",
    };


    //{80, 92, 97, 99, 96, 53, 84, 89, 75, 61}

    int scores[10] ={80, 92, 97, 99, 96, 53, 84, 89, 75, 61};
    // srand((unsigned)time(NULL));
    // for(int i=0;i<10;i++)
    //     scores[i] = rand()%40 + 60;
    
    s_node student[10];
    for(int i=0;i<10;i++)
    {
        strcpy(student[i].name, names[i]);
        student[i].score = scores[i];
    }

    cout << "\n  Student data\n" << endl;
    for(int i=0;i<10;i++)
        cout << student[i].name << "  -  Score: " << student[i].score << endl;

    sort(student, student+10, compare);

    cout << "\n\tstat\n" << endl;
    float av = AvrScore(student);
    float SD = SDScore(student);
    cout << "Max Student: " << MaxStudent(student) << endl;
    cout << "Min Student: " << MinStudent(student) << endl;
    cout << "Average score: " << av << endl;
    cout << "Mode: " << ModeScore(student) << endl;
    cout << "Median: " << MedianScore(student) << endl;
    cout << "Standard Deviation: " << SD << endl;

    cout << "\n\tGrade\n" << endl;
    for(int i=0;i<10;i++)
        cout << student[i].name << " - Grade: " << get_grade(av, SD, student[i].score) << endl;

    return 0;
}