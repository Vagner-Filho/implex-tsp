from random import randrange

def get_random_solution(space):
  nodes = list(range(len(space)))
  random_solution = []

  for v in range(0, len(space)):
    random_node = nodes[randrange(0, len(nodes))]
    random_solution.append(space[random_node])
    nodes.remove(random_node)

  return random_solution