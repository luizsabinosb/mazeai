import heapq

def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # distância de Manhattan

def astar(labirinto, inicio, fim):
    linhas, colunas = len(labirinto), len(labirinto[0])
    fila = []
    heapq.heappush(fila, (0, inicio))
    veio_de = {}
    custo_total = {inicio: 0}

    while fila:
        _, atual = heapq.heappop(fila)

        if atual == fim:
            break

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            vizinho = (atual[0]+dx, atual[1]+dy)
            if 0 <= vizinho[0] < linhas and 0 <= vizinho[1] < colunas:
                if labirinto[vizinho[0]][vizinho[1]] == 1:
                    continue
                novo_custo = custo_total[atual] + 1
                if vizinho not in custo_total or novo_custo < custo_total[vizinho]:
                    custo_total[vizinho] = novo_custo
                    prioridade = novo_custo + heuristica(vizinho, fim)
                    heapq.heappush(fila, (prioridade, vizinho))
                    veio_de[vizinho] = atual

    # Reconstroi caminho
    caminho = []
    atual = fim
    while atual != inicio:
        caminho.append(atual)
        atual = veio_de.get(atual)
        if atual is None:
            return []  # sem caminho
    caminho.append(inicio)
    caminho.reverse()
    return caminho
