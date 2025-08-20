Year=int(input("Enter The Year : "))
if(Year%400==0) or (Year%4==0) and (Year%100!=0):
    print(Year,", It is Leap Year...")
else:
    print(Year,", It is not Leap Year....")    