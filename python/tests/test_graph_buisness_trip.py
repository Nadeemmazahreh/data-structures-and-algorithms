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

def business_trip(graph,cities):
    can = True
    cost = 0
    for i in range(len(cities)-1):
        for city in graph.get_neighbors(cities[i]):
            if cities[i+1]==city[0]:
                cost+=city[1]
                break
            else:
                can=False

    if can==False:
            cost=0

    return can, f'${cost}'

def test_happy_path():
    graph2 = Graph()

    pandora= graph2.add_node('pandora')
    arendelle= graph2.add_node('arendelle')
    metroville= graph2.add_node('metroville')
    narina= graph2.add_node('narina')
    naboo= graph2.add_node('naboo')
    manstropolis= graph2.add_node('manstropolis')

    graph2.add_edge(pandora,arendelle,150)
    graph2.add_edge(pandora,metroville,82)
    graph2.add_edge(arendelle,pandora,150)
    graph2.add_edge(arendelle,metroville,99)
    graph2.add_edge(arendelle,manstropolis,42)
    graph2.add_edge(metroville,pandora,82)
    graph2.add_edge(metroville,arendelle,99)
    graph2.add_edge(metroville,manstropolis,105)
    graph2.add_edge(metroville,naboo,26)
    graph2.add_edge(metroville,narina,37)
    graph2.add_edge(narina,metroville,37)
    graph2.add_edge(narina,naboo,250)
    graph2.add_edge(naboo,narina,250)
    graph2.add_edge(naboo,metroville,26)
    graph2.add_edge(naboo,manstropolis,73)
    graph2.add_edge(manstropolis,naboo,73)
    graph2.add_edge(manstropolis,arendelle,42)
    graph2.add_edge(manstropolis,metroville,105)

    actual=business_trip(graph2,[metroville,pandora])
    expected=(True, '$82')
    assert actual==expected



def test_edge_case():
    graph2 = Graph()

    pandora= graph2.add_node('pandora')
    arendelle= graph2.add_node('arendelle')
    metroville= graph2.add_node('metroville')
    narina= graph2.add_node('narina')
    naboo= graph2.add_node('naboo')
    manstropolis= graph2.add_node('manstropolis')

    graph2.add_edge(pandora,arendelle,150)
    graph2.add_edge(pandora,metroville,82)
    graph2.add_edge(arendelle,pandora,150)
    graph2.add_edge(arendelle,metroville,99)
    graph2.add_edge(arendelle,manstropolis,42)
    graph2.add_edge(metroville,pandora,82)
    graph2.add_edge(metroville,arendelle,99)
    graph2.add_edge(metroville,manstropolis,105)
    graph2.add_edge(metroville,naboo,26)
    graph2.add_edge(metroville,narina,37)
    graph2.add_edge(narina,metroville,37)
    graph2.add_edge(narina,naboo,250)
    graph2.add_edge(naboo,narina,250)
    graph2.add_edge(naboo,metroville,26)
    graph2.add_edge(naboo,manstropolis,73)
    graph2.add_edge(manstropolis,naboo,73)
    graph2.add_edge(manstropolis,arendelle,42)
    graph2.add_edge(manstropolis,metroville,105)

    actual=business_trip(graph2,[arendelle,manstropolis, naboo])
    expected=(False, '$0')
    assert actual==expected


def test_expected_failure():
    graph2 = Graph()

    pandora= graph2.add_node('pandora')
    arendelle= graph2.add_node('arendelle')
    metroville= graph2.add_node('metroville')
    narina= graph2.add_node('narina')
    naboo= graph2.add_node('naboo')
    manstropolis= graph2.add_node('manstropolis')

    graph2.add_edge(pandora,arendelle,150)
    graph2.add_edge(pandora,metroville,82)
    graph2.add_edge(arendelle,pandora,150)
    graph2.add_edge(arendelle,metroville,99)
    graph2.add_edge(arendelle,manstropolis,42)
    graph2.add_edge(metroville,pandora,82)
    graph2.add_edge(metroville,arendelle,99)
    graph2.add_edge(metroville,manstropolis,105)
    graph2.add_edge(metroville,naboo,26)
    graph2.add_edge(metroville,narina,37)
    graph2.add_edge(narina,metroville,37)
    graph2.add_edge(narina,naboo,250)
    graph2.add_edge(naboo,narina,250)
    graph2.add_edge(naboo,metroville,26)
    graph2.add_edge(naboo,manstropolis,73)
    graph2.add_edge(manstropolis,naboo,73)
    graph2.add_edge(manstropolis,arendelle,42)
    graph2.add_edge(manstropolis,metroville,105)

    actual=business_trip(graph2,[arendelle,manstropolis, naboo])
    expected=(True, '$82')
    assert actual!=expected
