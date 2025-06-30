import random

def gerar_labirinto(linhas, colunas):
    # Garante que linhas e colunas sejam ímpares
    if linhas % 2 == 0: linhas += 1
    if colunas % 2 == 0: colunas += 1

    lab = [[1 for _ in range(colunas)] for _ in range(linhas)]

    def dentro(i, j):
        return 0 <= i < linhas and 0 <= j < colunas

    def dfs(x, y):
        direcoes = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(direcoes)
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            if dentro(nx, ny) and lab[nx][ny] == 1:
                lab[nx][ny] = 0
                lab[x + dx // 2][y + dy // 2] = 0
                dfs(nx, ny)

    def adicionar_ciclos(matriz, quantidade):
        tentativas = 0
        adicionados = 0
        max_tentativas = quantidade * 10

        while adicionados < quantidade and tentativas < max_tentativas:
            i = random.randint(1, linhas - 2)
            j = random.randint(1, colunas - 2)
            if matriz[i][j] == 1:
                vizinhos = 0
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + dx, j + dy
                    if dentro(ni, nj) and matriz[ni][nj] == 0:
                        vizinhos += 1
                if vizinhos >= 2:
                    matriz[i][j] = 0
                    adicionados += 1
            tentativas += 1

    # Geração básica com DFS
    lab[1][1] = 0
    dfs(1, 1)

    # Adiciona ciclos para criar múltiplos caminhos
    ciclos = max((linhas * colunas) // 8, 10)  # força ao menos 10 ciclos
    adicionar_ciclos(lab, quantidade=ciclos)

    # Define início e fim
    inicio = (1, 1)
    fim = (linhas - 2, colunas - 2)
    lab[fim[0]][fim[1]] = 0

    return lab, inicio, fim
