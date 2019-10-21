import 'dart:io';

// To get the greates number
int gratestNumber(int fn, int sn) {
  if(fn > sn) {
    return fn;
  }
  return sn;
}

main() {
  stdout.write("Whats your first number? : ");
  int firstNumber = int.parse(stdin.readLineSync());

  stdout.write("And second one? : ");
  int secondNumber = int.parse(stdin.readLineSync());

  print("Your grestest number is ${gratestNumber(firstNumber, secondNumber)}");
}
