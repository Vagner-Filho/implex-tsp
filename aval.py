import math

def aval(current_solution, search_space):
  euclidean_distance = 0
  count = 0
  for n in current_solution:
    euclidean_distance += math.sqrt((math.pow((n.x - search_space[count].x), 2)) + (math.pow((n.y - search_space[count].y), 2)))
    count += 1
  return euclidean_distance