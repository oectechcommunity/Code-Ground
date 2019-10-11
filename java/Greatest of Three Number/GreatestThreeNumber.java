import java.util.Scanner;

public class GreatestThreeNumber {

    public static void main(String[] args) {

        int x,y,z;

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the first Number:");
        x = sc.nextInt();

        System.out.println("Enter the Second Number:");
        y = sc.nextInt();

        System.out.println("Enter the third Number:");
        z = sc.nextInt();

        if(x > y && x > z) {
            System.out.println(x + " is the Greatest Number.");
        } else if (y > z) {
            System.out.println(y + " is the Greatest Number.");
        } else {
            System.out.println(z + " is the Greatest Number.");
        }


    }

} 