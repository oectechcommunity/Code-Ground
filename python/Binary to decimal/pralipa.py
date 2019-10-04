print("Enter 'X' for exit.");
binary=input("Enter a number in binary form : ");
if binary == 'X':
        exit();
else:
        decimal = int(binary, 2);
        print(binary,"in Decimal =",decimal);
