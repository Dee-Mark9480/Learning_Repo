#This is a Branch
n = int(input("Enter your Number: "))
temp = n
sum = 0

while (n > 0):
    dig = n%10
    sum = (sum * 10) + dig
    n = n//10

if (temp == sum):
    print("It is a Palindrome.")
else:
    print("It is not a Palindrome.")
