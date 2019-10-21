import java.util.Scanner;
class RectangleAreaDemo {
   public static void main (String[] args)
   {
       System.out.println("Enter Length of Rectangle:");
       //Capture the user's input
       System.out.println("Enter Breadth of Rectangle");
       //Capture the user's input
       Scanner scanner = new Scanner(System.in);
       //Storing the captured value in a variable
       double length = scanner.nextDouble();
       double breadth = scanner.nextDouble();
       //Area of Rectangle = length*breadth
       double area = length*breadth; 
       System.out.println("Area of Rectangle is: "+area);
   }
}
