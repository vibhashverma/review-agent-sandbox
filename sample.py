def calc(a, b, op):
    """Perform basic arithmetic calculations."""
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    else:
        return None


def evens(nums):
    """Return a list of even numbers from the given iterable."""
    return [n for n in nums if n % 2 == 0]


class user:
    """A simple user class."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        """Print a greeting message for the user."""
        print("Hello " + self.name + ", you are " + str(self.age))
