#This program converts weight between pounds and kilograms. It prompts the user to input their weight and the unit of measurement (either pounds or kilograms). Depending on the unit provided, it performs the appropriate conversion and displays the result.
weight = float(input('Weight: '))
unit =input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight // 0.45
    print(f"You are {converted} pounds")
    