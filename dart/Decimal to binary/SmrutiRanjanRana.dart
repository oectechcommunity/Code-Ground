import 'dart:io';

void main() {
  stdout.write("Put a decimal number : ");
  int decimalValue = int.parse(stdin.readLineSync());

  print(decimalToBinary(decimalValue));
}

int decimalToBinary(int decimalValue) {
  String binaryValue = "";

  if(decimalValue == 0) {
    return 0;
  }

  while(decimalValue > 0) {
    binaryValue += (decimalValue % 2).toString();
    decimalValue = (decimalValue ~/ 2);
  }

  return int.parse(binaryValue.split('').reversed.join());
}