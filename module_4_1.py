from fake_math import divide as a_divide

from true_math import divide as b_divide

result1 = a_divide(69, 3)
result2 = a_divide(3, 0)
result3 = b_divide(49, 7)
result4 = b_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)

