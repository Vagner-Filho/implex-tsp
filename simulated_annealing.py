from aval import aval
import math
from random import random
import vizinhos

def simulated_annealing(dominio, funcao_custo, temperatura = 10000.0, resfriamento = 0.95, passo = 1):
    # random.seed(a=0)
    solucao = random.random()
    custos = []
    count = 1
    parar_no_plato = 0

    while temperatura > 0.1:
        vizinhos = vizinhos(solucao, count)
        
        atual = funcao_custo(solucao)
        melhor = atual 
        solucao_atual = solucao
        custos.append(atual)

        for i in range(len(vizinhos)):
            
            if parar_no_plato == 20:
                break

            custo = funcao_custo(vizinhos[i])
            probabilidade = pow(math.e, (-custo - melhor) / temperatura)
            
            if custo >= melhor or random() < probabilidade:
                parar_no_plato = parar_no_plato + 1 if custo == melhor else 0
                melhor = custo
                solucao = vizinhos[i]

        temperatura = temperatura * resfriamento

    return solucao, custos

solucao_tempera_simulada = simulated_annealing([0, 1], aval)
custo_tempera_simulada = aval(solucao_tempera_simulada[0])

print('Menor custo', custo_tempera_simulada)