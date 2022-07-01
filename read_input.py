import sys

class Node:
  def __init__(self, v, x, y):
    self.v = v
    self.x = x
    self.y = y

def read_input():
  try:
    with open(sys.argv[1], 'r') as f:
      rawContent = f.readlines()

      content = []
      for rawNode in rawContent:
        if (rawNode != '\n'):
          node = rawNode.split()
          nodei = Node(float(node[0]), float(node[1]), float(node[2]))
          content.append(nodei)

    if (len(content) < 1):
      return 'Input vazio'

    metaheuristic = input('Metaheuristica Hill Climbing (h) ou Simulated Annealing (s): ')
    if (metaheuristic == 'h'):
      viz_limit = input('Limite máximo de vizinhos (0 para máximo): ')
    else:
      viz_limit = 0

    user_options = {
      "metaheuristic": metaheuristic,
      "viz_limit": viz_limit
    }

    return content, user_options
  except Exception as e:
    print(e)