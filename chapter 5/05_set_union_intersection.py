s1 = {1, 34, 5, 6, 7, 8}
s2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(s1 | s2)  # Union of s1 and s2
print(s1.union(s2))  # Union of s1 and s2 using union method    
print(s1 & s2)  # Intersection of s1 and s2
print(s1.intersection(s2))  # Intersection of s1 and s2 using intersection method
print(s1 - s2)  # Difference of s1 and s2
print(s1.difference(s2))  # Difference of s1 and s2 using difference method
print(s1 ^ s2)  # Symmetric difference of s1 and s2
print(s1.symmetric_difference(s2))  # Symmetric difference of s1 and s2
print(s1.isdisjoint(s2))  # Check if s1 and s2 are disjoint
print(s1.issubset(s2))  # Check if s1 is a subset of s2
print(s1.issuperset(s2))  # Check if s1 is a superset of s2
