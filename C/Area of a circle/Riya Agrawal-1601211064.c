#include <stdio.h>   
#include <conio.h>
#include <math.h>
#define PI 3.141  
void main()   
{  
    double dia, area;  
    printf("Enter Diameter of circle\n");  
    scanf("%lf", & dia);  
    area = fmod((PI*dia*dia),4);  
    printf("Area of circle : %lf\n", area);  
    getch();    
}   
