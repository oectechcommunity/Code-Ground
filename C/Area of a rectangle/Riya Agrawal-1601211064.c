#include<stdio.h>
#include<conio.h>
 
void main()
{
   int length, breadth, area;
   printf("\nEnter the Length of Rectangle : ");
   scanf("%d", &length);
 
   printf("\nEnter the Breadth of Rectangle : ");
   scanf("%d", &breadth);
 
   area = length * breadth;
   printf("\nArea of Rectangle : %d", area);
 }
