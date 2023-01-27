# QuinticPolynomial.py
#
# Author: Omar Gabr
# This file solves for an approximation to a quintic polynomial


# store constant terms in list
c_list = []
# store constant terms of derivative in different list
dc_list = []

for c in range(6):
    # ask user for coefficients of quintic polynomial and add to c_list
    c_i = int(input(f"Enter x^{c} coefficients: "))
    c_list.append(c_i)
    # calculate new constants after derivative and add to dc_list
    dc_i = c_i * c
    dc_list.append(dc_i)

# ask user for guess answer
x_0 = float(input("Enter guess: "))

# create a function that computes the polynomial
# input parameters are (1) list + (2) x-value
def poly(list, x):
    # the sum of the polynomial and i_th exponent are initialized
    sum = 0
    i = 0
    # for each element: (1) multiply with its corresponding x-term (2) then increment exponent
    for element in list:
        sum += element * (x ** i)
        i += 1
    # return sum of the polynomial
    return sum

# create list of  approximations
x_list = []
# calculate x_i terms
for i in range(60):
    # only when i is first value in range
    if (i == 0):
        # initialize x_i value as x_0 guess term
        x_i = x_0
    try:
        # initialize f(x) and f'(x) using poly function and pass x_i as input
        fx_i = poly(c_list, x_i)
        fdx_i  = poly(dc_list, x_i)
        # compute following x approximation using previous x_value
        x_i = x_i - (fx_i / fdx_i)
        # append each approximation into list
        x_list.append(x_i)
    except ZeroDivisionError:
        print("Division By Zero")
        break
print(f"An approximate solution to the quintic polynomial is: {x_list[-1]:.9f}")
