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
        node = rawNode.split()
        nodei = Node(int(node[0]), int(node[1]), int(node[2]))
        content.append(nodei)
    if (len(content) < 1):
      return 'Input vazio'

    return content
  except Exception as e:
    print(e)