public class LCMOfTwoNumbers {
   public static void main(String args[]){
      int a, b, max, step, lcm = 0;
      Scanner sc = new Scanner(System.in);
      System.out.println("Enter first number ::");
      a = sc.nextInt();
      System.out.println("Enter second number ::");
      b = sc.nextInt();

      if(a > b){
         max = step = a;
      }
      else{
         max = step = b;
      }

      while(a!= 0) {
         if(max % a == 0 && max % b == 0) {
            lcm = max;
            break;
         }
         max += step;
      }
      System.out.println("LCM of given numbers is :: "+lcm);
   }
}