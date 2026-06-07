# interface.py - Pessoa 2
# Menu interativo e visualização ASCII das duas árvores.

from benchmark import rodar_benchmark

# ------------------------------------------------------------------ #
#  Visualização ASCII                                                  #
# ------------------------------------------------------------------ #

def _linhas_arvore(node, prefixo="", eh_esquerdo=True, get_fb=None):
    """
    TODO Pessoa 2: gera uma lista de strings que representam a árvore
    em ASCII de forma recursiva.

    Exemplo de saída esperada:
        [Carlos|FB:0]
        ├── [Ana|FB:0]
        └── [Pedro|FB:-1]
               └── [Maria|FB:0]

    Dica: use os caracteres ├── └── │ para os galhos.
    O parâmetro get_fb é uma função que recebe o nó e retorna o FB
    (para a BST pode ser None e não exibir FB).
    """
    # TODO Pessoa 2
    pass


def exibir_arvore(raiz, titulo, get_fb=None):
    """
    TODO Pessoa 2: imprime o título e chama _linhas_arvore para
    desenhar a árvore no terminal.
    Se raiz for None, imprime "(árvore vazia)".
    """
    print(f"\n{'='*40}")
    print(f"  {titulo}")
    print(f"{'='*40}")
    # TODO Pessoa 2
    pass


# ------------------------------------------------------------------ #
#  Helpers de entrada                                                  #
# ------------------------------------------------------------------ #

def _input_contato():
    """
    TODO Pessoa 2: solicita nome e telefone ao usuário e retorna (nome, telefone).
    Tratar entrada vazia.
    """
    # TODO Pessoa 2
    pass


def _input_nome():
    """
    TODO Pessoa 2: solicita apenas o nome ao usuário e retorna string.
    """
    # TODO Pessoa 2
    pass


# ------------------------------------------------------------------ #
#  Menu principal                                                      #
# ------------------------------------------------------------------ #

def menu(bst, avl, BST, AVL):
    """
    TODO Pessoa 2: loop principal do programa.

    Opções:
        1 - Inserir contato  → insere nas duas árvores e exibe ambas
        2 - Remover contato  → remove das duas e exibe ambas
        3 - Buscar contato   → busca nas duas e exibe resultado
        4 - Listar em ordem  → percurso em ordem (deve ser idêntico nas duas)
        5 - Benchmark        → chama rodar_benchmark(BST, AVL, exibir_arvore)
        6 - Sair

    Após inserção e remoção, exibir as duas árvores com exibir_arvore()
    para o usuário ver a diferença estrutural em tempo real.
    """
    print("=" * 40)
    print("  GERENCIADOR DE CONTATOS — BST vs AVL")
    print("=" * 40)

    while True:
        print("\n[1] Inserir contato")
        print("[2] Remover contato")
        print("[3] Buscar contato")
        print("[4] Listar em ordem")
        print("[5] Benchmark BST vs AVL")
        print("[6] Sair")
        opcao = input("\nEscolha: ").strip()

        if opcao == "1":
            # TODO Pessoa 2: coletar dados e chamar bst.inserir + avl.inserir
            pass

        elif opcao == "2":
            # TODO Pessoa 2: coletar nome e chamar bst.remover + avl.remover
            pass

        elif opcao == "3":
            # TODO Pessoa 2: coletar nome, buscar nas duas e exibir resultado
            pass

        elif opcao == "4":
            # TODO Pessoa 2: exibir em_ordem() das duas árvores
            pass

        elif opcao == "5":
            rodar_benchmark(BST, AVL, exibir_arvore)

        elif opcao == "6":
            print("\nAté mais!")
            break

        else:
            print("Opção inválida.")
