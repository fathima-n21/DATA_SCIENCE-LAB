num=int(input("Enter a number: "))
rev=0
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    rev= rev*10+digit
    num=num//10
print("Reverse: ",rev)
print("Sum of digits: ",sum)