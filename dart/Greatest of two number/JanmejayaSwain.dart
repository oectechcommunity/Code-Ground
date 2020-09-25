import 'dart:io';

int gratestNumber(int fn, int sn) {
  if (fn > sn) {
    return fn;
  }
  return sn;
}

main() {
  stdout.write("enter 1st numnber: ");

  int firstNumber = int.parse(stdin.readLineSync());

  stdout.write("enter 2st numnber: ");

  int secondNumber = int.parse(stdin.readLineSync());

  print("Your gretest Number is ${gratestNumber(firstNumber, secondNumber)} ");
}
