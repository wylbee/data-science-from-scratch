# %% codecell
# Modules

import re
my_regex = re.compile("[0-9]+", re.I)

from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

# %% codecell
# Funcetions
def double(x):
    """
    This is where you put an optional docstring that explains what the function
    does. For example, this function multiplies its input by 2.
    """
    return x * 2

def apply_to_one(f):
    """Calls the function f with 1 as its argument"""
    return f(1)

my_double = double
x = apply_to_one(my_double)

y = apply_to_one(lambda x: x + 4)

another_double = lambda x: 2 * x

def another_double(x):
    """Do this instead"""
    return 2 * x


def my_print(message = "my default message"):
    print(message)

my_print("hello")
my_print()

def full_name(first = "What's-his-name", last = "something"):
    return first + " " + last

full_name("Joel", "Grus")
full_name("Joel")
full_name(last="Grus")

# %% codecell
# Strings

single_quoted_string = 'data science'
double_quoted_string = "data science"

tab_string = "\t"
len(tab_string)

not_tab_string = r"\t"
len(not_tab_string)

multi_line_string = """This is the first line.
and this is the second line
and this is the third line."""

first_name = "Joel"
last_name = "Grus"

full_name1 = first_name + " " + last_name
full_name2 = "{0} {1}".format(first_name, last_name)
full_name3 = f"{first_name} {last_name}"

# %% codecell
# Exceptions
try:
    print(0 / 0)
except ZeroDivisionError:
    print("don't do that")

# %% codecell
# Lists
integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]

list_length = len(integer_list)
list_sum = sum(integer_list)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

zero = x[0]     # equals 0, lists are 0-indexed
one = x[1]      # equals 1,
nine = x[-1]    # equals 9, 'Pythonic' for last element
eight = x[-2]   # equals 8, 'Pythonic' for next to last element
x[0] = -1       # now x is [-1, 1, 2, 3, ..., 9]

first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]

every_third = x[::3]
five_to_three = x[5:2:-1]

every_second = x[::2]
every_second

1 in [1, 2, 3]
0 in [1, 2 ,3]

x = [1, 2, 3]
x.extend([4, 5, 6])

x = [1, 2, 3]
y = x + [4, 5, 6]

x =  [1, 2, 3]
x.append(0)
y = x[-1]
z = len(x)

x, y = [1, 2]

_, y =  [1, 2]

# %% codecell
# Tuples
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple =  3, 4
my_list[1] = 3

try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")

def sum_and_product(x, y):
    return (x + y), (x * y)

sp = sum_and_product(2, 3)
s, p = sum_and_product(5, 10)

x, y = 1, 2
x, y = y, x

# %% codecell
# Dictionaries
empty_dict = {}     # Pythonic
empty_dict2 = dict()
grades = {"Joel": 80, "Tim": 95}

joels_grade = grades["Joel"]

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

joel_has_grade = "Joel" in grades
kate_has_grade = "Kate" in grades

joels_grade = grades.get("Joel", 0)
kates_grade = grades.get("Kate", 0)
no_ones_grades = grades.get("No one")

grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)

tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()

"user" in tweet_keys
"user" in tweet         #"Pythonic"
"joelgrus" in tweet_values

# defaultdict
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

from collections import defaultdict

word_counts = defaultdict(int)
for word in document:
    word_counts[word] += 1

dd_list = defaultdict(list)
dd_list[2].append(1)

dd_dict = defaultdict(dict)
dd_dict["Joel"]["City"] = "Seattle"

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1

# %% codecell
# Counters

from collections import Counter
c = Counter([0, 1, 2, 0])

word_counts = Counter(document)

# prints the 1- most common words and their counts
for word, count, in word_counts.most_common(10):
    print(word, count)

# %% codecell
# Sets
primes_below_10 = {2, 3, 5, 7}

s = set()
s.add(1)
s.add(2)
s.add(2)
x = len(s)
y = 2 in s
z = 3 in s

stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]

"zip" in stopwords_list     # False, but have to check every element

stopwords_set = set(stopwords_list)
"zip" in stopwords_set      # very fast to check

item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)
item_set = set(item_list)
num_distinct_items = len(item_set)
distinct_item_list = list(item_set)

# %% codecell
# Control Flow
