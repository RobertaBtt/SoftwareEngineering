## Generators

Memory is a limited structure.
Generators allow us to solve a very large problem and attack 
one small manageable chunk at a time.

See [__init__.py.infinite_sequence](__init__.py)

Everytime a generator is called, it runs untile
the next

    yield

statement. So I can have more than one **yield** statement.

A Generator is exhausted when it doesn't have a next value to go to,
and eventually it produces a 

    StopIteration error

There is another way to create Generators and those are the
**generator expressions**

    nums_squared = (num**2 for num in range(5))