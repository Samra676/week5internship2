def square_numbers(numbers):
    return [num ** 2 for num in numbers]
nums = [2, 3, 4, 5]
squared = square_numbers(nums)
print(squared)  # Output: [4, 9, 16, 25]
#task 2
def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
