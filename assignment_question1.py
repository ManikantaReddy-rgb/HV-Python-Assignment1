num = [int(input("Enter Five numbers:")) for _ in range(5)]
x = open("sumoutput.txt", "a")
print("the given inputs are:",num,file=x)
print("Sum of given inputs is:",sum(num))
print("Sum of given inputs is:",sum(num), file=x)