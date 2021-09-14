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

    def depth_first(self,start_node):
        if start_node not in self.adjacency_list.keys():
            return 'The node is not in the graph'
        output=[]

        def recursive(node):
            print(node.value)
            if not node in output:
                output.append(node)
            for node2 in self.get_neighbors(node):
                if not node2[0] in output:
                    recursive(node2[0])

        recursive(start_node)

        return output
