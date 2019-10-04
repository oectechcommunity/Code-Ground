import 'dart:io';

void main() {
  stdout.write("What's your name ? ");

  String name = stdin.readLineSync();
  String convertedName = "";

  for(int i=0; i<name.length; i++) {
    if(isUpperCase(name[i])) {
      convertedName += name[i].toLowerCase();
    } else {
      convertedName += name[i].toUpperCase();
    }
  }

  print(convertedName);

}

bool isUpperCase(String string) {
  if (string == null) {
    return false;
  }
  if (string.isEmpty) {
    return false;
  }
  if (string.trimLeft().isEmpty) {
    return false;
  }
  String firstLetter = string.trimLeft().substring(0, 1);
  if (double.tryParse(firstLetter) != null) {
    return false;
  }
  return firstLetter.toUpperCase() == string.substring(0, 1);
}