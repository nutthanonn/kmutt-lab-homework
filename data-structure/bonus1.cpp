#include <iostream>
#include <ctime>
#include <cstdlib>
#include <cmath>

using namespace std;

/*
    studenNumber = 64090500431
    Hero = (2, 1)
    monster = (8, 3)
*/

int main()
{
    // int lastStudentNumber = 9, birthDay = 1, lastSecStudentNumber = 5;
    int lastStudentNumber = 1, birthDay = 2, lastSecStudentNumber = 3;
    srand((unsigned)time(NULL));
    int j = rand() % 10, k = rand() % 10;

    int map[10][10];
    for (int i = 0; i < 10; i++)
        for(int j=0;j<10;j++)
            map[i][j] = 0;

    map[j][k] = 1;
    map[lastStudentNumber][birthDay] = 2;
    map[lastSecStudentNumber][10 - birthDay] = 3;

    for (int i = 9; i > -1; i--)
    {
        for(int j=0;j<10;j++)
            cout << map[i][j] << " ";
        cout << endl;
    }

    int d_x = (10-birthDay) - birthDay;
    int d_y = lastSecStudentNumber - lastStudentNumber;

    cout << "Taxicab: " << abs(d_x) + abs(d_y) << endl;
    cout << "Euclidean: " << sqrt(pow(d_x, 2) + pow(d_y, 2)) << endl;
    cout << "Chebyshev: " << max(abs(d_x), abs(d_y)) << endl;

    return 0;
}