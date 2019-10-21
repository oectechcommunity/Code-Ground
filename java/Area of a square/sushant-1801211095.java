import java.util.Scanner;
class SquareAreaDemo {
   public static void main (String[] args)
   {
       System.out.println("Enter Side of Square:");
       //Capture the user's input
       Scanner scanner = new Scanner(System.in);
       //Storing the captured value in a variable
       double side = scanner.nextDouble();
       //Area of Square = side*side
       double area = side*side; 
       System.out.println("Area of Square is: "+area);
   }
}
