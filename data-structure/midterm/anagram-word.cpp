#include <iostream>
using namespace std;


bool Anagram(string str1, string str2)
{
    
    if(str1.size() != str2.size())
        return false;

    int bucket1[26] = {0};
    int bucket2[26] = {0};

    for(int i = 0; str1[i] && str2[i]; i++) 
    {
        bucket1[str1[i] - 65]++;
        bucket2[str2[i] - 65]++;
    }

    for(int i = 0; i < 26; i++)
        if (bucket1[i] != bucket2[i])
            return false;
        
    return true;
}


int main()
{
    string str1 = "ABCDZA";
    string str2 = "ZCABDA";
    transform(str1.begin(), str1.end(), str1.begin(), ::toupper);
    transform(str2.begin(), str2.end(), str2.begin(), ::toupper);

    cout << "str1: " << str1 << endl;
    cout << "str2: " << str2 << endl;
    if(Anagram(str1, str2)) cout << "Is anagram word" << endl;
    else cout << "Is not anagram word" << endl;
    return 0;
}