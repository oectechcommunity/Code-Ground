import java.util.Scanner;
public class AreaOfCircle {
   public static void main(String args[]){
      double radius;
      double area;
      Scanner scanner = new Scanner(System.in);
      System.out.println("Enter the radius of the circle");
      radius = scanner.nextInt();
      area = (radius*radius)*3.14;
      System.out.println("Area of the circle is : "+area);
   }
}