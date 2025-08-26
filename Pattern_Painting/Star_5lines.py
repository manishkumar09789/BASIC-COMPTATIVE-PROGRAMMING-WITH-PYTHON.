n=int(input("Enter the row :"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j==1)or (j==5):
            print("*", end=" ")
        else:
            print(" ",end=" ")    
    print()        