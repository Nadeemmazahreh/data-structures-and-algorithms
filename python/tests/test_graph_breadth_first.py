from collections import deque


class Queue():
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)



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

    def BreadthFirst(self,node):
        if node not in self.adjacency_list:
            return 'This node is not in the graph'
        nodes=[]
        breadth = Queue()
        visited = set()

        breadth.enqueue(node)
        visited.add(node)

        while breadth:
            front=breadth.dequeue()
            nodes.append(front)
            for edge in self.adjacency_list[front]:

                if edge.vertix not in visited:

                    visited.add(edge.vertix)
                    breadth.enqueue(edge.vertix)

        return nodes


    def __str__(self):
        output = ''
        for vertix in self.adjacency_list.keys():

            output += vertix.value

            for edge in self.adjacency_list[vertix]:
                output += ' -> ' + edge.vertix.value

            output += '\n'
        return output

def test_happy_path():
    graph2 = Graph()
    pandora= graph2.add_node('pandora')
    arendelle= graph2.add_node('arendelle')
    metroville= graph2.add_node('metroville')
    narina= graph2.add_node('narina')
    naboo= graph2.add_node('naboo')
    manstropolis= graph2.add_node('manstropolis')
    graph2.add_edge(pandora,arendelle)
    graph2.add_edge(arendelle,pandora)
    graph2.add_edge(arendelle,metroville)
    graph2.add_edge(arendelle,metroville)
    graph2.add_edge(metroville,arendelle)
    graph2.add_edge(metroville,manstropolis)
    graph2.add_edge(metroville,naboo)
    graph2.add_edge(metroville,narina)
    graph2.add_edge(narina,metroville)
    graph2.add_edge(narina,naboo)
    graph2.add_edge(naboo,narina)
    graph2.add_edge(naboo,metroville)
    graph2.add_edge(naboo,manstropolis)
    graph2.add_edge(manstropolis,naboo)
    graph2.add_edge(manstropolis,arendelle)
    graph2.add_edge(manstropolis,metroville)

    actual=graph2.BreadthFirst(pandora)
    expected=[pandora,arendelle,metroville,manstropolis,naboo,narina]
    assert actual==expected



def test_edge_case():
    graph2 = Graph()
    pandora=Vertix('pandora')

    actual=graph2.BreadthFirst(pandora)
    expected='This node is not in the graph'
    assert actual==expected


def test_expected_failure():
    graph2 = Graph()
    pandora= graph2.add_node('pandora')
    arendelle= graph2.add_node('arendelle')
    metroville= graph2.add_node('metroville')
    narina= graph2.add_node('narina')
    naboo= graph2.add_node('naboo')
    manstropolis= graph2.add_node('manstropolis')
    graph2.add_edge(pandora,arendelle)
    graph2.add_edge(arendelle,pandora)
    graph2.add_edge(arendelle,metroville)
    graph2.add_edge(arendelle,metroville)
    graph2.add_edge(metroville,arendelle)
    graph2.add_edge(metroville,manstropolis)
    graph2.add_edge(metroville,naboo)
    graph2.add_edge(metroville,narina)
    graph2.add_edge(narina,metroville)
    graph2.add_edge(narina,naboo)
    graph2.add_edge(naboo,narina)
    graph2.add_edge(naboo,metroville)
    graph2.add_edge(naboo,manstropolis)
    graph2.add_edge(manstropolis,naboo)
    graph2.add_edge(manstropolis,arendelle)
    graph2.add_edge(manstropolis,metroville)

    actual=graph2.BreadthFirst(pandora)
    expected=[pandora,arendelle,metroville,manstropolis,narina,naboo]
    assert actual!=expected
