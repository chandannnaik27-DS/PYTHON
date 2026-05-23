   
# def collatz_sequence(n):
#     sequence = [n]
    
#     # Continue applying rules until the number reaches 1
#     while n != 1:
#         if n % 2 == 0:
#             n = n // 2  # Integer division for even numbers
#         else:
#             n = 3 * n + 1  # 3n + 1 rule for odd numbers
#         sequence.append(n)
    
#     return sequence

# try:
#     num = int(input("Enter a positive integer: "))
#     if num <= 0:
#         print("Please enter a number greater than 0.")
#     else:
#         result = collatz_sequence(num)
#         print(f"Collatz Sequence: {result}")
#         print(f"Total steps: {len(result) - 1}")
# except ValueError:
#     print("Invalid input! Please enter a whole number.")


# # 2D Table (Multiplication) 
# for i in range(1, 4):
#      for j in range(1, 4):
#         print(i * j, end="\t") 
#      print()

# n = int(input("Enter the number:"))
# for i in range(1,11):
#     # result = n*
#     print(f"{n} X {i} = {n*i}")
    

for i in range(10): 
    if i == 3:
        continue
    print(i)

for i in range(10):
    if i == 7:
        break
    print(i)