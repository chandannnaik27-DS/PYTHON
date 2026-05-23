# total=0
# while True:
#   num = float(input("enter a number: "))
#   if num ==0:
#     break
#   total+=num
# print("The sum of the numbers: ",total)



for i in range (1,6):
    print("Table of",i)

    for j in range(1, 11):
        print(i ,"X", j, "=", i * j)

    print()