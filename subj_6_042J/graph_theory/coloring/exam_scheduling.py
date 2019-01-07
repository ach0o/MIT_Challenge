"""
Exam Scheduling(Graph Coloring) Problem

written by @achooan
"""


class Node(object):
    """
    A base class for graph nodes
    """

    def __init__(self, name):
        """
        parameters:
            name(string) - a name of this node
        """
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Edge(object):
    """
    A base class for graph edges
    """

    def __init__(self, src, dst):
        """
        parameters:
            src(Node object) - source node
            dst(Node object) - destination node
        """
        self.src = src
        self.dst = dst

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dst

    def __eq__(self, other):
        return {self.src, self.dst} == {other.src, other.dst}

    def __str__(self):
        return '{}-{}'.format(self.src, self.dst)

    def __repr__(self):
        return '{}-{}'.format(self.src, self.dst)


class Graph(object):
    """
    A class that represents a graph and manages nodes and edges
    """

    def __init__(self):
        """
        attributes:
            self.nodes(set[`Node`]) - contains nodes that construct this graph.
            self.edges(list[`Edge`]) - contains edges that connect the nodes
                                       in this graph.
        """
        self.nodes = set()
        self.edges = list()

    def add_nodes(self, nodes):
        self.nodes.update(nodes)

    def add_edges(self, edges):
        for edge in edges:
            src, dst = edge.get_source(), edge.get_destination()

            if not(src in self.nodes and dst in self.nodes):
                raise ValueError('node is not in the graph')

            if edge not in self.edges:
                self.edges.append(edge)

    def get_degrees(self):
        degrees = dict()
        for edge in self.edges:
            src, dst = edge.get_source(), edge.get_destination()
            degrees[src] = degrees.get(src, 0) + 1
            degrees[dst] = degrees.get(dst, 0) + 1
        return degrees

    def get_adjacent_nodes(self, node, exclude_nodes=[]):
        adj_nodes = list()

        for edge in self.edges:
            edge_nodes = [edge.get_source(), edge.get_destination()]
            if node in edge_nodes.copy():
                edge_nodes.remove(node)
                adj_nodes.extend(edge_nodes)

        for node in adj_nodes.copy():
            if node in exclude_nodes:
                adj_nodes.remove(node)

        return adj_nodes

    def validate_node_colors(self):
        status = []
        for edge in self.edges:
            if not edge.src.time_slot or not edge.dst.time_slot:
                status.append(False)
            else:
                status.append(edge.src.time_slot != edge.dst.time_slot)
            # print(edge, status)
        return all(status)


class Exam(Node):
    """
    A child class of `Node` class
    """

    def __init__(self, name):
        """
        parameters:
            name(string) - a course name of this exam(node)

        attributes:
            self.name - a course name of this exam(node)
            self.time_slot - represents a scheduled time period(a color)
                             for this exam(node)
        """
        super().__init__(name)
        self.time_slot = None

    def set_time_slot(self, slot):
        self.time_slot = slot

    def get_time_slot(self):
        return self.time_slot

    def __eq__(self, other):
        return super().__eq__(other)

    def __hash__(self):
        return self.name.__hash__()

    def __str__(self):
        return '{}({})'.format(self.name, self.time_slot)

    def __repr__(self):
        return '{}({})'.format(self.name, self.time_slot)


class Student(object):
    def __init__(self, courses: list):
        self.courses = courses

    def get_courses(self):
        return self.courses.copy()


def get_permutations(sequence: list):
    if len(sequence) == 1:
        return list()
    else:
        result = []
        for node in sequence[1:]:
            result.append((sequence[0], node))
        result.extend(get_permutations(sequence[1:]))
        return result


def assign_time_slots(graph, node, previous_slot, slot_list):
    if not node:
        # Get a node with the highest degree
        degrees = graph.get_degrees()
        max_degree = max(degrees.values())
        max_degree_nodes = [node for node, degree in degrees.items()
                            if degree == max_degree]

        node = max_degree_nodes[0]

    available_slot = slot_list.copy()
    if previous_slot:
        # Exclude previous slot because adjacent nodes
        # must not have the same color
        available_slot.remove(previous_slot)

    for slot in available_slot:

        if graph.validate_node_colors():
            # Break if all adjacent nodes have a different color
            break

        node.set_time_slot(slot)
        adj_nodes = graph.get_adjacent_nodes(node)
        # If the node has the same slot
        if any([adj.time_slot == node.time_slot for adj in adj_nodes]):
            continue

        temp_colored_nodes = set([node])

        no_slot_nodes = [adj for adj in adj_nodes if not adj.time_slot]
        if not no_slot_nodes:
            # Return the current node when every adjacent nodes are colored
            return temp_colored_nodes

        # Iterate nodes w/o color that are adjacent to the 'node',
        # then, recall this function to assign a new color.
        # If the new color doesn't cause any conflict, then update the graph
        for idx, ns_node in enumerate(no_slot_nodes):
            assigned_node = assign_time_slots(graph, ns_node, slot, slot_list)

            # Check if newly assigned node has color conflicts
            # with the adjacent nodes
            conflict_status = []
            for asgn in assigned_node:
                adjs = graph.get_adjacent_nodes(asgn)
                conflict_status.append(all([asgn.time_slot != adnode.time_slot
                                            for adnode in adjs]))
            if all(conflict_status):
                temp_colored_nodes.update(assigned_node)

    return graph.nodes


def scheduling(students, verbose=False):
    graph = Graph()
    nodes = dict()
    edges = list()

    for std in students:
        courses = std.get_courses()
        for crs in courses:
            nodes[crs] = nodes.get(crs, Exam(crs))

        if len(courses) == 1:
            # A lonely node may have any color('*')
            nodes[courses[0]].time_slot = '*'
        else:
            temp = [nodes[crs] for crs in courses]
            possible_edges = [Edge(*perm) for perm in get_permutations(temp)]
            edges.extend(possible_edges)

    graph.add_nodes(list(nodes.values()))
    graph.add_edges(edges)

    if len(graph.nodes) == 1 or len(graph.edges) == 0:
        # Return all nodes if a graph has only one node
        # Or if a graph has no edges(it means a graph has all lonely nodes)
        return graph.nodes

    max_colorable = len(graph.nodes) + 1
    available_colors = list(range(1, max_colorable + 1))
    degrees = graph.get_degrees()

    result = assign_time_slots(graph, None, None, available_colors)

    if verbose:
        print('NODES: {}\nEDGES: {}'.format(graph.nodes, graph.edges))
        print('AVAILABLE COLORS(max): {}\nDEGREES: {}\nANSWER:{}'.format(
            available_colors, degrees, result))

    return result


if __name__ == '__main__':
    st1 = Student(['6.002', '6.170'])
    st2 = Student(['6.002', '6.003'])
    st3 = Student(['6.002', '6.042'])
    st4 = Student(['6.002', '6.041'])
    st5 = Student(['6.170', '6.041'])
    st6 = Student(['6.170', '6.003'])
    st7 = Student(['6.042', '6.003'])
    st8 = Student(['6.042', '6.041'])

    happy_case = [st1, st2, st3, st4, st5, st6, st7, st8]
    scheduling(happy_case, verbose=True)
