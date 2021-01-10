from base import AbstractGraph, Vertex, Edge


class AMGraph(AbstractGraph):

    def __init__(self, n):
        self._size = n
        self._vertices: list = [None] * n
        self._edges: list = []
        self._matrix: list = [[None for _ in range(n)] for _ in range(n)]

    def vertex_count(self):
        return len(self._vertices)

    def vertices(self):
        return self._vertices

    def edge_count(self):
        return len(self._edges)

    def edges(self):
        return self._edges

    def get_edge(self, u, v):
        u_idx = self._vertices.index(u)
        v_idx = self._vertices.index(v)
        return self._matrix[u_idx][v_idx]

    def degree(self, v, out=True):
        v_idx = self._vertices.index(v)
        return sum(1 if x is not None else 0 for x in self._matrix[v_idx])

    def incident_edges(self, v, out=True):
        v_idx = self._vertices.index(v)
        return set(x for x in self._matrix[v_idx])

    def insert_vertex(self, x=None):
        _idx = self._vertices.index(None)
        v = Vertex(x=x)
        if _idx > -1:
            self._vertices[_idx] = v
        else:
            raise Exception("space is used.")

    def insert_edge(self, u, v, x=None):
        eg = Edge(u, v, x=x)
        u_idx = self._vertices.index(u)
        v_idx = self._vertices.index(v)
        self._matrix[u_idx][v_idx] = eg

    def remove_vertex(self, v):
        v_idx = self._vertices.index(v)
        self._vertices[v_idx] = None
        for x in range(self._size):
            eg = self._matrix[v_idx][x]
            # eg1 = self._matrix[x][v_idx]
            self._matrix[v_idx][x] = None
            self._matrix[x][v_idx] = None
            self._edges.remove(eg)
            # self._edges.remove(eg1)

    def remove_edge(self, eg):
        u, v = eg.endpoints()
        u_idx = self._vertices.index(u)
        v_idx = self._vertices.index(v)
        self._matrix[u_idx][v_idx] = None
        self._matrix[v_idx][u_idx] = None
        self._edges.remove(eg)

