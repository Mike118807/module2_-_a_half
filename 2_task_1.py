# Task 1: Identify the Greatest- Write a Python program that asks the user to enter three numbers. 
# Your code should then identify and print out the largest number among the three.


num_A = float(input("Enter number for A: "))

num_B = float(input("Enter number for B: "))

num_C = float(input("Enter number for C: "))


# Calculate the largest number out of the three selected.

if num_A >= num_B and num_A >= num_C:
    largest = num_A
elif num_B >= num_A and num_B >= num_C:
    largest = num_B
else:
    largest = num_C

# Print your results

print ("The largest number is:", largest)
