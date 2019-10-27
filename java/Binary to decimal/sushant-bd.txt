public class BinaryDecimal {
    public static void main(String[] args) {
        long num = 110110111;
        int decimal = convertBinaryToDecimal(num);
        System.out.printf("%d in binary = %d in decimal", num, decimal);
    }
    public static int convertBinaryToDecimal(long num)
    {
        int decimalNumber = 0, i = 0;
        long remainder;
        while (num != 0)
        {
            remainder = num % 10;
            num /= 10;
            decimalNumber += remainder * Math.pow(2, i);
            ++i;
        }
        return decimalNumber;
    }
}
