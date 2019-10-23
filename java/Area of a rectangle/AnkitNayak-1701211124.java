import java.util.Scanner;
class RectangleArea {
   public static void main (String[] args)
   {
       System.out.println("Enter Length and Breadth of Rectangle:");
       Scanner scanner = new Scanner(System.in);
       double length = scanner.nextDouble();
       double breadth = scanner.nextDouble();
       double area = length*breadth; //Area of Rectangle = length*breadth                                    
       System.out.println("Area of Rectangle is: "+area);
   }
}
