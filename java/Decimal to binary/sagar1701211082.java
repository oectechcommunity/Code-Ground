class DecimalBinary{
 
  public void convertBinary(int num){
     int binary[] = new int[40];
     int index = 0;
     while(num > 0){
       binary[index++] = num%2;
       num = num/2;
     }
     for(int i = index-1;i >= 0;i--){
       System.out.print(binary[i]);
     }
  }
 
  public static void main(String a[]){
     DecimalBinary obj = new DecimalBinary();
     System.out.println("Binary representation of 124: ");
     obj.convertBinary(124);
     System.out.println("\nBinary representation of 45: ");
     obj.convertBinary(45);
     System.out.println("\nBinary representation of 999: ");
     obj.convertBinary(999);
  }
}