import pygame
from config import CELL_SIZE, FPS, TAMANHOS, CORES
from generation.generator import gerar_labirinto
from ia.bfs import bfs
from ia.astar import astar
from ia.bfs_ruim import bfs_pior
from ia.astar_ruim import astar_ruim
from interface.visual import desenhar_labirinto
from interface.ui import Botao

ALTURA_BOTOES = 60
LINHAS_BOTOES = 2
ESPACO_TOTAL = ALTURA_BOTOES * LINHAS_BOTOES

class Estado:
    def __init__(self):
        self.dificuldade = "médio"
        self.algoritmo = "BFS"
        self.labirinto, self.inicio, self.fim = gerar_labirinto(*TAMANHOS[self.dificuldade])
        self.caminho = self.resolver()

    def resolver(self):
        if self.algoritmo == "BFS":
            return bfs(self.labirinto, self.inicio, self.fim)
        elif self.algoritmo == "A*":
            return astar(self.labirinto, self.inicio, self.fim)
        elif self.algoritmo == "PIOR":
            return bfs_pior(self.labirinto, self.inicio, self.fim, max_nos=50000, timeout=2.0)
        elif self.algoritmo == "A*_RUIM":
            return astar_ruim(self.labirinto, self.inicio, self.fim)
        return []

    def atualizar_labirinto(self, dificuldade):
        self.dificuldade = dificuldade
        self.labirinto, self.inicio, self.fim = gerar_labirinto(*TAMANHOS[dificuldade])
        self.caminho = self.resolver()

    def mudar_algoritmo(self, novo_alg):
        self.algoritmo = novo_alg
        self.caminho = self.resolver()

def calcular_dimensoes(dificuldade):
    linhas, colunas = TAMANHOS[dificuldade]
    largura_labirinto = colunas * CELL_SIZE
    largura_minima = 800
    largura = max(largura_labirinto, largura_minima)
    altura = linhas * CELL_SIZE + ESPACO_TOTAL
    return largura, altura, linhas

def main():
    pygame.init()
    fonte = pygame.font.SysFont(None, 24)
    estado = Estado()
    largura, altura, linhas = calcular_dimensoes(estado.dificuldade)
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("mazeai - Labirinto com IA")
    clock = pygame.time.Clock()
    passo = 0

    def redimensionar(dificuldade):
        nonlocal tela, altura, largura, botoes, passo
        estado.atualizar_labirinto(dificuldade)
        largura, altura, _ = calcular_dimensoes(dificuldade)
        tela = pygame.display.set_mode((largura, altura))
        botoes = criar_botoes(altura, largura)
        passo = 0

    def usar_bfs():
        nonlocal passo
        estado.mudar_algoritmo("BFS")
        passo = 0

    def usar_astar():
        nonlocal passo
        estado.mudar_algoritmo("A*")
        passo = 0

    def usar_pior():
        nonlocal passo
        estado.mudar_algoritmo("PIOR")
        passo = 0

    def usar_astar_ruim():
        nonlocal passo
        estado.mudar_algoritmo("A*_RUIM")
        passo = 0

    def criar_botoes(altura_real, largura_real):
        botoes = []
        largura_botao = 130
        espacamento = 20
        topo_labirinto = altura_real - ESPACO_TOTAL + 20
        topo_caminho = topo_labirinto + ALTURA_BOTOES

        botoes_lab = [
            ("Fácil", lambda: redimensionar("fácil"), (180, 180, 180), (220, 220, 220)),
            ("Médio", lambda: redimensionar("médio"), (180, 180, 180), (220, 220, 220)),
            ("Difícil", lambda: redimensionar("difícil"), (180, 180, 180), (220, 220, 220)),
        ]
        botoes_path = [
            ("BFS", usar_bfs, (150, 200, 255), (180, 220, 255)),
            ("A*", usar_astar, (150, 200, 255), (180, 220, 255)),
            ("BFS Ruim", usar_pior, (255, 180, 180), (255, 200, 200)),
            ("A* Ruim", usar_astar_ruim, (255, 150, 255), (255, 200, 255)),
        ]

        def distribuir_botoes(lista, y_pos):
            total = len(lista) * largura_botao + (len(lista) - 1) * espacamento
            inicio_x = (largura_real - total) // 2
            for i, (texto, acao, cor, cor_hover) in enumerate(lista):
                x = inicio_x + i * (largura_botao + espacamento)
                botoes.append(Botao(texto, x, y_pos, largura_botao, 30, cor, cor_hover, acao))

        distribuir_botoes(botoes_lab, topo_labirinto)
        distribuir_botoes(botoes_path, topo_caminho)
        return botoes

    botoes = criar_botoes(altura, largura)

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        tela.fill(CORES["fundo"])
        caminho_atual = estado.caminho[:passo + 1]
        desenhar_labirinto(tela, estado.labirinto, caminho_atual, estado.fim)

        tela.blit(fonte.render("LABIRINTO:", True, (0, 0, 0)), (20, altura - ESPACO_TOTAL + 5))
        tela.blit(fonte.render("CAMINHO:", True, (0, 0, 0)), (20, altura - ALTURA_BOTOES + 5))

        for botao in botoes:
            botao.desenhar(tela)

        pygame.display.flip()
        passo = min(passo + 1, len(estado.caminho) - 1)
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()