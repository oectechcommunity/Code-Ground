// import java.util.*;
// class factorial
// {
//     public static void main(String args[])
//     {
//     Scanner sc= new Scanner(System.in);
//     System.out.ptintln("Enter a number ");
//     int a = sc.nextInt();
//     int flag=0;
//     for(int i=2;i<a;i++)
//     {
//         if(a%i==0)
//         {
//             flag=1;
//             break;
//         }
//     }
//     if(flag==0)
//     System.out.ptintln("Factorial Number");
//     else
//     System.out.ptintln("Enter a number ");
//     }
// }

class factorial{  
 public static void main(String args[]){  
  int i,fact=1;  
  int number=5;//It is the number to calculate factorial    
  for(i=1;i<=number;i++){    
      fact=fact*i;    
  }    
  System.out.println("Factorial of "+number+" is: "+fact);    
 }  
}  