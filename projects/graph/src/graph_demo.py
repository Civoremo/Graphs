#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv

from graph import Graph


def main():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_vertex('5')
    graph.add_vertex('6')
    graph.add_vertex('7')
    graph.add_directed_edge('5', '3')
    graph.add_directed_edge('6', '3')
    graph.add_directed_edge('7', '1')
    graph.add_directed_edge('4', '7')
    graph.add_directed_edge('1', '2')
    graph.add_directed_edge('7', '6')
    graph.add_directed_edge('2', '4')
    graph.add_directed_edge('3', '5')
    graph.add_directed_edge('2', '3')
    graph.add_directed_edge('4', '6')
    print(f'first: {graph.vertices}')

    print(f'\n----- Breadth-First Traversal')
    graph.bft('1')
    print(f'\n----- Depth-First Traversal')
    graph.dft('1')
    print(f'\n----- Depth-First Traversal Recursion')
    graph.dft_recursion('1')
    print(f'\n----- Breadth-First Search')
    graph.bfs('1', '5')
    print(f'\n----- Depth-First Search')
    graph.dfs('1', '6')

    # graph1 = Graph()  # Instantiate your graph
    # graph1.add_vertex('0')
    # graph1.add_vertex('1')
    # graph1.add_vertex('2')
    # graph1.add_vertex('3')
    # graph1.add_edge('0', '1')
    # graph1.add_edge('0', '3')
    # # graph.add_edge('0', '4')
    # # print(f'second: {graph.vertices}')
    # graph1.bft('0')
    # graph1.dft('0')
    # graph1.bfs('0', '3')

if __name__ == '__main__':
    # TODO - parse argv
    main()
