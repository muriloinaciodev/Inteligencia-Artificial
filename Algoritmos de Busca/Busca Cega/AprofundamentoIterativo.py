def aprofundamento_iterativo(estado_inicial, teste_objetivo, acoes, custo):
    profundidade = 0
    while True:
        resultado = busca_profundidade_limitada(estado_inicial, teste_objetivo, acoes, custo, profundidade)
        if resultado is not None:
            return resultado
        profundidade += 1
