# print(dir(5))

def this_function_is_an_object():
  return True


print(dir(this_function_is_an_object))

#output:
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', 
# '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
# '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__',
#  '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__',
#  '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']