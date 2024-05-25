using System;
using System.Collections.Generic;

class Program
{
    public static void Main()
    {
        // Example graph represented as an adjacency list
        var graph = new Dictionary<string, Dictionary<string, double>>
        {
            { "A", new Dictionary<string, double> { { "B", 1.2 }, { "H", 4 } } },
            { "B", new Dictionary<string, double> { { "A", 1.2 }, { "C", 7 } } },
            { "C", new Dictionary<string, double> { { "A", 5 }, { "B", 7 }, { "D", 7.3 }, { "E", 6 }, { "G", 6 }, { "H", 3.2 } } },
            { "D", new Dictionary<string, double> { { "E", 1.5 }, { "C", 7.3 }, { "F", 3 } } },
            { "E", new Dictionary<string, double> { { "D", 1.5 }, { "F", 2 }, { "C", 6 } } },
            { "F", new Dictionary<string, double> { { "D", 3 }, { "E", 2 }, { "H", 7.1 }, { "G", 8 } } },
            { "G", new Dictionary<string, double> { { "F", 8 }, { "C", 6 } } },
            { "H", new Dictionary<string, double> { { "A", 4 }, { "C", 3.2 }, { "F", 7.1 } } }
        };

        // Run Dijkstra's algorithm for specified start and end nodes
        var roadMap = new List<Tuple<string, string>>
        {
            Tuple.Create("A", "F"),
            Tuple.Create("F", "B"),
            Tuple.Create("B", "E"),
            Tuple.Create("E", "H")
        };

        foreach (var road in roadMap)
        {
            var start = road.Item1;
            var destination = road.Item2;
            var (distance, path) = Dijkstra(graph, start, destination);
            Console.WriteLine($"Shortest distance from {start} to {destination} is {distance}");
            Console.WriteLine($"Path: {string.Join(" -> ", path)}");
        }
    }

    public static (double, List<string>) Dijkstra(Dictionary<string, Dictionary<string, double>> graph, string start, string end)
    {
        var distances = new Dictionary<string, double>();
        var previousNodes = new Dictionary<string, string>();
        var priorityQueue = new SortedSet<(double, string)>();

        foreach (var node in graph.Keys)
        {
            distances[node] = double.PositiveInfinity;
            previousNodes[node] = null;
        }
        distances[start] = 0;
        priorityQueue.Add((0, start));

        while (priorityQueue.Count > 0)
        {
            var (currentDistance, currentNode) = priorityQueue.Min;
            priorityQueue.Remove(priorityQueue.Min);

            if (currentDistance > distances[currentNode])
                continue;

            if (currentNode == end)
                break;

            foreach (var neighbor in graph[currentNode].Keys)
            {
                var distance = currentDistance + graph[currentNode][neighbor];

                if (distance < distances[neighbor])
                {
                    priorityQueue.Remove((distances[neighbor], neighbor));
                    distances[neighbor] = distance;
                    previousNodes[neighbor] = currentNode;
                    priorityQueue.Add((distance, neighbor));
                }
            }
        }

        var path = new List<string>();
        var current = end;
        while (current != null)
        {
            path.Add(current);
            current = previousNodes[current];
        }
        path.Reverse();

        return (distances[end], path);
    }
}
