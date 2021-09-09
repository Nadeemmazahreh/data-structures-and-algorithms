import pytest

class Vertix:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'Vertix > {self.value}'

class Edge:
    def __init__(self, vertix , weight):
        self.vertix = vertix
        self.weight = weight

class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        v = Vertix(value)
        self.adjacency_list[v] = []
        return v

    def add_edge(self, start_node, end_node, weight=0):
        all_nodes=self.adjacency_list.keys()
        if not start_node in all_nodes and not end_node in all_nodes:
            return 'Both nodes are not in the Graph'
        elif not start_node in all_nodes:
            return 'The first node is not in the Graph'
        elif not end_node in all_nodes:
            return 'The seconde node is not in the Graph'

        edge = Edge(end_node, weight)
        self.adjacency_list[start_node].append(edge)

    def get_nodes(self):
        arr=[]
        for vertix in self.adjacency_list.keys():
            arr.append(vertix)
        if len(arr)==0:
            return None
        return arr

    def get_neighbors(self, node):
        arr=[]

        if node in self.adjacency_list :

            for edge in self.adjacency_list[node]:

               arr.append((edge.vertix, edge.weight))

            return arr
        if len(arr)==0:
            return None


    def size(self):
        return len(self.adjacency_list.keys())

    def __str__(self):
        output = ''
        for vertix in self.adjacency_list.keys():

            output += vertix.value

            for edge in self.adjacency_list[vertix]:
                output += ' -> ' + edge.vertix.value

            output += '\n'
        return output

def test_can_add():
    graph = Graph()
    actual = graph.add_node('a')
    expected=graph.get_nodes()[0]
    assert actual==expected

def test_can_addedge():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    graph.add_edge(a, b)
    actual=graph.get_neighbors(a)[0][0]
    expected=b
    assert actual==expected

def test_get_nodes():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    actual=graph.get_nodes()
    expected=[a,b,c,d,e,f]
    assert actual==expected

def test_get_neighbors_node():
    graph = Graph()
    a = graph.add_node('a')
    c = graph.add_node('c')
    graph.add_edge(a, c)
    actual=graph.get_neighbors(a)[0][0]
    expected=c
    assert actual==expected

def test_get_neighbors_weight():
    graph = Graph()
    a = graph.add_node('a')
    c = graph.add_node('c')
    graph.add_edge(a, c)
    actual=graph.get_neighbors(a)[0][1]
    expected=0
    assert actual==expected


def test_size():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    actual=graph.size()
    expected=6
    assert actual==expected

def test_only_one_node():
    graph = Graph()
    a = graph.add_node('a')
    actual=graph.get_neighbors(a)
    expected=[]
    assert actual==expected


def test_empty_graph():
    graph = Graph()
    actual=graph.get_nodes()
    expected=None
    assert actual==expected


