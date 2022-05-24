from .area.polygon import Polygon
from .area.ellipse import Ellipse
from .arith.basic import Basic

def main():
    val1 = float(input("Enter your value 1: "))
    val2 = float(input("Enter your value 2: "))

    poly = Polygon()
    print("area rectangle: " + str(poly.rectangle(val1, val2)))
    print("area triangle: " + str(poly.triangle(val1, val2)))

    ellipse = Ellipse()
    print("area circle: " + str(ellipse.circle(val1)))

    basic = Basic()
    print("add: " + str(basic.add(val1, val2)))
    print("subtract: " + str(basic.subtract(val1, val2)))
    print("multiply: " + str(basic.multiply(val1, val2)))
    print("divide: " + str(basic.divide(val1, val2)))

if __name__ == '__main__':
    main()