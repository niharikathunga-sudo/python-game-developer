x={2,7,3,9,5}
print(x)
# a set is not indexable 
# to add an item to a set
x.add(6)
print(x)
# to remove an item in a set
x.remove(3)
print(x)
# frozenset
y=frozenset(x)
#y.add(10)
print(y)