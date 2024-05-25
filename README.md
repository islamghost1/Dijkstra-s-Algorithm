# Dijkstra's Algorithm and Graph Plotting

This repository contains a Python script that implements Dijkstra's algorithm to find the shortest path between nodes in a graph and visualizes the graph and the shortest path using `networkx` and `matplotlib`.

## Requirements

- Python 3.x
- `networkx` library
- `matplotlib` library

You can install the required libraries using pip:

```bash
pip install networkx matplotlib
```

## Script Description

The script consists of two main functions:

1. `dijkstra(graph, start, end)`: This function implements Dijkstra's algorithm to find the shortest path between `start` and `end` nodes in a given graph.
2. `plot_graph(graph, path)`: This function visualizes the graph and highlights the shortest path.

### Functions

#### `dijkstra(graph, start, end)`

- **Parameters**:
  - `graph`: A dictionary representing the graph as an adjacency list.
  - `start`: The starting node for the shortest path search.
  - `end`: The destination node for the shortest path search.

- **Returns**:
  - `distances[end]`: The shortest distance from `start` to `end`.
  - `path`: A list of nodes representing the shortest path from `start` to `end`.

#### `plot_graph(graph, path)`

- **Parameters**:
  - `graph`: A dictionary representing the graph as an adjacency list.
  - `path`: A list of nodes representing the shortest path to be highlighted.

- **Description**:
  - This function creates a visual representation of the graph using `networkx` and `matplotlib`. It highlights the shortest path in red.

### Example Usage

The script provides an example graph and runs Dijkstra's algorithm for multiple start and end nodes defined in `RoadMap`. It prints the shortest distances and paths and plots the graph.

```python
# Example graph represented as an adjacency list
graph = {
    'A': {'B': 1.2, 'H': 4},
    'B': {'A': 1.2, 'C': 7},
    'C': {'A': 5, 'B': 7, 'D': 7.3 , 'E':6 ,'G':6,'H':3.2},
    'D': {'E': 1.5, 'C': 7.3,'F':3},
    'E': {'D': 1.5, 'F': 2,'C':6},
    'F': {'D': 3, 'E': 2,'H':7.1,'G':8},
    'G': {'F': 8, 'C': 6},
    'H': {'A': 4, 'C': 3.2,'F':7.1}
}

# Run Dijkstra's algorithm for specified start and end nodes
RoadMap  = [['A','F'],['F','B'],['B','E'],['E','H']]
for road in RoadMap:
    start = road[0]
    destination = road[1]
    distance, path = dijkstra(graph, start, destination)
    print(f"Shortest distance from {start} to {destination} is {distance}")
    print(f"Path: {path}")
    plot_graph(graph, path)
```

### Output

The script will output the shortest distances and paths for the specified routes in `RoadMap` and display the corresponding graphs with highlighted paths.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
