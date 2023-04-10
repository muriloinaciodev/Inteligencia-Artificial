def busca_profundidade_limitada(estado_inicial, teste_objetivo, acoes, custo, limite_profundidade):
    return busca_profundidade_limitada_recursiva(estado_inicial, teste_objetivo, acoes, custo, limite_profundidade)

def busca_profundidade_limitada_recursiva(estado_atual, teste_objetivo, acoes, custo, limite_profundidade, profundidade=0):
    if profundidade > limite_profundidade:
        return None
    if teste_objetivo(estado_atual):
        return estado_atual
    sucessores = acoes(estado_atual)
    for sucessor in sucessores:
        resultado = busca_profundidade_limitada_recursiva(sucessor, teste_objetivo, acoes, custo, limite_profundidade, profundidade+1)
        if resultado is not None:
            return resultado
    return None
