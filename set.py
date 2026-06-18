s = set() # empty set and s={} is a dictionary not a set

set = {1, 2, 3, 4, 5}

# Set methods
set.add(6)
set.remove(3)
print(set.pop())
print(set)

# Union and intersection of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
print(set1.intersection(set2))