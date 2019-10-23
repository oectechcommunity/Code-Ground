import java.util.Scanner;
class AreaofSquare {
   public static void main (String[] args)
   {
       System.out.println("Enter Side of Square:");
       Scanner scanner = new Scanner(System.in);
       double side = scanner.nextDouble();
       double area = side*side; 
       System.out.println("Area of Square is: "+area);
   }
}
