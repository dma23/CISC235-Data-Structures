import random

class graph:

    def __init__(self, v=0, e=False):
        self.vertices = {}
        self.edges = {}
        # adds number of vertices to graph, defaults to 0 (empty graph) 
        for i in range(v):
            self.vertices[i] = i
        # adds random number of edges, defaults to False (empty graph) and adds random weights to them
        if e != False:
            for i in range(2, v):
                x = random.randint(1, v-1)
                S = random.sample(list(self.vertices), v-1)
                for s in S:
                    weights = random.randint(10, 100)
                    self.add_edge(i, s, weights)

    def add_vertex(self, v):
        # adds a vertex to the graph under key, v
        self.vertices[v] = v

    def add_edge(self, v1, v2, w):
        # creates an edge between v1 and v2 with weight, w 
        if v1 not in self.vertices or v2 not in self.vertices or (v1 == v2):
            # makes sure both vertices are in the graph and are not attempting to connect to itself
            # print("Unable to create edge between {0} and {1}".format(v1, v2))
            return None
        else:
            # removes/overwrites any previous edge values 
            if (v2, v1) in self.edges:
                del self.edges[v2, v1]
                self.edges[v1, v2] = w
            else: 
                self.edges[v1, v2] = w

    def get_vertices(self):
        # returns a list of vertices in the graph
        return self.vertices.keys()

    def get_edges(self):
        # returns a list of edges in the graph along with weights
        return self.edges.items()

    def get_weights(self):
        # returns only the weights in the graph
        return self.edges.values()

    def convert_to_adj_list(self):
        # not necessary but quality of life feature
        adj_list = {}
        # get every vertex in the graph
        for keys in self.vertices.keys():
            # for every edge, get the pair if the key appears in it 
            temp = [x for x in self.get_edges() if keys in x[0]]
            c = []
            # take the value that is not the key 
            for i in temp:
                if i[0][0] == keys: 
                    a = i[0][1]
                else:
                    a = i[0][0]
                # the weight
                b = i[1]
                # add to temp list of values (v2, weight)
                c.append((a,b))
            # connect full list of (v2, weight) to key in adj list
            adj_list[keys] = c
        return adj_list

if __name__ == '__main__':
    # initalize graph
    g = graph(5, True)
    # test adding a vertex 'a'
    #g.add_vertex('a')
    # test get_vertices 
    print(g.get_vertices())
    # adding more vertices
    #g.add_vertex('b')   
    #g.add_vertex('c')
    #g.add_edge(0, 1, 5)
    #g.add_edge(0, 1, 10)
    #g.add_edge('c', 'b', 6)
    # test get_edges
    print(g.get_edges())
    # test get_weights
    print(g.get_weights())

    print(g.convert_to_adj_list())
