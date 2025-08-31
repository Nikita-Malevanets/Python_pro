import math


def calculate_circle_area(radius:float) -> float:
    """ Function calculate the area of circle """
    area = radius * radius * math.pi
    return area


print(f"Area of circle is {calculate_circle_area(float(input("Enter radius: ")))}")



