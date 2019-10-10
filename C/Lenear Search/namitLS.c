// Linear search program
#include <stdio.h>
#include <stdlib.h>

int search(int arr[], int n, int x);

int main(void)
{
    int n, x;
    ;
    printf("Enter the number of digits in the array\n");
    scanf("%d",&n);

    if (n < 1) {
      printf("It should not be less than 1\nProgram closed\n");
      return 0;
    }

    int* arr =(int*)malloc(n * sizeof(int));

    printf("Enter elements in the array\n");
    for (unsigned int i = 0; i < n; i++) {
      scanf("%d",&arr[i]);
    }

    printf("Enter element to be searched in the array\n");
    scanf("%d",&x);

    int result = search(arr, n, x);
    (result == -1) ? printf("False, Element is not present in the array")
                   : printf("True, Element is present at %d position",
                            result+1);
    return 0;
}

// fumction to return the index of element

int search(int* arr, int n, int x)
{
    int i;
    for (i = 0; i < n; i++)
        if (arr[i] == x)
            return i;
    return -1;
}
