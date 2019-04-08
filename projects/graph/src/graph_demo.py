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

    graph.bft(1)

    graph = Graph()  # Instantiate your graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    # graph.add_edge('0', '4')
    # print(f'second: {graph.vertices['0']}')
    graph.bft(0)

if __name__ == '__main__':
    # TODO - parse argv
    main()
