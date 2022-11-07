#include <iostream>
using namespace std;


bool kangaroo(char *txt, char *sub)
{
    int n = strlen(txt);
    int j = 0;
    for(int k=0;k<n;k++)
        if(txt[k] == sub[j])
            j++;

    return j == strlen(sub);
}


int main()
{   
    char txt[] = "AfNfeutCT";
    char sub[] = "Nut";
    cout << "---Text---" << endl << txt;

    cout << "\n\n---Find sub---" << endl << sub;

    cout << "\n\n--is kangaroo---" << endl;

    if(kangaroo(txt, sub)) cout << "True" << endl;
    else cout << "False" << endl;

    return 0;
}