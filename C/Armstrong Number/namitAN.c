/* Armstrong number program */
#include <stdio.h>

int isArmstrong(int);
int power(int, unsigned int);
unsigned int digits(int);

int main (void) {
    int n;

    printf("Input a number\n");
    scanf("%d",&n);

    if (isArmstrong(n))
      printf("%d is an armstrong number.\n",n);
    else
      printf("%d isn't an armstrong number.\n",n);

    return 0;
}

// Function to check if the given number is armstrong number or not

int isArmstrong(int n) {
  if(n < 0) {
    return 0;
  }

  int sum = 0, temp;
  int remainder;
  unsigned int dig = digits(n);

  temp = n;

  while (temp) {
    remainder = temp%10;
    sum += power(remainder, dig);
    printf("%d\n",sum);
    temp /= 10;
  }

  if (n == sum)
    return 1;
  else
    return 0;
}

// function to find the number of digits

unsigned int digits(int x){   // number of digits is a non-negative quantity
  unsigned int dig = 0;
  while (x) {
    dig++;
    x /= 10;
  }
  return dig;
}

// function to raise the digit to the power of total number of digits

int power(int n, unsigned int r) {
  unsigned int c;
  int p = 1;

 for (c = 0; c < r; c++)
    p *= n;

   return p;
}
