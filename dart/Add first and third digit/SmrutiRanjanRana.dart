import 'dart:io';

void main() {
  stdout.write("Enter a number : ");

  String number = stdin.readLineSync();

  print(int.parse(number[0]) + int.parse(number[2]));
}
