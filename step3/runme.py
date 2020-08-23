from polygon import Polygon
from ellipse import Ellipse

val1 = int(input("Enter your value 1: "))
val2 = int(input("Enter your value 2: "))

poly = Polygon()
ellipse = Ellipse()


print("area rectangle: " + str(poly.rectangle(val1, val2)))
print("area triangle: " + str(poly.triangle(val1, val2)))
print("area circle: " + str(ellipse.circle(val1)))

