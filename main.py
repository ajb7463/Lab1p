temp = float(input("Enter temperature: "))
unit = input("Enter unit in F/f or C/c: ")
x = (temp - 32) * 5/9
y = (temp * 1.8) + 32
if unit == "F" or unit == "f":
  print(f"{temp}° in Fahrenheit is equivalent to {x}° Celsius.")
elif unit == "C" or unit == "c":
  print(f"{temp}° in Celsius is equivalent to {y}° Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")