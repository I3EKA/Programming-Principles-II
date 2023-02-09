# %% [markdown]
# # Python Classes
# 
# 1. Define a class which has at least two methods:
# `getString`: to get a string from console input
# `printString`: to print the string in upper case.
# 
# 2. Define a class named `Shape` and its subclass `Square`. The `Square` class has an `init` function which takes a `length` as argument. Both classes have a `area` function which can print the area of the shape where Shape's area is 0 by default.
# 
# 3. Define a class named `Rectangle` which inherits from `Shape` class from task 2. Class instance can be constructed by a `length` and `width`. The `Rectangle` class has a method which can compute the `area`.
# 
# 4. Write the definition of a Point class. Objects from this class should have a
#     - a method `show` to display the coordinates of the point
#     - a method `move` to change these coordinates
#     - a method `dist` that computes the distance between 2 points
# 
# 5. Create a bank account class that has attributes `owner`, `balance` and two methods `deposit` and `withdraw`. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
# ```python
# class Account:
#     pass
# ```
# 
# 6. Write a program which can filter prime numbers in a list by using `filter` function.
# Note: Use `lambda` to define anonymous functions.

# %% [markdown]
# #### Bank Account

# %%
class Account():
    owner = ""
    balance = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Owner of an account is: {self.owner}\nAccount balance is: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return "Deposit!!"

    def withdraw(self, amount):
        if (amount <= self.balance):
            self.balance -= amount
            return "Withdraw accepted"
        else:
            return "Withdraw can not be accepted"


acc1 = Account("Bexultan", 1000)
print(acc1)

print(acc1.deposit(50))
print(acc1.withdraw(20))
print(acc1.balance)


# %% [markdown]
# #### Filter Prime

# %%
class Filter_prime():
    def isPrime(self, num):
        if (num < 2):
            return False
        else:
            for i in range(2, num):
                if (num % i == 0):
                    return False
        return True

    def filter_primes(self, listofnums):
        return filter(lambda x: self.isPrime(x), listofnums)


prime_filter = Filter_prime()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(prime_filter.filter_primes(nums))
print(prime_numbers)


# %% [markdown]
# #### Getting and Printing

# %%
class String:
    def getString(self):
        self.userInput = input()

    def printString(self):
        print(self.userInput.upper())


string = String()
string.getString()
string.printString()


# %% [markdown]
# #### Points

# %%
import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, x1, y1):
        self.x += x1
        self.y += y1

    def dist(self, p2):
        newx = math.sqrt((p2.x - self.x) * (p2.x - self.x))
        newy = math.sqrt((p2.y - self.y) * (p2.y - self.y))
        return newx, newy


p1 = Point(5, 4)
p2 = Point(3, 4)

print(p1.show())
p1.move(1, 1)
print(p1.show())
print(p1.dist(p2))


# %% [markdown]
# #### Rectangle

# %%
class Shape():
    def __init__(self):
        pass

    def area(self, length, width):
        return 0


class Rectangle(Shape):
    def __init__(self, length=0, width=0):
        Shape.__init__(self)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


l = int(input())
w = int(input())
r = Rectangle(l, w)
print(r.area())

print(Rectangle().area())


# %% [markdown]
# #### Square

# %%
class Shape():
    def __init__(self) -> None:
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length * self.length


x = int(input())
s = Square(x)
print(s.area())

print(Square().area())


# %% [markdown]
# # Python Function
# 
# 1. A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. 
# `ounces = 28.3495231 * grams`
# 
# 2. Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion:
# `C = (5 / 9) * (F – 32)`
# 
# 3. Write a program to solve a classic puzzle: 
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
# `create function: solve(numheads, numlegs):`
# 
# 4. You are given list of numbers separated by spaces. Write a function `filter_prime` which will take list of numbers as an agrument and returns only prime numbers from the list.
# 
# 5. Write a function that accepts string from user and print all permutations of that string.
# 
# 6. Write a function that accepts string from user, return a sentence with the words reversed.
# `We are ready -> ready are We`
# 
# 7. Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# ```python
# def has_33(nums):
#     pass
# 
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False
# ```
# 
# 8. Write a function that takes in a list of integers and returns True if it contains `007` in order
# ```python
# def spy_game(nums):
#     pass
# 
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False
# ```
# 9. Write a function that computes the volume of a sphere given its radius.
# 
# 10. Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection `set`.
# 
# 11. Write a Python function that checks whether a word or phrase is `palindrome` or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
# 
# 12. Define a functino `histogram()` that takes a list of integers and prints a histogram to the screen. For example, `histogram([4, 9, 7])` should print the following:
# ```
# ****
# *********
# *******
# ```
# 
# 13. Write a program able to play the `"Guess the number"` - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
# ``` 
# Hello! What is your name?
# KBTU
# 
# Well, KBTU, I am thinking of a number between 1 and 20.
# Take a guess.
# 12
# 
# Your guess is too low.
# Take a guess.
# 16
# 
# Your guess is too low.
# Take a guess.
# 19
# 
# Good job, KBTU! You guessed my number in 3 guesses!
# ```
# 
# 14. Create a python file and import some of the functions from the above 13 tasks and try to use them.

# %% [markdown]
# #### Centigrade

# %%
def converter(F):
    C = (5 / 9) * (F - 32)
    return C
print(converter(327))

# %% [markdown]
# #### Filter Primes

# %%
def filter_prime(my_list):
    l = []
    for i in my_list:
        cnt = 0
        if (i == 2):
            l.append(i)
            continue
        elif (i == 1):
            continue
        for j in range(2, i):
            if (i % j == 0):
                cnt += 1
        if (cnt == 0):
            l.append(i)
    return l
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_prime(my_list))

# %% [markdown]
# #### Gram too Unce

# %%
def converter(grams):
    ounces = 28.3495231 * grams
    return ounces
print(converter(234))


# %% [markdown]
# #### Guess

# %%
import random
    

def guessGame():
    guessNumber = random.randint(1, 20)
    tries = 0
    num = 0
    name = input("Hello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    while (num != guessNumber):
        num = int(input("Take a guess\n"))
        tries += 1
        if (num < guessNumber):
            print("\nYour guess is too low.")
        elif (num > guessNumber):
            print("\nYour guess is too big.")

    print(f"Good job, {name}! You guessed my number in {tries} guesses!")


guessGame()


# %% [markdown]
# #### Has 33

# %%
def has_33(nums):
    for i in range(len(nums) - 1):
        if (nums[i] == nums[i+1] == 3):
            return True
    return False


print(has_33([1, 3, 3]))


# %% [markdown]
# #### Histogram

# %%
def histogram(my_list):
    for i in my_list:
        for j in range(i):
            print("*", end="")
        print()


histogram([4, 7, 9])


# %% [markdown]
# #### Import

# %%
import Guess
from Laboratory_3.Python_Functions.Guess import guessGame

guessGame()


# %% [markdown]
# #### Palindrome

# %%
def palindrome(string):
    s = string[::-1]
    if (s == string):
        return True
    return False
print(palindrome('abba'))

# %% [markdown]
# #### Permutation so fastring

# %%
import itertools


def permutations(string):
    perms = [''.join(p) for p in itertools.permutations(string)]
    print(*perms, sep=' ')


permutations("abc")


# %% [markdown]
# #### Rabits and Chikens

# %%
def solve(numheads, numlegs):
    chikens = (numlegs - (4 * numheads)) / -2
    rabits = numheads - chikens
    return f"Rabits: {int(rabits)}\nChikens: {int(chikens)}"


print(solve(35, 94))


# %% [markdown]
# #### Reverse Sentence

# %%
def reverseSentence(s):
    s = s.split(" ")
    l = list(s)
    l.reverse()
    for i in l:
        print(i, end=' ')


reverseSentence("We are ready")


# %% [markdown]
# #### Unique

# %%
def unique(my_list):
    d = {}
    l = []
    for i in my_list:
        if (i not in d):
            d[i] = 1
        else:
            d[i] += 1

    for x, y in d.items():
        if (y == 1):
            l.append(x)
    return l


print(unique([1, 1, 2, 3, 2, 4, 1, 5]))


# %% [markdown]
# ### Volume

# %%
def volume(r):
    return (4/3) * 3.14 * r**3


print(volume(213))


# %% [markdown]
# # Python Function
# 
# ```python
# # Dictionary of movies
# 
# movies = [
# {
# "name": "Usual Suspects", 
# "imdb": 7.0,
# "category": "Thriller"
# },
# {
# "name": "Hitman",
# "imdb": 6.3,
# "category": "Action"
# },
# {
# "name": "Dark Knight",
# "imdb": 9.0,
# "category": "Adventure"
# },
# {
# "name": "The Help",
# "imdb": 8.0,
# "category": "Drama"
# },
# {
# "name": "The Choice",
# "imdb": 6.2,
# "category": "Romance"
# },
# {
# "name": "Colonia",
# "imdb": 7.4,
# "category": "Romance"
# },
# {
# "name": "Love",
# "imdb": 6.0,
# "category": "Romance"
# },
# {
# "name": "Bride Wars",
# "imdb": 5.4,
# "category": "Romance"
# },
# {
# "name": "AlphaJet",
# "imdb": 3.2,
# "category": "War"
# },
# {
# "name": "Ringing Crime",
# "imdb": 4.0,
# "category": "Crime"
# },
# {
# "name": "Joking muck",
# "imdb": 7.2,
# "category": "Comedy"
# },
# {
# "name": "What is the name",
# "imdb": 9.2,
# "category": "Suspense"
# },
# {
# "name": "Detective",
# "imdb": 7.0,
# "category": "Suspense"
# },
# {
# "name": "Exam",
# "imdb": 4.2,
# "category": "Thriller"
# },
# {
# "name": "We Two",
# "imdb": 7.2,
# "category": "Romance"
# }
# ]
# ```
# 
# 1. Write a function that takes a single movie and returns `True` if its IMDB score is above 5.5
# 
# 2. Write a function that returns a sublist of movies with an IMDB score above 5.5.
# 
# 3. Write a function that takes a category name and returns just those movies under that category.
# 
# 4. Write a function that takes a list of movies and computes the average IMDB score.
# 
# 5. Write a function that takes a category and computes the average IMDB score.

# %% [markdown]
# Movie Analyser

# %%
movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]


def is_high_imdb(movie):
    return movie["imdb"] > 5.5


def high_imdb_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]


def movies_by_category(movies, category):
    my_list = []
    for i in movies:
        if (i["category"] == category):
            my_list.append(i["name"])
    return my_list


def average_imdb(movies):
    imdb_scores = [movie["imdb"] for movie in movies]
    return sum(imdb_scores) / len(imdb_scores)


def average_imdb_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb(category_movies)


print(is_high_imdb(movies[0]))
print(high_imdb_movies(movies))
print(movies_by_category(movies, "Romance"))
print(average_imdb(movies))
print(average_imdb_by_category(movies, "Romance"))



