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


pie_sizes = [8, 12, 16, 20, "Personal Pan"]

show = True

while show:
    for size in pie_sizes:
        try:
            print(f"{size} inch pie will cost {price_of_round_pizza(size):.2f}")
        except (TypeError, ValueError):
            print(f'"{size}" is not a valid size for a pizza')

    show = input("Do you want to try again? (Y/N): ") in ["Y", "y"]
