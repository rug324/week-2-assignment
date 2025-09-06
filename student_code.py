'''Representing graphs'''
node_dict={'a':0,'b':1,'c':2,'d':3,'e':4}
def part_1_graph():
    """
    Returns a directed graph represented as a list of sets.
    """
    graph = [
        {'b', 'e'},
        {'c'},
        {'d', 'e'},
        {'b'},
        set()
    ]
    return graph
def part_2_graph():
    """
    Returns a directed graph represented as a list of lists.
    """
    graph = [
        ['a', 'b', 'e'],
        ['c'],
        ['a', 'd', 'e'],
        [],
        ['d']
    ]
    return graph
def part_3_graph():
    """
    Returns a weighted directed graph represented as a list of dicts.
    """
    graph = [
        {'a': 8, 'b': 1, 'e': 4},
        {'c': 3},
        {'a': 2, 'e': 4},
        {},
        {}
    ]
    return graph
def part_4_graph():
    """
    Returns a directed graph represented as a dict of sets.
    """
    graph = {
        'a': {'a', 'b', 'e'},
        'b': {'c'},
        'c': {'a'},
        'd': set(),
        'e': set()
    }
    return graph
def part_5_graph():
    """
    Returns a weighted directed graph represented as a dict of dicts.
    """
    graph = {
        'a': {'b': 5},
        'b': {'e': 3},
        'c': {},
        'd': {},
        'e': {'a': 6, 'b': 2}
    }
    return graph
