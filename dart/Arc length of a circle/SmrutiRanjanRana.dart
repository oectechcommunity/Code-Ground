import 'dart:io';
import 'dart:math';

double getArcLength(double diameter, double angle) {
  if (angle >= 360) {
    print("Angle cannot be formed!");
    return 0;
  }

  return (pi * diameter) * (angle / 360);
}

void main() {
  stdout.write("What's the diameter?");
  double diameter = double.parse(stdin.readLineSync());

  stdout.write("What's the angle? ");
  double angle = double.parse(stdin.readLineSync());

  print("Arc is ${getArcLength(diameter, angle)}");
}
