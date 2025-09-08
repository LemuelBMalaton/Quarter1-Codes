import math
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
x3 = x2 - x1
y3 = y2 - y1
d = math.sqrt(pow(x3, 2)+pow(y3, 2))
print("The distance between the two points is: " + f"{d:.2f}")
