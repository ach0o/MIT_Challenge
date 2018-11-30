"""
6.0002 Introduction to Computational Thinking and Data Science

Assignment
(https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/assignments/)

Problem Set 1

Solved by achooan
"""

# 6.0002 Problem Set 1a: Space Cows

from ps1_partition import get_partitions
import time

# ================================
# Part A: Transporting Space Cows
# ================================

# Problem 1


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows = dict()

    with open(f'./{filename}', 'r') as f:
        for line in f:
            name, weight = line.strip().split(',')
            cows[name] = int(weight)
    return cows

# Problem 2


def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # ordered_cows = sorted(cows.items(), key=lambda x: x[1], reverse=True)

    def greedy_trip(cows, limit, result=[]):
        new_cows = cows.copy()
        total_wei = 0

        if len(cows) <= 1:
            return result.append(list(cows))

        cows_onboard = []
        for name, wei in cows.items():
            if total_wei + wei <= limit:
                total_wei += wei
                cows_onboard.append(name)
                del new_cows[name]

        result.append(cows_onboard)
        greedy_trip(new_cows, limit, result)
        return result

    return greedy_trip(cows, limit)

# Problem 3


def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    all_trip_parts = get_partitions(cows)

    def is_trip_valid(trip, memo={}):
        for t in trip:
            weight = sum([cows[name] for name in t])
            if weight > limit:
                return False
        return True

    result = []
    for trip_parts in all_trip_parts:
        if is_trip_valid(trip_parts) \
                and (not result or len(trip_parts) < len(result)):
            result = trip_parts

    return result

# Problem 4


def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """

    st = time.time()
    res = greedy_cow_transport(load_cows('ps1_cow_data.txt'))
    print(f'[GREEDY] needs to travel {len(res)} times:\n', res)
    print(time.time() - st)
    print()

    st = time.time()
    res = brute_force_cow_transport(load_cows('ps1_cow_data.txt'))
    print(f'[BRUTE FORCE] needs to travel {len(res)} times:\n', res)
    print(time.time() - st)


if __name__ == '__main__':
    compare_cow_transport_algorithms()
