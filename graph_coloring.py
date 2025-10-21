import pytest

class Node:
    def __init__(self, label):
        self.label = label
        self.neighbors = []
        self.color = None

    def connect(self, other):
        if other not in self.neighbors:
            self.neighbors.append(other)
        if self not in other.neighbors:
            other.neighbors.append(self)


def _build_triangle():
    a = Node('A')
    b = Node('B')
    c = Node('C')
    a.connect(b)
    b.connect(c)
    c.connect(a)
    return [a, b, c]


def _build_pair():
    a = Node('A')
    b = Node('B')
    a.connect(b)
    return [a, b]


@pytest.fixture(params=[
    (_build_triangle, ['red', 'blue', 'green'], {'A': 'red', 'B': 'blue', 'C': 'green'}),
    (_build_pair, ['red', 'blue'], {'A': 'red', 'B': 'blue'}),
])
def case(request):
    builder, colors, expected = request.param
    graph = builder()
    return graph, colors, expected


def test_color_graph(case):
    graph, colors, expected = case
    sol = Solution()
    sol.color_graph(graph, colors)
    result = {node.label: node.color for node in graph}
    assert result == expected


def main():
    graph = _build_triangle()
    colors = ['red', 'blue', 'green']
    try:
        Solution().color_graph(graph, colors)
        print({n.label: n.color for n in graph})
    except NotImplementedError:
        print('color_graph is not implemented')


class Solution:
    def color_graph(self, graph, colors):
    
        for node in graph:
            if node in node.neighbors:
                raise Exception('Legal coloring impossible for node with loop: %s' % node.label)
            illegal_colors = set(neighbor.color for neighbor in node.neighbors if neighbor.color)
    
            for color in colors:
                if color not in illegal_colors:
                    node.color = color
                    break



if __name__ == '__main__':
    main()

