def dfs(graph, visited, vertex, result_dict, count):
    """
    Depth first search implementation
    :param graph: input graph G = {V, E}
    :param visited: set of visited node
    :param vertex: current vertex
    :param result_dict: dictionary mark each vertex with order they are visisted
    :param count: count visited order of vertex
    :return:
    """
    if vertex not in visited:
        visited.add(vertex)
        count += 1
        result_dict[vertex] = count
        for adjacent in graph[vertex]:
            dfs(graph, visited, adjacent, result_dict, count)


if __name__ == "__main__":
    g = {
        "a": ["c", "d", "e"],
        "b": ["e", "f"],
        "c": ["a", "d", "f"],
        "d": ["a", "c"],
        "e": ["a", "b", "f"],
        "f": ["b", "c", "e"],
        "g": ["h", "j"],
        "h": ["g", "i"],
        "i": ["h", "j"],
        "j": ["g", "i"]
    }
    visit = set()
    c = 0
    f = {key: 0 for key in g.keys()}
    for key in g.keys():
        dfs(g, visit, key, f, c)
    print(f)
