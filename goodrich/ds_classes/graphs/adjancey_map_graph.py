from base import AbstractGraph, Vertex, Edge


class AMGraph(AbstractGraph):

    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._outgoing is not self._incoming

    def vertex_count(self):
        return len(self._outgoing.keys())

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum([len(val) for val in self._outgoing.values()])
        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()
        for val in self._outgoing.values():
            result.update(val)
        return list(result)

    def get_edge(self, u, v):
        return self._outgoing[u].get(v)

    def degree(self, v, out=True):
        adj = self._outgoing if out else self._incoming
        return len(adj[v])

    def incident_edges(self, v, out=True):
        adj = self._outgoing if out else self._incoming
        return adj[v].values()

    def insert_vertex(self, x=None):
        v = Vertex(x=x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        eg = Edge(u, v, x=x)
        self._outgoing[u][v] = eg
        self._incoming[v][u] = eg

    def remove_vertex(self, v):
        del self._outgoing[v]
        for val in self._outgoing.values():
            val.pop(v, None)

    def remove_edge(self, eg: Edge):
        u, v = eg.endpoints()
        del self._outgoing[u][v]
        del self._incoming[v][u]
