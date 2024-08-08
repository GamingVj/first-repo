#include <iostream>
#include <conio.h>
using namespace std;

int main() {
	
    int arr1[50], arr2[50], merge[100], size1, size2, size, i, j, k, temp;

    cout << "Enter array1 size:";
    cin >> size1;
    cout << "Enter array1 elements:";
    for (i = 0; i < size1; i++) {
        cin >> arr1[i];
    }

    cout << "Enter array2 size:";
    cin >> size2;
    cout << "Enter array2 elements:";
    for (i = 0; i < size2; i++) {
        cin >> arr2[i];
    }

    size = size1 + size2;

    // Copy arr1 to merge array
    for (i = 0; i < size1; i++) {
        merge[i] = arr1[i];
    }

    // Merge arr2 into merge array
    for (i = 0, k = size1; i < size2 && k < size; i++, k++) {
        merge[k] = arr2[i];
    }

    cout << "Now the new array after merging is:\n";
    for (i = 0; i < size; i++) {
        cout << merge[i] << " ";
    }

    // Sorting the merged array
    for (i = 0; i < size - 1; i++) {
        for (j = 0; j < size - i - 1; j++) {
            if (merge[j] > merge[j + 1]) {
                temp = merge[j];
                merge[j] = merge[j + 1];
                merge[j + 1] = temp;
            }
        }
    }

    cout << "\nData after sorting:\n";
    for (i = 0; i < size; i++) {
        cout << merge[i] << " ";
    }
    getch();
    return 0;
}
