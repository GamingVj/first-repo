
/*  
    Write a program to store the element in 1-10 aray and perform the operation like searching, 
    sorting and reversing the elements.
*/

#include <iostream>

int main()
{
    int arr[50], size, i, j, temp;
    std::cout << "Enter array size: ";
    std::cin >> size;
    std::cout << "Enter array elements: ";
    for (i = 0; i < size; i++)
    {
        std::cin >> arr[i];
    }
    j = size - 1;
    i = 0;
    while (i < j)
    {
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        i++;
        j--;
    }
    std::cout << "Now the Reverse of Array is:\n";
    for (i = 0; i < size; i++)
    {
        std::cout << arr[i] << " ";
    }
    return 0;
}
