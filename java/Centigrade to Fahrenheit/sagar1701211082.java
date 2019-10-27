import java.util.Scanner;

public class JavaProgram
{
    public static void main(String args[])
    {
        float cen;
        double fah;
        Scanner scan = new Scanner(System.in);
		
        System.out.print("Enter Temperature in Centigrade : ");
        cen = scan.nextFloat();		
        fah = (1.8*cen) + 32;
		
        System.out.print("Equivalent Temperature in Fahrenheit = " + fah);
    }
}