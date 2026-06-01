import math

true_value1 = 865240
approx_value1 = 865200
true_value2 =  37.46235
approx_value2 = 37.46

absolute_error1 =  abs(true_value1-approx_value1)
relative_error1 = absolute_error1/true_value1
percentage_error1 = relative_error1 * 100

absolute_error2 =  abs(true_value2-approx_value2)
relative_error2 = absolute_error2/true_value2
percentage_error2 = relative_error2 * 100

print("ERROR CALCULATIONS")
print("Absolute Error 1:",absolute_error1)
print("Relative Error 1:",relative_error1)
print("Percentage Error 1:",percentage_error1)

print("Absolute Error 2:",absolute_error2)
print("Relative Error 2 :",relative_error2)
print("Percentage Error 2:",percentage_error2)