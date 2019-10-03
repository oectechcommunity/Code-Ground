import java.util.Scanner;

class AreaOfRectangle {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the length of rectangle: ");
        double length = sc.nextDouble();

        System.out.println("Enter the breadth of rectangle: ");
        double breadth = sc.nextDouble();

        double area = length * breadth;

        System.out.println("The area of rectangle is: " + area);

    }

}