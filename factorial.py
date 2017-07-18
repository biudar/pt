def factorial(number):
    product = 1
    for i in range(number):
        product = product * (i + 1)
    return product


number = input('enter a non-negative integer to take the factorial of:')
product_output = factorial(number)
print product_output