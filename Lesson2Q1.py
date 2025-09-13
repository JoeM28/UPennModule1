#Question 1.1: Use the randn function to create an array with a dimension of 5X5 and use a for loop to calculate the sum of all elements in the diagonal of the array.
import numpy as np

np.random.seed(22)
arr=np.random.rand(5,5)
print(arr)
diagsum=0
for i in range(5):
    diagsum += arr[i,i]
print("Diagonal Sum = ", diagsum)
#print(np.trace(arr))

#Question 1.2: Choose any three functions to apply to this array

average_arr=np.average(arr)
print(average_arr)

median_arr=np.median(arr)
print(median_arr)

max_arr=np.max(arr)
print(max_arr)

min_arr=np.min(arr)
print(min_arr)

stddev_arr=np.std(arr)
print(stddev_arr)

#Explaination of the CODE in Sentences

#np.average(arr)
#This calculates the arithmetic mean of all elements in the array by adding up all numbers and dividing by the total count of elements.

#np.median(arr)
#This finds the middle value when all elements in the array are sorted from smallest to largest - if there's an even number of elements, it takes the average of the two middle values.

#np.max(arr)
#This finds and returns the largest numerical value present anywhere in the array.

#np.min(arr)
#This finds and returns the smallest numerical value present anywhere in the array.

#np.std(arr)
#This calculates the standard deviation, which measures how spread out the numbers are from the mean - a larger standard deviation means the numbers are more scattered, while a smaller one means they're clustered closer to the mean.