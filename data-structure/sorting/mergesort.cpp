#include <iostream>
using namespace std;

void merge(int item[], int begin, int mid, int end)
{
    int left = mid - begin + 1;
    int right = end - mid;
    int l1[left], l2[right];

    for(int i=0;i<left;i++)
        l1[i] = item[i + begin];

    for(int j=0;j<right;j++)
        l2[j] = item[mid+j+1];

    int i=0, j=0, k=begin;
    
    while (i < left && j < right)
    {
        if(l1[i] <= l2[j]){
            item[k] = l1[i];
            i++;
        }else { 
            item[k] = l2[j];
            j++;
        }
        k++;
    }

    while (i < left)
    {
        item[k] = l1[i];
        i++;
        k++;
    }

    while (j < right)
    {
        item[k] = l2[j];
        j++;
        k++;
    }
}


void mergeSort(int item[], int begin, int end)
{
    if(begin >= end)
        return;

    int mid = begin + (end - begin) / 2;
    mergeSort(item, begin, mid);
    mergeSort(item, mid+1, end);
    merge(item, begin, mid, end);
}

int main()
{
    int arr[] = {6, 5, 12, 10, 9, 1};
    int size = sizeof(arr) / sizeof(arr[0]);
    mergeSort(arr, 0, size - 1);
    for(int i=0;i<size;i++)
        cout << arr[i] << " ";
    return 0;
}