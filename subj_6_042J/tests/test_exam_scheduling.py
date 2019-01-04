from .context import graph_theory
from graph_theory.coloring import exam_scheduling as es


st1 = es.Student(['6.001'])
st2 = es.Student(['6.002'])
st3 = es.Student(['6.001', '6.002'])
st4 = es.Student(['6.002', '6.003'])
st5 = es.Student(['6.003', '6.004'])
st6 = es.Student(['6.004', '6.005'])
st7 = es.Student(['6.005', '6.001'])
st8 = es.Student(['6.001', '6.003'])
st9 = es.Student(['6.001', '6.004'])
st10 = es.Student(['6.002', '6.004'])
st11 = es.Student(['6.002', '6.005'])
st12 = es.Student(['6.003', '6.005'])


def node_with_color(course, color):
    exam = es.Exam(course)
    exam.time_slot = color
    return exam


def test_coloring_one_node_empty_graph():
    students = [st1]
    result = [node_with_color(students[0].courses[0], '*')]

    assert es.scheduling(students) == set(result)


def test_coloring_two_nodes_empty_graph():
    students = [st1, st2]
    result = list()
    for std in students:
        result.extend([node_with_color(crs, '*') for crs in std.get_courses()])

    assert es.scheduling(students) == set(result)


def test_coloring_two_nodes_line_graph():
    students = [st3]
    result = list()
    result.append(node_with_color(students[0].courses[0], '1'))
    result.append(node_with_color(students[0].courses[1], '2'))

    assert es.scheduling(students) == set(result)


def test_coloring_five_nodes_cycle_graph():
    students = [st3, st4, st5, st6, st7]
    result = list()
    result.append(node_with_color(students[0].courses[0], '1'))
    result.append(node_with_color(students[0].courses[1], '2'))
    result.append(node_with_color(students[1].courses[0], '2'))
    result.append(node_with_color(students[1].courses[1], '1'))
    result.append(node_with_color(students[2].courses[0], '1'))
    result.append(node_with_color(students[2].courses[1], '2'))
    result.append(node_with_color(students[3].courses[0], '2'))
    result.append(node_with_color(students[3].courses[1], '3'))
    result.append(node_with_color(students[4].courses[0], '3'))
    result.append(node_with_color(students[4].courses[1], '1'))

    assert es.scheduling(students) == set(result)


def test_coloring_five_nodes_complete_graph():
    students = [st3, st4, st5, st6, st7, st8, st9, st10, st11, st12]
    courses = set()
    for std in students:
        courses.update(std.get_courses())
    result_nodes = es.scheduling(students)
    colors = [node.time_slot for node in result_nodes]

    # all colors has to be different
    assert len(colors) == len(set(colors))
