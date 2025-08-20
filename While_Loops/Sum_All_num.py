Num=int(input("Enter the numbers : "))
Sum=0
while(Num>0):
    Digit=Num%10
    Num=Num//10
    Sum+=Digit
print(Sum)    