import java.util.Scanner;
public class greatest_of_two_numbers
{
	public static void main(String[] args)
	{
		//scanner class declaration
		Scanner sc = new Scanner(System.in);
		//input first number		
		System.out.print("Enter the first number : ");				
		int first = sc.nextInt();
		//input second number
		System.out.print("Enter the second number : ");				
		int second = sc.nextInt();
		//conditions
		if(first > second)											
			System.out.println(first+" is greater than "+second);
		else if(second > first)
			System.out.println(second+" is greater than "+first);
		else
			System.out.println("Both numbers are Equal");
		//closing scanner class(not compulsory, but good practice)
		sc.close();													
	}
}