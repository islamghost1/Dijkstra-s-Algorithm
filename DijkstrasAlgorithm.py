import heapq

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
