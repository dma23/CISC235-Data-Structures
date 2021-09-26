from a1_1 import graph
import random

def bfs(g, s=None): 
    # Breadth-first search algorithm
    # takes in a graph g, as a adjacency list and starting node, s (defaults to None)
    # creates the queue, visited status and total weight variables
    queue = []
    visited = []
    total = 0

    # if there is no specified start value, pick one of the vertices at random
    if s == None: 
        s = random.randint(0, len(g.keys())-1)

    # mark the starting node as visited
    visited.append(s) 
    queue.append(s)

    while queue:
        curr = queue.pop(0)
        #print(curr)
        
        for adj in g[curr]:
            #print(adj[0])
            # searches through nodes in queue, if node has not been searched yet, add it to queue and grab its weight
            if adj[0] not in visited:
                visited.append(adj[0])
                queue.append(adj[0])
                total += adj[1]
        
    return total, visited

if __name__ == '__main__':

    g1 = { # in adjacency list form 
        0: [[1, 15], [3, 7], [4, 10]],
        1: [[0, 15], [2, 9], [3, 11], [5, 9]], 
        2: [[1, 9], [4, 12], [5, 7]], 
        3: [[0, 7], [1, 11], [4, 8], [5, 14]], 
        4: [[0, 10], [2, 12], [3, 8], [5, 8]], 
        5: [[1, 9], [2, 7], [3, 14], [4, 8]]
    } 
    # tests all possible starting nodes
    for i in range(6):
        # prints total weight of branches travelled and order of traversal
        print(bfs(g1, i))
    
    # tests random s value
    print(bfs(g1))

    # testing coversion function from a1_1, ignore 
    g = graph(6)
    g.add_edge(0, 1, 15)
    g.add_edge(0, 3, 7)
    g.add_edge(0, 4, 10) 
    g.add_edge(1, 2, 9)
    g.add_edge(1, 3, 11) 
    g.add_edge(1, 5, 9)
    g.add_edge(2, 4, 12)
    g.add_edge(2, 5, 7)
    g.add_edge(3, 4, 8)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 8)
    # print(g.convert_to_adj_list())
