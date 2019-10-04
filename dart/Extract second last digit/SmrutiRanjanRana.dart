import 'dart:io';

String getSecondDigit(String number) {
  return number.split('').reversed.join()[1];
}

void main() {
  stdout.write('Enter a number : ');
  String number = stdin.readLineSync();

  print("Second last number is ${getSecondDigit(number)}");
}
