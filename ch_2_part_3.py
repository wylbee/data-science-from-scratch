def add(a, b):
	return a + b

assert add(10, 5) == 15, "+ is valid for numbers"
assert add([1, 2], [3]) == [1, 2, 3], "+ is valid for lists"
assert add("hi", "there") == "hi there", "+ is valid for strings"

try:
	add(10, "five")
except TypeError:
	print("cannot add an int to a string")

def total(xs: list) -> float:
	return sum(total)

from typing import List 

def total(xs: List[float]) -> float:
	return sum(total)

x: int = 5

values = []
best_so_far = None

from typing import Optional

values: List[int] = []
best_so_far: Optional[float] = None # allowed to be either a float or none.

# the type annotations in this snippet are all unecessary
from typing import Dict, Iterable, Tuple

# keys are strings, values are ints
counts: Dict[str, int] = {'data': 1, 'science': 2}

# lists and generators are both iterable
if lazy:
	evens: Iterable[int] = (x for x in range(10) if x % 2 == 0)
else:
	evens = [0, 2, 4, 6, 8]

# tuples specify a type for each element
triple: Tuple[int, float, int] = (10, 2.3, 5)

from typing import Callable

# The type hint says that repeater is a function that takes
# two arguments, a string and an int, and return a string.
def twice(repeater: Callable[[str, int], str], s: str) -> str:
	return repeater(s, 2)

def comma_repeater(s: str, n: int) -> str:
	n_copies = [s for _ in range(n)]
	return ', '.join(n_copies)

assert twice(comma_repeater, "type hints") == "type hints, type hints"

Number = int 
Numbers = List[Number]

def total(xs: Numbers) -> Number:
	return sum(xs)