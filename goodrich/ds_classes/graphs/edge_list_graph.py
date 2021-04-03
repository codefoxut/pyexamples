from base import AbstractGraph, Edge, Vertex


class ELGraph(AbstractGraph):
    def __init__(self):
        self._edges = []
        self._vertices = []

    def vertex_count(self):
        return len(self._vertices)

    def vertices(self):
        return self._vertices

    def edge_count(self):
        return len(self._edges)

    def edges(self):
        return self._edges

    def get_edge(self, u, v):
        for eg in self._edges:
            _u, _v = eg.endpoints()
            if u == _u and v == _v:
                return eg
        return None

    def degree(self, v, out=True):
        count = 0
        for eg in self._edges:
            _u, _v = eg.endpoints()
            if v == _u or v == _v:
                count += 1
        return count // 2

    def incident_edges(self, v, out=True):
        result = set()
        for eg in self._edges:
            _u, _v = eg.endpoints()
            if v == _u or v == _v:
                result.add(eg)
        return list(result)

    def insert_vertex(self, x=None):
        v = Vertex(x=x)
        self._vertices.append(v)
        return v

    def insert_edge(self, u, v, x=None):
        eg = Edge(u, v, x=x)
        self._edges.append(eg)
        return eg

    def remove_vertex(self, v):
        self._vertices.remove(v)
        for eg in self._edges:
            _u, _v = eg.endpoints()
            if _u == v or _v == v:
                self._edges.remove(eg)

    def remove_edge(self, eg):
        self._edges.remove(eg)


if __name__ == '__main__':
    g = ELGraph()
    v_list = ['u', 'v', 'w', 'z']
    edges_list = [('u', 'v', 'e'), ('u', 'w', 'g'), ('v', 'w', 'f'), ('w', 'z', 'h')]

    vertices_dict = {}
    for t in v_list:
        v_obj = g.insert_vertex(x=t)
        vertices_dict[t] = v_obj

    for ed in edges_list:
        edge = g.insert_edge(vertices_dict[ed[0]], vertices_dict[ed[1]], ed[2])

    print(g.degree(vertices_dict['v']))
    print(g.incident_edges(vertices_dict['v']))
    print(g.get_edge(vertices_dict['w'], vertices_dict['z']))
