from collections import defaultdict
import heapq


def prim(g, s=0):
    # takes in graph g, and starting node s, (defaults to 0 node)
    # intialize our vertices storage, total count, and visited 
    vertices = []
    total = 0
    visited = [s]
    # sets the inital edge using the start node 
    edges = [
        (weight, s, nxt)
        for nxt, weight in g[s]
    ]
    (heapSort(edges))
    #print(edges)
    while edges:
        weight, begin, nxt = edges.pop(0)
        #print(edges)
        if nxt not in visited:
            #print(to)
            total += weight
            visited.append(nxt)
            vertices.append(nxt)
            for nxt_node, weight in g[nxt]:
                #print(graph[to].items())
                if nxt_node not in visited:
                    #print(edges, 'first')
                    heapq.heappush(edges, (weight, nxt, nxt_node))
                    #print(edges, 'second')
    
    return vertices, total

# heapSort algorithm is taken from lecture notes/g4g heapsort page
# eventually decided to use heapq but w/e 
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

if __name__ == '__main__':

    g1 = { # in adjacency list form 
        0: [[1, 15], [3, 7], [4, 10]],
        1: [[0, 15], [2, 9], [3, 11], [5, 9]], 
        2: [[1, 9], [4, 12], [5, 7]], 
        3: [[0, 7], [1, 11], [4, 8], [5, 14]], 
        4: [[0, 10], [2, 12], [3, 8], [5, 8]], 
        5: [[1, 9], [2, 7], [3, 14], [4, 8]]
    } 
    a,b = prim(g1, 1)
    print('Order of vertices: {}, total weight of MST: {}'.format(a, b))
