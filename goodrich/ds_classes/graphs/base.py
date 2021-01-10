from abc import ABC, abstractmethod


class Vertex:
    __slots__ = '_element'

    def __init__(self, x):
        self._element = x

    def element(self):
        return self._element

    def __hash__(self):
        return hash(id(self))


class Edge:
    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u, v, x):
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        return self._origin, self._destination

    def opposite(self, v):
        return self._destination if v is self._origin else self._origin

    def element(self):
        return self._element

    def __hash__(self):
        return hash((self._origin, self._destination))


class AbstractGraph(ABC):

    @abstractmethod
    def vertex_count(self):
        """Return the number of vertices of the graph."""

    @abstractmethod
    def vertices(self):
        """Return an iteration of all the vertices of the graph."""

    @abstractmethod
    def edge_count(self):
        """Return the number of the edges of the graph."""

    @abstractmethod
    def edges(self):
        """Return a iteration of all the edges of the graph."""

    @abstractmethod
    def get_edge(self, u, v):
        """Return the edge from vertex u to vertex v, if one exists; otherwise return None."""

    @abstractmethod
    def degree(self, v, out=True):
        """For an undirected graph, return the number of edges incident to vertex v.
        For a directed graph, return the number of outgoing or incoming edges to vertex v.
        """

    @abstractmethod
    def incident_edges(self, v, out=True):
        """Return an iteration of all the edges incident to vertex v.
        For a directed graph, report outgoing edges by default, report incoming edges if optional
        parameter is set to False.
        """

    @abstractmethod
    def insert_vertex(self, x=None):
        """Create and return a new vertex storing element x."""

    @abstractmethod
    def insert_edge(self, u, v, x=None):
        """Create and return a new edge from vertex u to vertex v, storing element x."""

    @abstractmethod
    def remove_vertex(self, v):
        """Remove vertex v and all its incident edges from the graph."""

    @abstractmethod
    def remove_edge(self, eg):
        """Remove edge eg from the graph."""
