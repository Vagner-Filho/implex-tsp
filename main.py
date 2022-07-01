from hill_climbing import hill_climbing
from simulated_annealing import simulated_annealing
from read_input import read_input

search_space, user_options = read_input()

viz_limit = int(user_options.get('viz_limit'))
metaheuristic = user_options.get('metaheuristic')

if (viz_limit == 0 or viz_limit > len(search_space)):
  viz_limit = len(search_space)
if  (viz_limit > len(search_space)):
  print('Limite de vizinhos excedido. O máximo será utilizado.')

if (metaheuristic == 'h'):
  print(hill_climbing(search_space, viz_limit))
elif (metaheuristic == 's'):
  print(f'Caso A: {simulated_annealing(search_space)}')
  print(f'Caso B: {simulated_annealing(search_space, 100, 0.9, 25, 10)}')

  print('Selecione os parâmetros: ')
  tmax = int(input('t_max = '))
  k = float(input('k = '))
  iteration_amount = int(input('iteration_amount = '))
  tmin = int(input('t_min = '))

  print(f'Caso C: {simulated_annealing(search_space, tmax, k, iteration_amount, tmin)}')
