#include <iostream>

using namespace std;


int main()
{
    int adjMatrix[5][5];
    int i, j;
    for(i = 0; i < 5; i++)
    {
        for(j = 0; j < 5; j++)
        {
            adjMatrix[i][j] = 0;
        }
    }

    adjMatrix[0][1] = 1;
    adjMatrix[0][2] = 1;

    adjMatrix[1][0] = 1;
    adjMatrix[1][2] = 1;
    adjMatrix[1][4] = 1;

    adjMatrix[2][0] = 1;
    adjMatrix[2][1] = 1;

    adjMatrix[3][4] = 1;

    adjMatrix[4][3] = 1;
    adjMatrix[4][1] = 1;

    return 0;
}