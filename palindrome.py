i=int(input("Enter the number"))
reverse=0
x=i
while i>0:
    reverse=reverse*10+i%10
    i=i//10
print(reverse) # reverse of a number
if reverse==x:
    print("is palindrome")
else:
    print("not palindrome")


