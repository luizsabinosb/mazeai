from collections import deque

def bfs(labirinto, inicio, fim):
    linhas, colunas = len(labirinto), len(labirinto[0])
    visitado = [[False]*colunas for _ in range(linhas)]
    pai = [[None]*colunas for _ in range(linhas)]

    fila = deque()
    fila.append(inicio)
    visitado[inicio[0]][inicio[1]] = True

    direcoes = [(-1,0), (1,0), (0,-1), (0,1)]

    while fila:
        atual = fila.popleft()
        if atual == fim:
            break

        for d in direcoes:
            ni, nj = atual[0] + d[0], atual[1] + d[1]
            if 0 <= ni < linhas and 0 <= nj < colunas:
                if labirinto[ni][nj] == 0 and not visitado[ni][nj]:
                    fila.append((ni, nj))
                    visitado[ni][nj] = True
                    pai[ni][nj] = atual

    caminho = []
    pos = fim
    while pos and pos != inicio:
        caminho.append(pos)
        pos = pai[pos[0]][pos[1]]

    if pos:
        caminho.append(inicio)
        caminho.reverse()
        return caminho
    return []
