from get_random import get_random_solution
from aval import aval
from vizinhos import get_vizinhos, get_best_vizinhos

def hill_climbing(search_space, viz_limit):
  current_solution = get_random_solution(search_space)
  current_euclidean_distance = aval(current_solution, search_space)
  vizinhos = get_vizinhos(current_solution, viz_limit)
  best_vizinho, best_euclidean_distance = get_best_vizinhos(search_space, vizinhos)

  while (best_euclidean_distance < current_euclidean_distance):
    current_solution = best_vizinho
    current_euclidean_distance = best_euclidean_distance
    vizinhos = get_vizinhos(current_solution, viz_limit)
    best_vizinho, best_euclidean_distance = get_best_vizinhos(search_space, vizinhos) 

  return current_euclidean_distance