# Assignment: Multiples, Sum, Average
# This assignment has several parts. All of your code should be in one file that is well commented to indicate what each
# block of code is doing and which problem you are solving. Don't forget to test your code as you go!
#
# Multiples
# Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

for count in range(1,1000):
    if count%2 !=0:
        print(count)

# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
for count in range(5,1000000):
    if count%5 ==0:
        print(count)
# Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
sum = 0
for count in a:
    sum = sum + count
print(sum)

# Average List
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
a1 = [1, 2, 5, 10, 255, 3]
average = 0
sum1 = 0
for count in a1:
    sum1 = sum1+count
average = sum1 / len(a1)
print(average)
