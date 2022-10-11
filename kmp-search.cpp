/*

KMP Search Algorithm
Time o(m + n); m = Time to make LPS Array

*/



#include <iostream>
using namespace std;

void LPS(char* str, int n, int* lps_arr) 
{
    lps_arr[0] = 0;
    int j = 0, i = 1;

    while (i < n) 
    {
        if (str[i] == str[j]) 
        {
            j++;
            lps_arr[i] = j;
            i++;
        }
        else
        {
            if (j != 0) j = lps_arr[j - 1];
            else
            {
                lps_arr[i] = 0;
                i++;
            }
        }
    }
}

bool KMP(char* str, char* sub, int* lps)
{

    int i = 0, j = 0;
    int len_str = strlen(str), len_sub = strlen(sub);

    while ((len_str - i) >= (len_sub - j)) 
    {
        if (sub[j] == str[i]) 
        {
            j++;
            i++;
        }

        if (j == len_sub)
        {
            return true;
            j = lps[j - 1];
        }
        else if (i < len_str && sub[j] != str[i]) 
        {
            if (j != 0) j = lps[j - 1];
            else i++;
        }
    }
    return false;
}



int main()
{
    char str[] = "ababacabcabcabababd";
    char sub[] = "ababd";
    int n = strlen(sub);
    int lps[n];
    LPS(sub, n, lps);
    if(KMP(str, sub, lps)) cout << "True";
    else cout << "False";
    return 0;
}