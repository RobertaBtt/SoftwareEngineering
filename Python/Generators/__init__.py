"""The code is pausing at the "yeld" point
This is called "state".

The function remembers where it was last time.


"""
def infinite_sequence():
    num = 0
    while 1:
        yield num
        num += 1


"""Generator expression"""
nums_squared = (num ** 2 for num in range(5))
next(nums_squared) # It calls the numbers
