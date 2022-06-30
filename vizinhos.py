from aval import aval
from random import randrange

def get_vizinhos(solution):
  vizinhos = []

  for i in range(len(solution)):
    for j in range(i + 1, len(solution)):
      vizinho = solution.copy()
      vizinho[i] = solution[j]
      vizinho[j] = solution[i]
      vizinhos.append(vizinho)
  return vizinhos

def get_best_vizinhos(search_space, vizinhos):
  # random_viz = randrange(0, len(vizinhos))
  random_viz = 0
  best_euclidean_distance = aval(vizinhos[random_viz], search_space)
  best_vizinho = vizinhos[random_viz]
  for viz in vizinhos:
    current_euclidean_distance = aval(viz, search_space)
    if (current_euclidean_distance < best_euclidean_distance and current_euclidean_distance > 0):
      best_euclidean_distance = current_euclidean_distance
      best_vizinho = viz
  return best_vizinho, best_euclidean_distance