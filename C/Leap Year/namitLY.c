// Check a year is Leap Year or Not program

#include <stdio.h>

int checkYear(int year);

int main()
{
    int year = 0;

    printf("Enter a year \n");
    scanf("%d",&year);

    checkYear(year)? printf("%d is a Leap Year",year):
                   printf("%d is not a Leap Year",year);
    return 0;
}

int checkYear(int year)
{
    if (year % 400 == 0)
        return 1;

    if (year % 100 == 0)
        return 0;

    if (year % 4 == 0)
        return 1;
    return 0;
}
