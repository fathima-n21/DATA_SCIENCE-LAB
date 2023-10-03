n=int(input("Enter a positive integer:"))
sum=0
for i in range(2,n+1,2):
    sum+=i**3
print("Sum of cube:",sum)
