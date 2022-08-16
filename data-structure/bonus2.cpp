#include <iostream>
#include <cstring>
#include <cmath>
#include <ctime>
using namespace std;

struct Student
{
    char name[50];
    int score;
};



void MaxStudent(struct Student student[10])
{   
    struct Student max_student;
    max_student.score=0;
    for(int i=0;i<10;i++)
    {
        if(student[i].score > max_student.score)
        {
            max_student.score = student[i].score;
            strcpy(max_student.name, student[i].name);
        }
    }
    cout << "Max Student: " << max_student.name << endl;
    cout << "score: " << max_student.score << endl;
}


void MinStudent(struct Student student[10])
{   
    struct Student min_student;
    min_student.score=INT_MAX;
    for(int i=0;i<10;i++)
    {
        if(student[i].score < min_student.score)
        {
            min_student.score = student[i].score;
            strcpy(min_student.name, student[i].name);
        }
    }
    cout << "Min Student: " << min_student.name << endl;
    cout << "score: " << min_student.score << endl;
}


double AvrScore(struct Student student[10])
{
    double av;
    for(int i=0;i<10;i++)
        av += student[i].score;
    av /= 10;
    cout << "AvrScore: " << av << endl; 
    return av;
}




void ModeScore(struct Student student[10])
{
    int number = student[0].score;
    int mode = number;
    int count = 1;
    int countMode = 1;

    for (int i=1; i<10; i++)
    {
        if(student[i].score == number)
            ++count;
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
    cout << "mode : " << mode << endl;
}


void selection_sort(int scores[10])
{
    for(int i=0;i<10;i++)
        for(int j=0;j<10;j++)
            if(scores[i] < scores[j])
                swap(scores[j], scores[i]);
}


double MedianScore(struct Student student[10])
{
    int scores[10];
    for(int i=0;i<10;i++)
        scores[i] = student[i].score;

    selection_sort(scores);

    double med = (scores[4]+scores[5]) / 2.0;
    cout << "Med: " << med << endl;

    return med;
}



double SDScore(struct Student student[10])
{
    int i;
    float sum = 0.0, mean, standardDeviation = 0.0;

    int data[10];
    for(int i=0;i<10;i++)
        data[i] = student[i].score;

    for(i = 0; i < 10; ++i) 
        sum += data[i];

    mean = sum / 10;

    for(i = 0; i < 10; ++i) 
        standardDeviation += pow(data[i] - mean, 2);

    double sd = sqrt(standardDeviation / 10);
    cout << "SDScore: " << sd << endl;

    return sd;
}


void get_grade(double avr, double SD, int score)
{   
    if(score >= avr + 2*SD)
        cout << "Grade: A";
    else if(score < avr+2*SD && score >= avr+SD)
        cout << "Grade: B";
    else if(score < avr+SD && score >= avr)
        cout << "Grade: C";
    else if(score < avr+SD && score >= avr-SD)
        cout << "Grade: D";
    else
        cout << "Grade: F";

}


int main()
{
    char names[10][50] = {
        "Barbara", "Ginger", "Larry", "Mary", "Diane", "Robert", "Michael", "Arturo", "Rodolfo", "Deborah",
    };

    int scores[10];
    srand((unsigned)time(NULL));
    for(int i=0;i<10;i++)
        scores[i] = rand()%50 + 50;
    
    
    struct Student student[10];
    for(int i=0;i<10;i++)
    {
        strcpy(student[i].name, names[i]);
        student[i].score = scores[i];
    }

    MaxStudent(student);
    cout<<endl;

    MinStudent(student);
    cout<<endl;

    double av = AvrScore(student);
    cout<<endl;

    ModeScore(student);
    cout<<endl;

    MedianScore(student);
    cout<<endl;

    double sd = SDScore(student);
    cout<<endl;


    for(int j=0;j<10;j++)
    {
        int score = student[j].score;
        cout << student[j].name;
        get_grade(av, sd, score);
        cout << endl;
    }

    return 0;
}