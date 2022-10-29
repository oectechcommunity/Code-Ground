import java.util.Scanner;
public class Armstrong {
    public static void main(String args[]) {
        int n, temp, d, s = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your number");
        n = sc.nextInt();
        temp = n;
        while(n > 0) {
            d = n % 10;
            s = s + Math.pow(d, 3);
            n = n / 10;
        }
        if (s == temp) {
            System.out.println("Armstrong number");
        }
        else {
            System.out.printlln("Not an Armstrong number");
        }
    }
}        
