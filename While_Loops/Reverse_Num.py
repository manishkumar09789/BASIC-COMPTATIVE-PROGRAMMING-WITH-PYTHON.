Num=int(input("Enter The Number : "))
Rev=0
while(Num>0):
    Digit=Num%10
    Num=Num//10
    Rev=Rev*10+Digit
print(Rev)    