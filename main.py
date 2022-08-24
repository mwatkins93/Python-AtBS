###################
## AtBS Workthrough
## MW
## Aug. 2022
###################

import random

## importing the random module (like R packages)

## Chapter 2 Practice questions
###############################

# 1. Boolean data types are True and False

# 2. and, or and not

# 3. Write the truth tables for the boolean values

## and

## a false b false - a and b false
## a true b false - a and b false
## a false b true - a and b false
## a true b true - a and b true

## or

## a false b false - a or b false
## a true b false - a or b true
## a false b true - a or b true
## a true b true - a or b true

## not

## a false - not a true
## a true - not a false

# 4. What do these expressions equate to?

(5 > 4) and (3 == 5)  # false
not (5 > 4)  # false
(5 > 4) or (3 == 5) # true
(True and True) and (True == False) # false
(not False) or (not True) # true

# 5. Six comparison operators
5 > 4 # greater than
2 < 5 # less than
5 == 5 # equal to
5 != 6 # not equal to
5 >= 4 # greater than or equal to
1 <= 5 # less than or equal to

# 6. Diff bt equal and assignment operator
x = 4 # one equals sign assigns 4 to x
2 == 4 # two equals signs checks if the values equate

# 7. What is a condition and where would you use one?

## A statement needed when we want to check conditions and change the outcome
## of the program. You would use one to print one string when a certain value is
## stored and print another string when a different value is stored

# 8. Identify the three blocks in this code

jam = 0
if jam == 10: # first indent here is block 1
    print('eggs')
    if jam > 5: # second indent here is block 2
        print('bacon')
    else: # third indent here is block 3
        print('ham')
    print('jam')
print('jam')
# 9. Write code that prints Hello if 1 is stored in spam, prints Howdy
# if 2 is stored in spam, and prints Greetings! if anything else is stored
# in spam.

spam = 1
if spam == 1:
    print("Hello")
    if spam == 2:
        print("Howdy")
else:
    print("Greetings")

# 10. How to get out of an infinite loop?

## Press Control + C

## 11. Difference bt break and continue

## Utilising continue will immediately jump back to the start of the loop
## and re-evaluated the loop's condition whereas break will escape the loop
## early

## 12. What is the difference between range(10), range(0, 10)
## and range(0, 10, 1) in a for loop?

for i in range(10): ## results in 10 iterations through the clause
    print("1")

for i in range(0, 10): ## defines a start/end range - starts at zero and
    print("1")         ## ends at 10

for i in range(0, 10, 1): # similar to above, but counts up by intervals of 1
        print("1")

## 13. Print 1 to 10 in a for loop and then in a while loop

for i in range(1, 11):
    print(i)

##

print('Numbers from 1 to 10:')
n = 1  ## set n as 1 initially
while n <= 10: ## while n less than or equal to 10
   print(n) ## print n
   n = n+1 ## but also add 1 to n, as long as n
           ## is less than 10

## 14. Call a function from inside a module

import spam  ## this is importing the module

spam.bacon()  ## calling the function inside the
              ## module

## Chapter 3 - Functions
########################

def hello():
    print("Howdy")
    print("Hello?!")
    print("Hello there.")

hello()

##

def hello(name): ## giving the function a name parameter
    print("Hello there " + name + ". How are you doing today?")

hello("John")

##

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidely so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Try again"
    elif answerNumber == 5:
        return "Ask in two hours"
    elif answerNumber == 6:
        return "Concentrate and ask again"
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outlook not great"
    elif answerNumber == 9:
        return "Highly unlikely"

print(getAnswer(random.randint(1, 9)))

##

spam = print("Hello!")

None == spam

##

print("Hello", sep = "]")

##

print('cats', 'dogs', 'mice', sep = ", ")

##

def spam():
    eggs = 31337
spam()
print(eggs) ## traceback because eggs is not defined in the global scope; only the local!

##

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

##

def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)  ## Prints the global variable because eggs is undefined in the local

##

def spam():
    eggs = "spam local"
    print(eggs)  ## this prints spam local

def bacon():
    eggs = "bacon local"
    spam()
    print(eggs)  ## prints bacon local

eggs = "global"
spam()  ## this will print spam local
bacon() ## this prints eggs from the spam function and eggs from bacon function!
print(eggs)  ## this should do the global egg assignment

##

def spam():
    global eggs  ## telling python to override local variables with the global one
    eggs = "spam"

eggs = "global"
spam()
print(eggs)

## Better feel for global // local scope rules

def spam():
      ## now a global variable
    eggs = "spam"

def bacon():
    eggs = "bacon"  ## this is local!

def ham():
    print(eggs)  ## this is global!

eggs = 42  ## obvs global
spam()
print(eggs)

## Don't assign a local variable after trying to use it - traceback!

def spam():
    print(eggs)
    eggs = "spam baby"  ## Python doesn't know eggs exists yet and will not default to
                        ## global!

eggs = "global"
spam()

##

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Invalid argument!")

print(spam(2))
print(spam(12))
print(spam(0))

## Guess the number game

secretNumber = random.randint(1, 100)
print("I've selected a number between 1 and 100; try to guess it!")

# Give the player 10 guesses
def numbergame():
    secretNumber = random.randint(1, 100)
    print("I've selected a number between 1 and 100; try to guess it!")

    for guessesTaken in range(1, 7):
        print("Take a guess.")
        guess = int(input())

        if guess < secretNumber:
            print("Your guess is too low")
        elif guess > secretNumber:
            print("Your guess is too high")
        else:
            break # because the else condition is the right number!

    if guess == secretNumber:
        print("Great! You guessed my number in " + str(guessesTaken) + " guesses!")
    else:
        print("Good try... The number I selected was " + str(secretNumber))

numbergame()

## Chapter 3 - Practice questions and projects

## 1. Why are functions good to have?

## They allow for more concise code without the use of copy and pasting which can lead to
## error.

## 2. When does the code in a function execute?

## The code in a function executes when it is called!

## 3. What statement creates a function

def

## 4. Diff bt function and a function call

## Defining a function does not execute the code within; the code within is only
## executed during a function call.
## Also syntax - def function() versus function()

## 5. Number of global scopes? local scopes?

## One global scope; local scopes could be infinite as they exist within each defined
## function

## 6. What happens to variables in the local scope when the function call returns

## The variables are forgotten because the local scope is actually destroyed!

## 7. What is a return value? Can it be part of an expression

## the value that a function call evaluates to is the return value. Yes it can be!

## 8. If no return statement, what is the return value of a call to that function

## return None

## 9. Force a variable in a function to refer to the global variable

## use a global statement inside the function

## 10. Data type of None?

## NoneType

## 11. What does this statement do

import areallyourpetsnamederic

## gives a traceback because there is no module of that name!

## 12. How to call bacon() function within the module spam

spam.bacon()

## 13. Prevent a program from crashing when it gets an error?

## You can use try and except commands - place the line of code that might cause an error
## in a try clause

## 14. What goes in the try clause? the except clause?

## Potentially error causing code goes in try. The code that executes if there is an
## error goes in the except clause!

## The Collatz sequence ------------------------------------------------

## Write a function named collatz() that has one parameter named number. Secondly,
## add a try and except statement to nullify entering strings!

def collatz(number):
    if (number % 2 == 0):
        number = number // 2
    elif (number % 2 == 1):
        number = 3 * number + 1
    print(number)
    return(number)
try:
    n = int(input("Choose a number: "))
    while (n != 1):
        n = collatz(n)
except ValueError:
        print("Error: please enter a valid integer!")

## Chapter 4 - Lists
####################
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