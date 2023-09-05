## List

- They can collect eterogeneous types of data (arbitrary objects)
- Are ordered 
- Are **mutable** which means that the content can be changed without change their identity

- Can be accessed by an index
- Can be nested


### What is a shallow copy

It has a sense of talking about deep copy or shallow copy only for 
compounded objects like **classes** or **lists**.

When we use the operator "="

    y=x

we are just creating a new reference to the original object.

To actually make a copy, we use the method

    copy

    list1 = [1,3,4,3,1,5,4]
    list2 = copy.copy(list1)
    list3 = copy.deepcopy(list1)

**Deep copy** copies all the objects in a recursive mode, in another object, 
so the changes in the original objects will not be reflected in the second one (the deep copy).

If I change the element in list2:

    list2[2,0] = 7

this change will be reflected also in the list1 because it is a shallow copy.

