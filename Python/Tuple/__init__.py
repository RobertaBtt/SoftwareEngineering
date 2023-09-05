t = (2)  # I create an integer
tt = (2,)  # I create a tuple
tp = 1, 2, 3  # Another tuple

# Swap of two elements in a tuple :
b = 5
a = 6

a, b = b, a  # so now a is 5

# Fibonacci sequence with tuple:

a, b = 0, 1
while a < 30:
    print(a)
    a, b = b, a + b
