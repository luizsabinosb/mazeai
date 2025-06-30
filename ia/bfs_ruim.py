import random
import time

def bfs_pior(matriz, inicio, fim, max_nos=50000, timeout=3.0):
    stack = [(inicio, [inicio])]
    maior_caminho = []
    visitados = set()

    start_time = time.time()

    while stack:
        if len(stack) > max_nos or (time.time() - start_time) > timeout:
            break  # Evita travamento

        atual, caminho = stack.pop()

        if atual == fim:
            if len(caminho) > len(maior_caminho):
                maior_caminho = caminho
            continue

        x, y = atual
        vizinhos = []
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matriz) and 0 <= ny < len(matriz[0]):
                if matriz[nx][ny] == 0 and (nx, ny) not in caminho:
                    vizinhos.append((nx, ny))

        random.shuffle(vizinhos)
        for viz in vizinhos:
            stack.append((viz, caminho + [viz]))

    return maior_caminho
