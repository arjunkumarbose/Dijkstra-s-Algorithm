# Dijkstra's Algorithm in Python

This repository contains an implementation of Dijkstra's Algorithm in Python for finding the shortest paths in a weighted graph.

## Overview

Dijkstra's Algorithm is a famous algorithm used to find the shortest path from a single source vertex to all other vertices in a weighted graph. This implementation allows the user to input the graph edges along with their weights and then find the shortest distances from a specified source vertex.

## How to Use

1. **Inputting the Graph:**
   - Run the Python script `dijkstra.py`.
   - Enter edges for the graph with weights in the format: `'source destination weight'`. Use '#' to stop adding edges.

2. **Finding Shortest Paths:**
   - After entering the graph edges, the program will prompt you to enter the source vertex.
   - Input the source vertex from which you want to find the shortest paths.

3. **Viewing Results:**
   - The program will display the shortest distances from the specified source vertex to all other vertices in the graph.

## Example Usage

```bash
$ python dijkstra.py
Enter edges for the graph with weights (format: 'source destination weight'). Enter '#' to stop:
1 2 4
1 3 1
2 3 2
3 4 5
# (Enter '#' to stop)
Enter the source vertex to find shortest paths from: 1

Shortest distances from vertex 1:
Vertex 1: Distance from source = 0
Vertex 2: Distance from source = 4
Vertex 3: Distance from source = 1
Vertex 4: Distance from source = 6
