# This is a function


def func():
    return True
    return False


## Example 1
# This is a generator


def gen():
    yield True
    yield False
    yield False


# Generators are a special type of function that can be used to create iterators (sequences of values).
# They are similar to functions, but instead of returning a single value, they yield a sequence of values.
# When a generator is called, it returns an iterator object that can be used to iterate over the values that the generator yields.
# You get values in the order that they are yielded.
#
# Note: the function is only executed ONCE, when the generator is created.
#
# Note: generators are lazy, which makes then very memory efficient.
#
# so the way it seems to work is that the function is run until the first yield, then is pauses. When the next value is requested, the function is resumed from where it left off until the next yield, and so on.

for val in gen():
    print(val)

# is equivalent to:

for val in [True, False, False]:
    print(val)

## Example 2


# This is a generator, but it is infinite
# this demonstrates that generators are lazy (if they weren't, this would run forever)
def flip_flop():
    val = True
    while True:
        yield val
        val = not val


# generate the first 10 values
for i, val in enumerate(flip_flop()):
    print(i, val)
    if i == 10:
        break
