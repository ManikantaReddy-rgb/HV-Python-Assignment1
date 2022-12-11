num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
num4 = int(input("Enter fourth number:"))
num5 = int(input("Enter fifth number:"))
x = open("sumoutput.txt", "a")
print("The given numbers are:",num1,num2,num3,num4,num5)
print("The given numbers are:",num1,num2,num3,num4,num5,file=x)
if (num1>0 and num2>0 and num3>0 and num4>0 and num5>0):
    sum = num1+num2+num3+num4+num5
    print("The sum of given numbers is:",sum)
    print("The sum of given numbers is:",sum,file=x)
else:
    print("Enter positive numbers only")














# num = [int(input("Enter Five numbers:")) for _ in range(5)]
# x = open("sumoutput.txt", "a")
# print("the given inputs are:",num,file=x)
# print("Sum of given inputs is:",sum(num))
# print("Sum of given inputs is:",sum(num), file=x)