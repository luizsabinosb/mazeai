import pygame
from config import CELL_SIZE, CORES

def desenhar_labirinto(tela, labirinto, caminho=[], fim=None):
    for i in range(len(labirinto)):
        for j in range(len(labirinto[0])):
            cor = CORES["parede"] if labirinto[i][j] == 1 else CORES["caminho"]
            pygame.draw.rect(
                tela,
                cor,
                (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

    # Células visitadas (trajetória da IA)
    for (i, j) in caminho:
        pygame.draw.rect(
            tela,
            CORES["visitado"],
            (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        )

    # Posição atual do agente
    if caminho:
        i, j = caminho[-1]
        pygame.draw.rect(
            tela,
            CORES["agente"],
            (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        )

    # Objetivo (fim)
    if fim:
        i, j = fim
        pygame.draw.rect(
            tela,
            CORES["objetivo"],
            (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        )
