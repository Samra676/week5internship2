#Create a module named `math_tools.py` with a function `multiply(x, y)` and use it in another script.


# main.py

from math_tools import multiply

# Do numbers
num1 = 6
num2 = 7

# Function ko call karke result nikalna
result = multiply(num1, num2)

# Result print karna
print(f"The result of multiplying {num1} and {num2} is: {result}")
