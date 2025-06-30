import heapq
import time

def heuristica_ruim(a, b):
    # Inverte a heurística tradicional (prefere se afastar do objetivo)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_ruim(matriz, inicio, fim, max_nos=100000, timeout=2.0):
    inicio_tempo = time.time()
    heap = []
    visitados = set()

    # Começa com heurística negativa para piorar o caminho (distanciar do objetivo)
    heapq.heappush(heap, (-heuristica_ruim(inicio, fim), 0, inicio, [inicio]))
    visitados.add(inicio)

    pior_caminho = []

    while heap and (time.time() - inicio_tempo) < timeout and max_nos > 0:
        _, custo, atual, caminho = heapq.heappop(heap)

        if atual == fim:
            if len(caminho) > len(pior_caminho):
                pior_caminho = caminho
            continue  # continua procurando caminho ainda pior

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = atual[0] + dx, atual[1] + dy
            vizinho = (nx, ny)

            if 0 <= nx < len(matriz) and 0 <= ny < len(matriz[0]):
                if matriz[nx][ny] == 0 and vizinho not in caminho:
                    novo_caminho = caminho + [vizinho]
                    novo_custo = custo + 1
                    prioridade = -(novo_custo + heuristica_ruim(vizinho, fim))  # heurística invertida
                    heapq.heappush(heap, (prioridade, novo_custo, vizinho, novo_caminho))
                    max_nos -= 1

    return pior_caminho
