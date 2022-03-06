#!/usr/bin/python3


def area_of_circle(diameter):
    if not isinstance(diameter, (int, float)):
        raise TypeError("The diameter must be an integer or float")
    elif diameter < 0:
        raise ValueError("The diameter must not be megative")
    else:
        radius = diameter / 2
        return 3.1415926 * radius * radius


def price_of_round_pizza(diameter):
    return 5.00 + 0.05 * area_of_circle(diameter)


def print_area_of_a_circle(diameter):
    result = area_of_circle(diameter)
    print(f"A {diameter} inch circle has an area of {result:.2f} sq. inches.")


def price_a_pizza(diameter):
    result = price_of_round_pizza(diameter)
    print(f"A {diameter} inch pie will cost ${result:.2f}")


def number_of_ideal_slices(diameter):
    width = round(2 * 3.1415926, 2)
    circumference = round(diameter * 3.1415926, 2)
    slices = circumference // width
    waste = circumference % width
    msg = f'A {diameter}" pie can be cut into {slices:.0f} {width:.2f}" slices'
    if waste > 0.5:
        msg += f', but wastes {waste:.2f}"'
    print(msg + ".")


def forEach(dataset, operation):
    for element in dataset:
        try:
            operation(element)
        except Exception as e:
            print(f"Error doing {operation.__name__} on value {element}: {e}")


pie_sizes = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, "Personal Pan"]

forEach(pie_sizes, print_area_of_a_circle)
forEach(pie_sizes, price_a_pizza)
forEach(pie_sizes, number_of_ideal_slices)

