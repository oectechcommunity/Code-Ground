#include<stdio.h>
#include<conio.h>
 
void main()
{
   float length, breadth, area;
   printf("\nEnter the Length of Rectangle : ");
   scanf("%f", &length);
 
   printf("\nEnter the Breadth of Rectangle : ");
   scanf("%f", &breadth);
 
   area = length * breadth;
   printf("\nArea of Rectangle : %f", area);
 }
