
A = {'a', 'b', 'c', 'd', 'f', 'g', 'j'}
B = {'b', 'c', 'd', 'h', 'i', 'j', 'k'}
C = {'c', 'd', 'f', 'h', 'k', 'l', 'm', 'o'}

elements_in_A_and_B = A.intersection(B)
print(f"Elements in A and B: {elements_in_A_and_B} -> Count: {len(elements_in_A_and_B)}")

elements_in_B_not_in_A_and_C = B - (A.union(C))
print(f"Elements in B not in A and C: {elements_in_B_not_in_A_and_C} -> Count: {len(elements_in_B_not_in_A_and_C)}")

print("\nc. Show the following using set operations:")

result_i = B - A.union(C) | B.intersection(C)
print(f"i. {result_i}")

result_ii = A.intersection(B).intersection(C)
print(f"ii. {result_ii}")

result_iii = B.intersection(A).union(B.difference(C))
print(f"iii. {result_iii}")

result_iv = A.intersection(B).intersection(C)
print(f"iv. {result_iv}")

result_v = A.intersection(B).intersection(C).intersection(C)
print(f"v. {result_v}")

result_vi = C - (A.union(B))
print(f"vi. {result_vi}")
