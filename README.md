# mazeai

Visualizador interativo de labirintos com algoritmos de busca, construído em Python e Pygame. O programa gera labirintos aleatórios em tempo real e mostra, passo a passo, o caminho encontrado por diferentes estratégias de IA — incluindo versões propositalmente "ruins" para fins didáticos de comparação.

## Recursos

- Geração procedural de labirintos via DFS, com ciclos extras para garantir múltiplos caminhos.
- Três níveis de dificuldade (fácil, médio, difícil) que ajustam o tamanho do grid.
- Quatro algoritmos selecionáveis durante a execução:
  - **BFS** — busca em largura, encontra o menor caminho em número de células.
  - **A\*** — busca informada com heurística de Manhattan.
  - **BFS Ruim** — variante limitada/penalizada para ilustrar buscas ineficientes.
  - **A\* Ruim** — variante de A\* com heurística degradada.
- Animação célula por célula do caminho encontrado.

## Estrutura do projeto

```
mazeai/
├── main.py              # Loop principal Pygame, UI e estado
├── config.py            # Tamanho de célula, FPS, tamanhos por dificuldade, paleta
├── generation/
│   └── generator.py     # Geração do labirinto (DFS + ciclos)
├── ia/
│   ├── bfs.py
│   ├── astar.py
│   ├── bfs_ruim.py
│   └── astar_ruim.py
├── interface/
│   ├── ui.py            # Componente de botão
│   └── visual.py        # Renderização do grid
├── utils/
│   └── grid_utils.py
└── data/
    └── mapa.txt
```

## Requisitos

- Python 3.10+
- [Pygame](https://www.pygame.org/)

## Instalação

```bash
pip install pygame
```

## Como executar

A partir da pasta `mazeai/`:

```bash
python main.py
```

Uma janela será aberta com o labirinto e duas linhas de botões:

- **LABIRINTO** — gera um novo labirinto na dificuldade escolhida (Fácil / Médio / Difícil).
- **CAMINHO** — troca o algoritmo de busca (BFS, A\*, BFS Ruim, A\* Ruim) e refaz a animação.

## Configuração

Os parâmetros visuais e os tamanhos de cada dificuldade ficam em [config.py](config.py):

- `CELL_SIZE` — tamanho de cada célula em pixels.
- `FPS` — velocidade da animação.
- `TAMANHOS` — dimensões (linhas, colunas) por dificuldade.
- `CORES` — paleta usada pelo renderizador.
