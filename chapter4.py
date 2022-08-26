## Chapter 4 - Lists
####################

import copy

[1, 2, 3]

x = ["cat", "bat", "mat", "rat"]

x[2]

"The " + x[0] + " went home."

x[10] # list index out of range error

x[1.1] # can't do float numbers

spam = [["cat", "bat"], [10, 20, 30, 40, 50]]
spam[0][1] # can access a list within a list (entire first list is indexed as 0)

spam[-1][4]

spam = ["cat", "bat", "rat", "mat"]
spam[1:3] # colon slices the list (can select a section of it)
spam[:3] # short only using one side

len(spam) # get number of values in a list with len()

spam[2] = "kangaroo" # can replace a list value by assigning a new one to an index spot
spam[2] = spam[1]
spam

##

[1, 2, 3] + ["A", "B", "C"] # can combine lists with +
[1, 2, 3] * 3 # can multiply lists

##

spam = ["cat", "bat", "rat", "mat"]
del spam[3]
spam

##

catName1 = "Zophie"
catName2 = "Pooka"
catName3 = "Simon"
catName4 = "LadyMacbeth"
catName5 = "Fat"
catName6 = "Miss Cleo"

print("Enter name of cat 1:")
catName2 = input()

catNames = []
while True:
    print("Enter the name of cat " + str(len(catNames) + 1) + " (Or enter nothing to stop.):")
    name = input()
    if name == "":
        break
    catNames = catNames + [name]
print("The cat names are:")
for name in catNames:
    print("  " + name)

##

for i in range(4):
    print(i)

##

supplies = ["pens", "staples", "flames", "binders"]  # make list

for i in range(len(supplies)):  ## iterate through and print the list items with string text
    print("Index " + str(i) + " in supplies is: " + supplies[i])

##

"howdy" in ["hello", "howdy", "trial"]

spam = ["hello", "hi", "howdy", "heyas"]
"cat" in spam

"howdy" not in spam

"cat" not in spam

##

myPets = ["Zophie", "Pooka", "Fat"]
print("Enter a pet name:")
name = input()
if name not in myPets:
    print("I do not have a pet named " + name)
else:
    print(name + " is my pet.")

##

cat = ["fat", "car", "john"]
cat[2] = "disposition"
size, color, disposition = cat
cat

spam = ["hello", "hi", "howdy", "heyas"]
spam.index("hello")
spam.index("hi")

spam.append("moose")
spam.insert(4, "chicken")

##

eggs = "hello"
eggs.append("world") # can't use append on strings, only lists!

bacon = 42
bacon.append(13)

spam
spam.remove("howdy")
spam

spam = ["trial", "by", "trial"]
spam.remove("trial")
spam

##

spam = [2, 6.5, 6.4, 9, 0]
spam.sort()
spam

spam.sort(reverse = True)
spam

spam = ["Ten", 12, 14]
spam.sort()

spam = ["Ten", "nine", "tractor"]
spam.sort()
spam

## Improved Magic 8-ball game with a list:

messages = ["It is so", "Nevermind", "maybe one day", "yes!", "absolutely not...",
            "highly unlikely", "try again", "not so great", "very doubtful"]
print(messages[random.randint(0, len(messages) - 1)])

##

name = "Matt"
name[3]

for i in name:
    print("///--|" + i + "|--///")

##

name[3] = "t"

newName = name[0:2] + "tether"
newName

##

eggs = ("hello", 42, 5)
eggs[0]

eggs[1:2]
len(eggs)
eggs[1] = 9

##

tuple(["cat", "dog", "five"])
list("hello")

##

spam = 34
cheese = spam
cheese
spam = 100
spam
cheese

##

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = "Hello!"
spam
cheese

##

def eggs(parameterX):
    parameterX.append("Hello")

spam = [1, 2, 3]
eggs(spam)
print(spam)

##

spam = ["a", "b,", "c", "d"]
cheese = copy.copy(spam)  # creates a totally new list!
cheese[1] = 42  # so changing this actually changes the list item in cheese
spam
cheese

## Practice questions
#####################

# 1. What is []

# [] or square brackets denotes an empty list

# 2. Assign "hello" to the third value in this list

spam = [2, 4, 6, 8, 10]

spam[2] = "hello"
spam

# 3. What does spam[int("3" * 2) / 11] evaluate to?

spam[3 * 2 / 11] # type error because list indices must be integers
# or slices not floats - list cannot contain equations?

# 4. What does spam[-1] evaluate to?

spam[-1]  # 10

# equals the last item in the list - because negative numbers can return
# list items starting from the end of the list

# 5. What does spam[:2] equate to?

spam[:2] # [2,4] because it is up to 2, not including. So answer the first
# and second values

bacon = [3.14, "cat", 11, "cat", True]
# 6. What does bacon.index("cat") evaluate to?

bacon.index("cat")  # will likely return the index of the
# first value only - 1

# 7. What does bacon.append(99) do to the list?

bacon.append(99)  # attaches 99 to the list
bacon

# 8. What does bacon.remove("cat") do to the list
bacon.remove("cat")  ## removes the first index of cat - 1
bacon

# 9. What are the operators for list concatenation and replication

# To combine lists use +; to replicate a list use * and an
# integer. Eg [1, 2, 3] + [1, 2] or [1, 2, 3] * 3

# 10. Diff bt append() and insert()

# append() will add a string/integer item to the end of an
# existing list whereas insert() can add them anywhere

bacon.append("14") # adds str 14 to end
bacon

bacon.insert(2, 190) # Says: "add 190 to the 2nd index value!
bacon

bacon.insert(0, "hello")
bacon

# 11. Two ways to remove values from lists

# One would be the del statement and the appropriate index
# You can also change the value of certain indexes

del bacon[2]
bacon

bacon[2] = "rest"
bacon

# 12. List a few ways list values are similar to string values

# list = [2, 4, 10]
# string = "Hello, my name is John"

# I know that lists are mutable and strings are not. They are
# similar in 1.

# 13. Difference bt lists and tuples

# 1. Tuples use regular parentheses, not square brackets
# 2. Tuples are immutable, whereas lists are mutable

# 14. How do you type the tuple value that has just the int value
# of 42 in it?

# Put it in a list and use the tuple command?
eggs = [42]
tuple([42])

# 15. How do you get the tuple form of a list value and vice verse?

# use the tuple and list commands!

matt = [5, "hey", "10", 17]
tuple([5, "hey", "10", 17])

john = (10, "hey", 14)
list((10, "hey", 14))

# 16. Variables that "contain" list values don't actually contain the
# list directly, they contain what?

# They contain a reference ID to a specific list. That is why, if you
# normally replicate a list, it actually creates a new list!

matt # original list
cheese = matt # cheese is copying the list reference

cheese[2] = "helloooo" # changing something
cheese
matt # both values stored are referring to the same list so you
# modify both

# 17. Diff bt copy.copy() and copy.deepcopy()

# copy.copy() is used to make a duplicate of a mutable value - for
# example a list

matt
cheese = copy.copy(matt) # copying the list
cheese[2] = 97
cheese # changes here
matt # but not here

# deep.copy() will copy lists contained within a list as well. Hence,
# the deep/depth. It is copying more!


## Practice projects
####################

# 1. Comma code

# Write a function that takes a list value as an argument and returns
# a string with all the items separated by a comma and a space, with and
# inserted before the last item. For example, passing the previous spam list to
# the function would return 'apples, bananas, tofu, and cats'. But your function
# should be able to work with any list value passed to it.

mylist = ["apples", "bananas", "pears", "grapefruit"]

me = [14]

def list_to_string(a_list): # function for the input of a list
    if not a_list: # if input is not a list
        return ""
    elif len(a_list) == 1: # if list is length one, return a string
        return str(a_list[0]) # of the first index of the list
    else:
        body = ", ".join(map(str, a_list[:-1]))
        return "{0} and {1}".format(body, a_list[-1])

list_to_string(me)