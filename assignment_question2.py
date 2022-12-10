Car = {}
x = open("Cars.txt", "a")
brandname = input("enter the Brand name:")
color = input("enter color:")
Car = {brandname:color}
print(Car,file=x)
print(Car)