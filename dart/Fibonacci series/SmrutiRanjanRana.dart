import 'dart:io';

void getFibonacciSeries(int number) {
  int first = 0;
  int second = 1;

  if (number <= 0) {
    print("Please input a valid number");
  } else if (number == 1) {
    print(first);
  } else {
    print(first);
    print(second);
  }

  for (var i = 2; i < number; i++) {
    int temp = first;
    first = second;
    second = temp + first;
    print(second);
  }
}

void main() {
  stdout.write("How many fibonaaci elements do you want? ");
  int number = int.parse(stdin.readLineSync());

  getFibonacciSeries(number);
}
