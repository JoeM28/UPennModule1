#Question 2.1 : Use x = np.random.randint(0, 1000, size = (10, 10)) to generate 10x10 array
#and use a for loop to find out how many even numbers are in it.

import numpy as np

np.random.seed(15)

x = np.random.randint(0, 1000, size = (10, 10))

print(x)

count_even= 0
for i in range(10):
    for j in range(10):
        if(x[i, j] % 2 == 0):
            #print(x[i, j])
            count_even += 1
            #print("Even Counter : ", count_even)

print("Number of Even numbers in the array : ", count_even)

#Question 2.2 : Randomly generate an 8x9 array from a normal distribution with mean = 1, sigma = 0.5.
#Calculate the mean of elements whose indexes have a relation of (i+j)%5 == 0
#(i is row index and j is column index).

np.random.seed(25)

arr_norm = np.random.normal(loc=1, scale=0.5, size=(8, 9))
print(arr_norm)

mean_elem = 0
sum_elem = 0
counter = 0
for i in range(8):
    for j in range(9):
        if( (i+j) % 5 == 0):
            counter += 1
            sum_elem += arr_norm[i, j]
mean_elem = sum_elem / counter
print("Count of indexes : " , counter)
print("Sum of indexes   : " , sum_elem)
print("Mean of indexes  : " , mean_elem)
