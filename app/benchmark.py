import time


#  dados fixos                                                         


CONTATOS_ORDENADOS = [
    ("Alice",    "61-9000-0001"),
    ("Bruno",    "61-9000-0002"),
    ("Carlos",   "61-9000-0003"),
    ("Diana",    "61-9000-0004"),
    ("Eduardo",  "61-9000-0005"),
    ("Fernanda", "61-9000-0006"),
    ("Gabriel",  "61-9000-0007"),
    ("Helena",   "61-9000-0008"),
    ("Igor",     "61-9000-0009"),
    ("Julia",    "61-9000-0010"),
]

CONTATOS_ALEATORIOS = [
    ("Pedro",   "61-9001-0001"),
    ("Ana",     "61-9001-0002"),
    ("Lucas",   "61-9001-0003"),
    ("Mariana", "61-9001-0004"),
    ("Thiago",  "61-9001-0005"),
    ("Sofia",   "61-9001-0006"),
    ("Rafael",  "61-9001-0007"),
    ("Beatriz", "61-9001-0008"),
    ("Diego",   "61-9001-0009"),
    ("Camila",  "61-9001-0010"),
]


#  medição                                                             


def _medir_insercoes(arvore, contatos):
    inicio = time.perf_counter()
    for nome, tel in contatos:
        arvore.inserir(nome, tel)
    return time.perf_counter() - inicio


def _medir_buscas(arvore, nomes):
    inicio = time.perf_counter()
    for nome in nomes:
        arvore.buscar(nome)
    return time.perf_counter() - inicio



#  exibição                                                            


def _barra(valor, maximo, largura=20):
    if maximo == 0:
        preenchido = 0
    else:
        preenchido = int((valor / maximo) * largura)
    return "█" * preenchido + "░" * (largura - preenchido)


def _exibir_resultado(label, tempo_bst, tempo_avl, altura_bst, altura_avl):
    maximo_tempo = max(tempo_bst, tempo_avl) or 1
    maximo_altura = max(altura_bst, altura_avl) or 1

    sep  = "─" * 46
    sep2 = f"{'─'*12}┬{'─'*15}┬{'─'*15}"
    sep3 = f"{'─'*12}┼{'─'*15}┼{'─'*15}"

    print(f"\n  ┌{sep}┐")
    print(f"  │  {label:<44}│")
    print(f"  ├{sep2}┤")
    print(f"  │{'':12}│{'  BST':^15}│{'  AVL':^15}│")
    print(f"  ├{sep3}┤")
    print(f"  │ {'Tempo':<11}│ {tempo_bst:.6f}s    │ {tempo_avl:.6f}s    │")
    print(f"  │ {'Altura':<11}│ {altura_bst:<14}│ {altura_avl:<14}│")
    print(f"  │ {'Gráfico':<11}│ {_barra(tempo_bst, maximo_tempo):<14}│ {_barra(tempo_avl, maximo_tempo):<14}│")
    print(f"  └{'─'*12}┴{'─'*15}┴{'─'*15}┘")


def _exibir_arvores(bst, avl, exibir_arvore_fn):
    exibir_arvore_fn(bst.raiz, "BST (sem balanceamento)")
    exibir_arvore_fn(avl.raiz, "AVL (balanceada)", get_fb=lambda n: avl._fb(n))



#  cenários                                                            


def cenario_ordenado(BST, AVL, exibir_arvore_fn):
    print("\n>>> CENÁRIO 1: Inserção em ordem alfabética (pior caso BST)")

    bst = BST()
    avl = AVL()
    nomes = [n for n, _ in CONTATOS_ORDENADOS]

    t_ins_bst = _medir_insercoes(bst, CONTATOS_ORDENADOS)
    t_ins_avl = _medir_insercoes(avl, CONTATOS_ORDENADOS)

    h_bst = bst.altura(bst.raiz)
    h_avl = avl._altura(avl.raiz)

    _exibir_resultado("Inserção ordenada", t_ins_bst, t_ins_avl, h_bst, h_avl)

    t_bus_bst = _medir_buscas(bst, nomes)
    t_bus_avl = _medir_buscas(avl, nomes)

    _exibir_resultado("Busca (após inserção ordenada)", t_bus_bst, t_bus_avl, h_bst, h_avl)

    _exibir_arvores(bst, avl, exibir_arvore_fn)


def cenario_aleatorio(BST, AVL, exibir_arvore_fn):
    print("\n>>> CENÁRIO 2: Inserção em ordem aleatória (caso médio)")

    bst = BST()
    avl = AVL()
    nomes = [n for n, _ in CONTATOS_ALEATORIOS]

    t_ins_bst = _medir_insercoes(bst, CONTATOS_ALEATORIOS)
    t_ins_avl = _medir_insercoes(avl, CONTATOS_ALEATORIOS)

    h_bst = bst.altura(bst.raiz)
    h_avl = avl._altura(avl.raiz)

    _exibir_resultado("Inserção aleatória", t_ins_bst, t_ins_avl, h_bst, h_avl)

    t_bus_bst = _medir_buscas(bst, nomes)
    t_bus_avl = _medir_buscas(avl, nomes)

    _exibir_resultado("Busca (após inserção aleatória)", t_bus_bst, t_bus_avl, h_bst, h_avl)

    _exibir_arvores(bst, avl, exibir_arvore_fn)



#  ponto de entrada                                                    


def rodar_benchmark(BST, AVL, exibir_arvore_fn):
    print("\n" + "=" * 50)
    print("           BENCHMARK — BST vs AVL")
    print("=" * 50)
    print("  Comparando inserção e busca em dois cenários:")
    print("  ordenado (pior caso BST) e aleatório (caso médio).")

    cenario_ordenado(BST, AVL, exibir_arvore_fn)
    cenario_aleatorio(BST, AVL, exibir_arvore_fn)

    print("\n" + "=" * 50)
    print("  Benchmark concluído.")
    print("=" * 50)