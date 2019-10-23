import java.util.Scanner;
class SquareArea {
   public static void main (String[] args)
   {
       System.out.println("Enter Side of Square:");
       Scanner scanner = new Scanner(System.in);
       double side = scanner.nextDouble();
       double area = side*side;  //Area of Square = s*s
       System.out.println("Area of Square is: "+area);
   }
}
