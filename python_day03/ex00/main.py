from NumPyCreator import NumPyCreator

obj = NumPyCreator()

x = obj.from_list([[1,2,3],[6,3,4]])
print(x)

x = obj.from_tuple(("a", "b", "c"))
print(x)

x = obj.from_iterable(range(5))
print(x)

shape = (3, 5)
x = obj.from_shape(shape)
print(x)

x = obj.random(shape)
print(x)

x = obj.identity(4)
print(x)
