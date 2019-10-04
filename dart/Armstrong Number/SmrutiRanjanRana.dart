import 'dart:io';
import 'dart:math';

bool isArmstrong(String number) {
  int total = 0;

  for (int i = 0; i < number.length; i++) {
    total += pow(int.parse(number[i]), number.length);
  }

  if (total == int.parse(number)) {
    return true;
  }

  return false;
}


void main() {
  stdout.write("Put a number here: ");
  String number = stdin.readLineSync();

  if(isArmstrong(number)) {
    print("$number is an amstrong number"); 
  } else {
    print("$number is not an amstrong number"); 
  }
}
