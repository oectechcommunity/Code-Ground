/* Fibonacci series program */
#include <stdio.h>

void Fibonacci(int);

int main(void) {

  int n;

  printf("Enter the number of terms\n");
  scanf("%d", &n);

  if(n <= 0) {
    printf("Enter a number greater than 0\nClosing the program\n");
    return 0;
  }

  printf("First %d terms of Fibonacci series are:\n", n);
  Fibonacci(n);

  return 0;
}

// function to print fibonacci series

void Fibonacci(int n) {

  int  first = 0, second = 1, next, c;

  for (c = 0; c < n; c++)
  {
    if (c <= 1)
      next = c;
    else
    {
      next = first + second;
      first = second;
      second = next;
    }
    printf("%d\t", next);
  }
}
