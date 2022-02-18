# Solving problems in statistics

import math
from my_utils import probability, union_probability
from my_utils.testing import test_equal, test_close
import my_utils.counting as C

print("\nSOME PROBABILITY PROBLEMS\n")

# Question 1
print("Q: Find the probability of getting a head when you toss a fair coin?")
p_head = probability(1, 2)
print(p_head)
print("A: The probability is {}".format(p_head) )
expected_p_head = 0.5
test_equal(p_head, expected_p_head)
print("")

# Question 2
print("Q: Find the probability of getting 3 heads when you toss 10 fair coins.")
p_3_heads = C.combinations(10, 3) / 2**10
print("A: The probability is {}".format(p_3_heads))
expected_p_3_heads = 0.1171875
test_close(p_3_heads, expected_p_3_heads)
print("")

# Question 3
print("Q: Find the probability of getting 4 heads when you toss 10 fair coins.")
p_3_heads = C.combinations(10, 4) / 2**10
print("A: The probability is {}".format(p_3_heads))
expected_p_3_heads = 0.205078125
test_close(p_3_heads, expected_p_3_heads)
print("")

# Question 4
print("Q: Find the probability of getting 5 heads when you toss 10 fair coins.")
p_3_heads = C.combinations(10, 5) / 2**10
print("A: The probability is {}".format(p_3_heads))
expected_p_3_heads = 0.205078125
test_close(p_3_heads, expected_p_3_heads)
print("")