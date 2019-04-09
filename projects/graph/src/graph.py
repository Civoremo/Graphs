"""
Simple graph implementation
"""
from queue import Queue


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # pass  # TODO
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError('The vertex does not exist. (add_edge)')

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('The vertex does not exist. (add_directed_edge)')

    def bft(self, start_vertex):
        q = Queue()
        q.enqueue(start_vertex)
        visited = set()

        while q.len() > 0:
            v = q.dequeue()
            if v not in visited:
                # print(f'Visited: {visited}')
                print(f'BFT: {v}')
                visited.add(v)
                print(f'BFT Visited: {visited}')
                for next_vertex in self.vertices[v]:
                    q.enqueue(next_vertex)

    def dft(self, start_vertex):
        s = []
        s.append(start_vertex)
        visited = set()

        while len(s) > 0:
            v = s.pop()
            if v not in visited:
                print(f'DFT: {v}')  
                visited.add(v)
                print(f'DFT Visited: {visited}')
                for next_vert in self.vertices[v]:
                    s.append(next_vert)

    def bfs(self, start_vertex, target_vertex):
        q = Queue()
        visited = set()
        path = []
        path.append(start_vertex)
        q.enqueue(path)

        
        while q.len() > 0:
            v = q.dequeue()
            if v[-1] not in visited:
                visited.add(v[-1])
                if v[-1] == target_vertex:
                    print(f'Take Path: {v}')
                    return v
                for next_vertex in self.vertices[v[-1]]:
                    copy = v.copy()
                    copy.append(next_vertex)
                    q.enqueue(copy)