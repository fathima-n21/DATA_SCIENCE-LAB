text=input("Enter a text: ")
u_count=0
l_count=0
for char in text:
    if char.isupper():
        u_count+=1
    if char.islower():
        l_count+=1
print("Uppercase count: ",u_count)
print("Lowercase count: ",l_count)