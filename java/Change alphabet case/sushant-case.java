import java.util.Scanner;

public class CaseManipulation {  
 public static String toToggleCase(String inputString) {
       String result = "";
       for (int i = 0; i < inputString.length(); i++) {
           char currentChar = inputString.charAt(i);
           if (Character.isUpperCase(currentChar)) {
               char currentCharToLowerCase = Character.toLowerCase(currentChar);
               result = result + currentCharToLowerCase;
           } else {
               char currentCharToUpperCase = Character.toUpperCase(currentChar);
               result = result + currentCharToUpperCase;
           }
       }
       return result;
   }
}