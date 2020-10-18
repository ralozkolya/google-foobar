from itertools import permutations

def solution(times, time_limit):
  bunny_count = len(times) - 2
  indices = [bunny + 1 for bunny in range(bunny_count)]

  bellman_ford_matrix = bellman_ford_complete(times)
  if has_negative_cycle(bellman_ford_matrix):
    return range(bunny_count)

  for width in range(bunny_count, 0, -1):
    for perm in permutations(indices, width):
      cost = get_path_cost(perm, bellman_ford_matrix)
      if cost <= time_limit:
        return [bunny - 1 for bunny in sorted(perm)]
  
  return []


def get_path_cost( bunnies, distanceMatrix ):
  cost = 0
  for i in range(0, len(bunnies) - 1):
      _from = bunnies[i]
      _to = bunnies[i + 1]
      cost += distanceMatrix[_from][_to]
  startNode = 0
  endNode = len(distanceMatrix) - 1
  cost += distanceMatrix[startNode][bunnies[0]]
  cost += distanceMatrix[bunnies[-1]][endNode]
  return cost

def bellman_ford_complete(edges):
  distanceMatrix = []
  for vertex in range( len(edges) ):
    distances = bellman_ford(edges, vertex)
    distanceMatrix.append(distances)
  return distanceMatrix

def bellman_ford(edges, start):
  distances = [ float('inf') for vertex in edges ]
  distances[start] = edges[start][start]
  for _ in range(len(edges)):
    for u, v, weight in enumerate_edges(edges):
      if distances[u] + weight < distances[v]:
        distances[v] = distances[u] + weight
  return distances
    
def enumerate_edges(edges):
  for u, row in enumerate(edges):
    for v, weight in enumerate(row):
      yield (u, v, weight)

def has_negative_cycle(bellmanFordMatrix):
  distances = bellmanFordMatrix[0]
  for u, v, weight in enumerate_edges(bellmanFordMatrix):
    if distances[u] + weight < distances[v]:
      return True
  return False
