from pprint import pprint
from os import system
from time import sleep


def busca_largura(estado_inicial, teste_objetivo, acoes, custo):
    fronteira = [(estado_inicial, None)]
    visitados = {estado_inicial: None}
    while fronteira:
        estado_atual, estado_pai = fronteira.pop(0)
        if teste_objetivo(estado_atual):
            caminho = []
            while estado_atual:
                caminho.append(estado_atual)
                estado_atual = visitados[estado_atual]
            return caminho[::-1]
        sucessores = acoes(estado_atual)
        for sucessor in sucessores:
            if sucessor not in visitados:
                visitados[sucessor] = estado_atual
                fronteira.append((sucessor, estado_atual))
    return None


# Definindo o problema
estado_inicial = (0, 0)  # posição inicial
estado_objetivo = (4, 4)  # posição objetivo
labirinto = [
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

# Definindo as funções


def teste_objetivo(estado):
    return estado == estado_objetivo


def acoes(estado):
    lin, col = estado
    possiveis_acoes = []
    if lin > 0 and labirinto[lin - 1][col] == 0:
        possiveis_acoes.append((lin - 1, col))
    if col > 0 and labirinto[lin][col - 1] == 0:
        possiveis_acoes.append((lin, col - 1)) 
    if lin < len(labirinto) - 1 and labirinto[lin + 1][col] == 0:
        possiveis_acoes.append((lin + 1, col))
    if col < len(labirinto[0]) - 1 and labirinto[lin][col + 1] == 0:
        possiveis_acoes.append((lin, col + 1))
    return possiveis_acoes


def custo(estado, acao):
    return 1


# Chamando a busca em largura
caminho = busca_largura(estado_inicial, teste_objetivo, acoes, custo)

for pos in caminho:
    system('clear')
    print(f'Ação {pos}')
    for il, linha in enumerate(labirinto):
        for ic, coluna in enumerate(linha):
            path = " "
            if (il, ic) == pos:
                path = '+'
            if coluna == 0:
                print(f'\033[42m{path}\033[m', end='')
            else:
                print(f'\033[41m{path}\033[m', end='')
        print()
    sleep(1)
print('Fim da Busca')
