import pygame

class Botao:
    def __init__(self, texto, x, y, largura, altura, cor, cor_hover, acao=None):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.cor = cor
        self.cor_hover = cor_hover
        self.acao = acao
        self.fonte = pygame.font.SysFont(None, 24)

    def desenhar(self, tela):
        mouse = pygame.mouse.get_pos()
        clicado = pygame.mouse.get_pressed()[0]
        cor_atual = self.cor_hover if self.rect.collidepoint(mouse) else self.cor
        pygame.draw.rect(tela, cor_atual, self.rect)
        texto_img = self.fonte.render(self.texto, True, (0,0,0))
        tela.blit(texto_img, (self.rect.x + 10, self.rect.y + 10))

        if self.rect.collidepoint(mouse) and clicado and self.acao:
            self.acao()
