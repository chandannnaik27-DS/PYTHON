# # Write a program to count even and odd numbers from a list


# list = [10, 4, 3, 9, 12, 4, 13, 15, 11]

# even_count = 0
# odd_count = 0
# for i in list:
#     if i % 2 == 0:
#         even_count += 1
#     else :
#         odd_count += 1

# print("Even number count =", even_count)
# print("Even number count =", odd_count)
    

# Function to calculate factorial
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Taking input from user
num = int(input("Enter a number: "))

# Display the result
print(f"The factorial of {num} is {factorial(num)}")
    
