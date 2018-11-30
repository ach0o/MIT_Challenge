"""
6.0002 Introduction to Computational Thinking and Data Science

Assignment
(https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/assignments/)

Problem Set 1B

Solved by achooan
- couldn't possibly solved with the implementation of the dynamic programming.
- credit to @tuthang102 for the insights on solving this problem
"""

# 6.0002 Problem Set 1b: Space Change
# Author: charz, cdenise


# ================================
# Part B: Golden Eggs
# ================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo={}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.

    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)

    Returns: int, smallest number of eggs needed to make target weight
    """
    min_eggs = target_weight

    if memo.get(target_weight, 0) > 0:
        # check memo if it's already computed
        return memo[target_weight]

    elif min_eggs in egg_weights:
        # check if it's one of the egg weights
        memo[min_eggs] = 1
        return 1

    else:
        for egg in egg_weights:
            if egg > target_weight:
                continue

            # add up the minimum possible num of eggs at the target weight
            num_eggs = 1 + \
                dp_make_weight(egg_weights, target_weight - egg, memo)

            # check if the num of eggs is less than the minimum
            if num_eggs < min_eggs:
                # replace the minimum with the current num of eggs
                min_eggs = num_eggs

                # update memo with the minimum num of eggs
                # at the current target weight
                memo[target_weight] = min_eggs

    return min_eggs


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
