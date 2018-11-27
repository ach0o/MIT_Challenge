"""
6.0001 Introduction to Computer Science and Programming in Python

Assignment
(https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/)

Problem Set 0

Solved by achooan
"""
import numpy


def get_number_input(prompt_msg='Enter number: '):
    try:
        value = int(input(prompt_msg))
    except ValueError:
        print('input value must be an integer')
        return get_number_input(prompt_msg)

    return value


def get_power(num_x, num_y):
    return num_x ** num_y


def get_log2(num):
    return numpy.log2(num)


if __name__ == '__main__':
    num_x = get_number_input(prompt_msg='Enter number x: ')
    num_y = get_number_input(prompt_msg='Enter number y: ')

    print(f'x**y = {get_power(num_x,num_y)}')
    print(f'log(x) = {get_log2(num_x)}')
