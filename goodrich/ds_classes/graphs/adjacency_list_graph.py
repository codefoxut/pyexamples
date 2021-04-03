from base import AbstractGraph, Edge, Vertex


class ALGraph(AbstractGraph):

    def __init__(self):
        self._vertices = []
        self._edges = {}

    def vertex_count(self):
        return len(self._vertices)

    def vertices(self):
        return self._vertices

    def edge_count(self):
        total = sum(len(val) for val in self._edges.values())
        return total // 2

    def edges(self):
        result = set()
        for val in self._edges.values():
            result.update(val)
        return result

    def get_edge(self, u, v):
        lst = self._edges[u]
        for eg in lst:
            _u, _v = eg.endpoints()
            if _v == v:
                return eg
        return None

    def degree(self, v, out=True):
        return len(self._edges[v])

    def incident_edges(self, v, out=True):
        return self._edges[v]

    def insert_vertex(self, x=None):
        v = Vertex(x=x)
        self._vertices.append(v)
        self._edges[v] = []
        return v

    def insert_edge(self, u, v, x=None):
        eg = Edge(u, v, x=x)
        self._edges[v].append(eg)
        self._edges[u].append(eg)
        return eg

    def remove_vertex(self, v):
        self._vertices.remove(v)
        self._edges.pop(v, None)
        for val in self._edges.values():
            for eg in val:
                _u, _v = eg.endpoints()
                if _v == v:
                    val.remove(eg)

    def remove_edge(self, eg):
        for val in self._edges.values():
            val.remove(eg)


if __name__ == '__main__':
    g = ALGraph()
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
