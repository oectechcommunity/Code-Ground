#include <stdio.h>
void main()
{
      float a,b,c;
      float avg;
      printf("\tEnter Three Numbers\n");
      printf("Enter First Number  : ");
      scanf("%f", &a);
      printf("\nEnter Second Number : ");
      scanf("%f",&b);
      printf("\nEnter Third Number : ");
      scanf("%f",&c);
      avg=(a+b+c)/3.0;
      printf("\nAverage of Three Numbers : %f",avg);
}
