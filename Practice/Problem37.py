''' Develop a program that prints all numbers from 1 to 100 that are divisible by 3
or 5 but not both. Use continue or break statements wherever suitable.'''


for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        continue
    if num % 3 == 0 or num % 5 == 0:
        print(num)