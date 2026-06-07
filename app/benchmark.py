# benchmark.py - Pessoa 2
# Módulo de benchmark: insere uma sequência de contatos nas duas árvores,
# mede o tempo de cada operação e exibe a comparação visual e numérica.

import time
import random
import string

# ------------------------------------------------------------------ #
#  Geração de dados                                                    #
# ------------------------------------------------------------------ #

# Sequência já ordenada — pior caso para a BST (vira lista encadeada)
CONTATOS_ORDENADOS = [
    ("Alice", "61-9000-0001"),
    ("Bruno", "61-9000-0002"),
    ("Carlos", "61-9000-0003"),
    ("Diana", "61-9000-0004"),
    ("Eduardo", "61-9000-0005"),
    ("Fernanda", "61-9000-0006"),
    ("Gabriel", "61-9000-0007"),
    ("Helena", "61-9000-0008"),
    ("Igor", "61-9000-0009"),
    ("Julia", "61-9000-0010"),
]

# Sequência aleatória — caso médio
CONTATOS_ALEATORIOS = [
    ("Pedro", "61-9001-0001"),
    ("Ana", "61-9001-0002"),
    ("Lucas", "61-9001-0003"),
    ("Mariana", "61-9001-0004"),
    ("Thiago", "61-9001-0005"),
    ("Sofia", "61-9001-0006"),
    ("Rafael", "61-9001-0007"),
    ("Beatriz", "61-9001-0008"),
    ("Diego", "61-9001-0009"),
    ("Camila", "61-9001-0010"),
]


# ------------------------------------------------------------------ #
#  Medição de tempo                                                    #
# ------------------------------------------------------------------ #

def _medir_insercoes(arvore, contatos):
    """
    TODO Pessoa 2: insere cada contato na árvore medindo o tempo total.
    Retorna o tempo em segundos (float).

    Dica:
        inicio = time.perf_counter()
        for nome, tel in contatos:
            arvore.inserir(nome, tel)
        return time.perf_counter() - inicio
    """
    # TODO Pessoa 2
    pass


def _medir_buscas(arvore, nomes):
    """
    TODO Pessoa 2: realiza uma busca para cada nome na lista e retorna
    o tempo total em segundos.
    """
    # TODO Pessoa 2
    pass


# ------------------------------------------------------------------ #
#  Exibição dos resultados                                             #
# ------------------------------------------------------------------ #

def _barra(valor, maximo, largura=30):
    """
    TODO Pessoa 2: retorna uma string de barra ASCII proporcional ao valor.

    Exemplo com largura=20:
        valor=0.003, maximo=0.010  →  "██████░░░░░░░░░░░░░░"
    """
    # TODO Pessoa 2
    pass


def _exibir_resultado(label, tempo_bst, tempo_avl, altura_bst, altura_avl):
    """
    TODO Pessoa 2: imprime uma tabela comparativa com barras ASCII.

    Exemplo de saída esperada:

    ┌─────────────────────────────────────────┐
    │  Inserção ordenada (pior caso BST)      │
    ├──────────┬──────────────┬───────────────┤
    │          │    BST       │      AVL      │
    ├──────────┼──────────────┼───────────────┤
    │ Tempo    │ 0.000412s    │  0.000089s    │
    │ Altura   │ 9            │  3            │
    │ Gráfico  │ ████████████ │  ███          │
    └──────────┴──────────────┴───────────────┘
    """
    # TODO Pessoa 2
    pass


def _exibir_arvores(bst, avl, exibir_arvore_fn):
    """
    TODO Pessoa 2: chama exibir_arvore_fn para desenhar as duas árvores
    em ASCII, igual ao que já existe em interface.py.
    Reaproveite a função exibir_arvore importada de interface.py.
    """
    # TODO Pessoa 2
    pass


# ------------------------------------------------------------------ #
#  Cenários de benchmark                                               #
# ------------------------------------------------------------------ #

def cenario_ordenado(BST, AVL, exibir_arvore_fn):
    """
    TODO Pessoa 2: executa o benchmark com CONTATOS_ORDENADOS.
    - Cria instâncias novas de BST e AVL
    - Mede tempo de inserção nas duas
    - Mede tempo de busca de todos os nomes nas duas
    - Chama _exibir_resultado para inserção e para busca
    - Chama _exibir_arvores para mostrar a diferença visual

    Este é o PIOR CASO da BST: inserção em ordem alfabética degenera
    a BST numa lista encadeada, enquanto a AVL permanece balanceada.
    """
    print("\n>>> CENÁRIO 1: Inserção em ordem alfabética (pior caso BST)")
    # TODO Pessoa 2
    pass


def cenario_aleatorio(BST, AVL, exibir_arvore_fn):
    """
    TODO Pessoa 2: mesmo que cenario_ordenado, mas com CONTATOS_ALEATORIOS.
    Aqui a BST ainda se sai razoavelmente bem; o objetivo é mostrar que
    a AVL é consistentemente boa independente da ordem de inserção.
    """
    print("\n>>> CENÁRIO 2: Inserção em ordem aleatória (caso médio)")
    # TODO Pessoa 2
    pass


# ------------------------------------------------------------------ #
#  Ponto de entrada do benchmark                                       #
# ------------------------------------------------------------------ #

def rodar_benchmark(BST, AVL, exibir_arvore_fn):
    """
    TODO Pessoa 2: exibe cabeçalho e chama os dois cenários em sequência.

    Recebe as classes BST e AVL (não instâncias) para poder criar
    árvores limpas em cada cenário, e exibir_arvore_fn importada
    de interface.py para desenhar as árvores.
    """
    print("\n" + "=" * 50)
    print("       BENCHMARK — BST vs AVL")
    print("=" * 50)
    print("Comparando desempenho de inserção e busca")
    print("em dois cenários: ordenado e aleatório.\n")

    # TODO Pessoa 2: chamar cenario_ordenado e cenario_aleatorio
    pass
