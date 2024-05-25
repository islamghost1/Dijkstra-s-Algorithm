import heapq
import networkx as nx
import matplotlib.pyplot as plt
def dijkstra(graph, start, end):
    # Create a dictionary to store the shortest distance to each node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Create a dictionary to store the path
    previous_nodes = {node: None for node in graph}
    
    # Priority queue to store the nodes to be explored
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If the current distance is greater than the recorded shortest distance, skip it
        if current_distance > distances[current_node]:
            continue
        
        # If we've reached the destination node, break
        if current_node == end:
            break
        
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's shorter
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Reconstruct the path from start to end
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path = path[::-1]  # Reverse the path to get it from start to end
    
    return distances[end], path
def plot_graph(graph, path):
    G = nx.Graph()
    
    # Add edges to the graph
    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)
    
    pos = nx.spring_layout(G)  # positions for all nodes
    
    # Draw the nodes and edges
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
    
    # Highlight the path
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=8, alpha=0.5, edge_color='r')
    
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.axis('off')
    plt.show()
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

# Run Dijkstra's algorithm from nodes wanted
RoadMap  = [['A','F'],['F','B'],['B','E'],['E','H']]
for road in RoadMap:
    start = road[0]
    destination = road[1]
    distance, path = dijkstra(graph, start, destination)
    print(f"Shortest distance from {start} to {destination} is {distance}")
    print(f"Path: {path}")
    plot_graph(graph,path)
