#Task 2:Create a function `is_even_or_odd` that takes a number and returns whether it is even or odd.

def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
num1 = 7
print(f"{num1} is {is_even_or_odd(num1)}")   # Output: 7 is Odd

num2 = 10
print(f"{num2} is {is_even_or_odd(num2)}")  # Output: 10 is Even

num3 = 0
print(f"{num3} is {is_even_or_odd(num3)}")  # Output: 0 is Even
