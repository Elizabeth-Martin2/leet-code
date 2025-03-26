class Solution:
    """Return how many undirected graphs can be created when given a number of vertices"""
    def count(self, n):
        exp = n * (n - 1) / 2
        return int(pow(2, exp))

    """Return the adjacency list of a graph given edges & number of vertices"""
    def printGraph(self, V : int, edges : list[list[int]]) -> list[list[int]]:
        adj = [[] for _ in range(V)]

        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)

        return adj

