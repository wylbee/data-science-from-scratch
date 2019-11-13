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
