                  # print numbers from 1 to 10 using for loop
for x in range(1,11):
  print(x)

            # print even numbers between 1 and 100 using while loop
# a=2
# while a<=100:
#     print(a)
#     a+=2

                 # print the multiplication table of any number    
# num=5
# i=1
# while(i<=10):
#     # print(f"{num} x {i} = {num * i}")
#     print(num,"x",i,"=",num*i)
#     i+=1

                   # print the sum of all numbers from 1 to n
# n = int(input("Enter a number: "))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print(f"The sum of numbers from 1 to {n} is {sum}")

                      # count digits in a number
# num=12345
# count=0
# while num!=0:
#     num//=10
#     count+=1
# print(count)

                          # reverse the digits in a number
# num=1234
# reverse=0
# while num!=0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num//=10
# print(reverse)

                                 # factorial of the number
# num=4
# fact=1
# i=1
# while i<=num:
#     fact*=i
#     i+=1
# print(fact)

                                # # print first 10 fibonacci numbers
# a=0
# b=1
# count=0
# while count<10:
#     # print(a)
#     c=a+b
#     a=b
#     b=c
#     count+=1


                                        # # palindrome
# i=int(input("Enter the number"))
# reverse=0
# x=i
# while i>0:
#     reverse=reverse*10+i%10
#     i=i//10
# print(reverse) # reverse of a number
# if reverse==x:
#     print("is palindrome")
# else:
#     print("not palindrome")

                           # # sum of digits of a number
# i=int(input("Enter a number"))
# sum=0
# while (i>0):
#     sum=sum+i%10
#     i=i//10
# print(sum)


                       # product of digits of a number
# i=int(input("Enter a number"))
# Product=1
# while (i>0):
#     Product=Product*(i%10)
#     i=i//10
# print(Product)

                         # print the sum of even digits 
# i=int(input("Enter a number"))
# Sum=0
# while i>0:
#     digit=i%10
#     if digit%2==0:
#         Sum+=digit
#     i//=10
# print(Sum)

                            #Smallest digit in a number
# num =368917
# smallest = 9  # Start with the largest possible digit
# while num > 0:
#     digit = num % 10
#     if digit < smallest:
#         smallest = digit
#     num = num // 10
# print("Smallest digit is:", smallest)


                                     # vowels
# text = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = 0
# for char in text:
#     if char in vowels:
#         count += 1
# print("Number of vowels:", count)

                               # triangle using * pattern
# rows = int(input("Enter number of rows: "))
# for i in range(1, rows + 1):
#     print("*" * i)

                          # # print odd numbers using do while loop
# num = 1
# while True:
#     if num % 2 != 0:
#         print(num)
#     num += 1
#     if num > 50:
#         break

