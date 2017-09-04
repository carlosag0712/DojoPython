# Assignment: String and List Practice
# Use only the built-in methods and functions from the previous tabs to do the following exercises.
# You will find the following methods and functions useful:
#
# • .find()
#
# • .replace()
#
# • .min()
#
# • .max()
#
# • .sort()
#
# • .len()
#
# Find and Replace
# In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the
# first instance of the word "day". Then create a new string where the word "day" is replaced with
# the word "month".

words = "It's thanksgiving day. It's my birthday,too!"

print(words.find("day"))
wordsMonth = words.replace("day","month",1)
print(wordsMonth)


# Min and Max
# Print the min and max values in a list like this one: x = [2,54,-2,7,12,98].
# Your code should work for any list.

x = [200,2,5,777,-12312312,90]

# max = x[0]
# min = x[0]
#
# for count in x:
#     if max < count:
#         max = count
#
#     if min > count:
#         min = count

print("max",max(x))
print("min",min(x))

# First and Last
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"].
# Now create a new list containing only the first and last values in the original list.
# Your code should work for any list.

x = ["hello",2,54,-2,7,12,98,"world"]
y = [x[0],x[len(x)-1]]
print(y)


# New List
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first.
# Then, split your list in half. Push the list created from the first half to position 0 of the
# list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98].
# Stick with it, this one is tough!

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x = sorted(x) #Sort your list first.
x1stHalf = x[0:int(len(x)/2)]
x2ndHalf = x[int(len(x)/2):]
print(x2ndHalf)

x2ndHalf.insert(0,x1stHalf)

print(x2ndHalf)
