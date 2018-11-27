"""
6.0001 Introduction to Computer Science and Programming in Python

Assignment
(https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/)

Problem Set 4A

Solved by achooan
"""


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]
    else:
        result = []
        for index, char in enumerate(sequence):
            permutations = get_permutations(
                sequence[:index] + sequence[index + 1:])
            for p in permutations:
                result.append(char + p)

        return result


if __name__ == '__main__':
    # EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'ab'
    print('Input:', example_input)
    print('Expected Output:', ['ab', 'ba'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'abcd'
    print('Input:', example_input)
    print('Expected Output:',
          ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda',
           'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb',
           'dbac', 'dbca', 'dcab', 'dcba'])
    print('Actual Output:', get_permutations(example_input))
