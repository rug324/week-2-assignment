'''Representing graphs'''
node_dict={'a':0,'b':1,'c':2,'d':3,'e':4}
def part_1_graph():
    """
    Returns a directed graph represented as a list of sets.
    """
    graph = [
        {1, 4},
        {2},
        {3, 4},
        {1},
        set()
    ]
    return graph
def part_2_graph():
    """
    Returns a directed graph represented as a list of lists.
    """
    graph = [
        [0, 1, 4],
        [2],
        [0, 3, 4],
        [],
        [3]
    ]
    return graph
def part_3_graph():
    """
    Returns a weighted directed graph represented as a list of dicts.
    """
    graph = [
        {0: 8, 1: 1, 4: 4},
        {2: 3},
        {0: 2, 4: 4},
        {},
        {}
    ]
    return graph
def part_4_graph():
    """
    Returns a directed graph represented as a dict of sets.
    """
    graph = {
        0: {0, 1, 4},
        1: {2},
        2: {0},
        3: set(),
        4: set()
    }
    return graph
def part_5_graph():
    """
    Returns a weighted directed graph represented as a dict of dicts.
    """
    graph = {
        0: {1: 5},
        1: {4: 3},
        2: {},
        3: {},
        4: {0: 6, 1: 2}  # e -> a (6), b (2)
    }
    return graph
