from aval import aval
from get_random import get_random_solution
import math
from random import randrange

def simulated_annealing(search_space, t_max = 10, k = 0.95, iteration_amount = 20, t_min = 5):
  scoped_t_max = t_max
  current_solution = get_random_solution(search_space)
  current_euclidean_distance = aval(current_solution, search_space)
  while scoped_t_max > t_min:
    t = 0
    while t < iteration_amount:
      new_solution = get_random_solution(current_solution)
      new_euclidean_distance = aval(new_solution, current_solution)

      if (new_euclidean_distance < current_euclidean_distance):
        current_euclidean_distance = new_euclidean_distance
      elif (randrange(0, 1) < math.e * ((current_euclidean_distance - new_euclidean_distance) / scoped_t_max)):
        current_euclidean_distance = new_euclidean_distance

      t += 1
    scoped_t_max = k * scoped_t_max
  return current_euclidean_distance  
