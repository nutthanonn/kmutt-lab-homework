#include <iostream>
#include <vector>
#include <random>
using namespace std;



int select(vector<int>& nums, int first, int last, int k)
{
    if (first == last) 
        return nums[first];
    int random_index = first+rand()%(last-first);
    
    swap(nums[random_index], nums[last]);
	
    int pivot = nums[last];
    
    int i = first;
    
    for (int j=first; j<last; j++)
    {
        if (nums[j]< pivot)
        {
            swap(nums[i], nums[j]);
            i++;
        }
    }

    swap(nums[last], nums[i]);

    if (i == k) 
        return nums[i];
    if (i < k)
        return select(nums, i+1, last, k);
    else
        return select(nums, first, i-1, k);

}


int quickSelect(vector<int> &nums, int k)
{
    int n = nums.size() - 1;
    int first = 0;
    int number = select(nums, 0, n, n - k + 1);

    return number;
}


int main()
{   
    vector<int> nums;
    nums.push_back(5);
    nums.push_back(9);
    nums.push_back(12);
    nums.push_back(2);
    nums.push_back(1);
    nums.push_back(13);

    int n = 3;
    cout << "Max n number is: ";
    for(int i=1;i<n+1;i++) 
        cout << quickSelect(nums, i) <<  " ";
    cout << endl;
    return 0;
}