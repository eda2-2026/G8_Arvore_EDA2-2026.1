from benchmark import rodar_benchmark


#  visualização ASCII                                                  


def _linhas_arvore(node, prefixo="", eh_esquerdo=True, get_fb=None):
    if node is None:
        return []

    fb_str = ""
    if get_fb is not None:
        fb_str = f"|FB:{get_fb(node)}"

    linhas = []
    conector = "├── " if eh_esquerdo else "└── "
    linhas.append(prefixo + conector + f"[{node.nome}{fb_str}]")

    extensao = "│   " if eh_esquerdo else "    "
    novo_prefixo = prefixo + extensao

    if node.esq or node.dir:
        linhas += _linhas_arvore(node.esq,  novo_prefixo, True,  get_fb)
        linhas += _linhas_arvore(node.dir,  novo_prefixo, False, get_fb)

    return linhas


def exibir_arvore(raiz, titulo, get_fb=None):
    print(f"\n{'='*40}")
    print(f"  {titulo}")
    print(f"{'='*40}")

    if raiz is None:
        print("  (árvore vazia)")
        return

    fb_str = ""
    if get_fb is not None:
        fb_str = f"|FB:{get_fb(raiz)}"

    print(f"[{raiz.nome}{fb_str}]")

    if raiz.esq or raiz.dir:
        linhas  = _linhas_arvore(raiz.esq,  "", True,  get_fb)
        linhas += _linhas_arvore(raiz.dir,  "", False, get_fb)
        for l in linhas:
            print(l)



#  Helpers de entrada                                                  


def _input_contato():
    while True:
        nome = input("  Nome: ").strip()
        if not nome:
            print("  Nome não pode ser vazio.")
            continue
        telefone = input("  Telefone: ").strip()
        if not telefone:
            print("  Telefone não pode ser vazio.")
            continue
        return nome, telefone


def _input_nome():
    while True:
        nome = input("  Nome: ").strip()
        if nome:
            return nome
        print("  Nome não pode ser vazio.")



#  Menu principal                                                      


def menu(bst, avl, BST, AVL):
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
            print("\n-- Inserir contato --")
            nome, telefone = _input_contato()
            bst.inserir(nome, telefone)
            avl.inserir(nome, telefone)
            print(f"\n  '{nome}' inserido com sucesso!")
            exibir_arvore(bst.raiz, "BST (sem balanceamento)")
            exibir_arvore(avl.raiz, "AVL (balanceada)", get_fb=lambda n: avl._fb(n))

        elif opcao == "2":
            print("\n-- Remover contato --")
            nome = _input_nome()
            bst.remover(nome)
            avl.remover(nome)
            print(f"\n  '{nome}' removido (se existia).")
            exibir_arvore(bst.raiz, "BST (sem balanceamento)")
            exibir_arvore(avl.raiz, "AVL (balanceada)", get_fb=lambda n: avl._fb(n))

        elif opcao == "3":
            print("\n-- Buscar contato --")
            nome = _input_nome()
            res_bst = bst.buscar(nome)
            res_avl = avl.buscar(nome)
            print()
            if res_bst:
                print(f"  BST → {res_bst.nome}: {res_bst.telefone}")
            else:
                print(f"  BST → '{nome}' não encontrado.")
            if res_avl:
                print(f"  AVL → {res_avl.nome}: {res_avl.telefone}")
            else:
                print(f"  AVL → '{nome}' não encontrado.")

        elif opcao == "4":
            print("\n-- Listagem em ordem --")
            lista_bst = bst.em_ordem()
            lista_avl = avl.em_ordem()
            print("\n  BST:")
            for nome, tel in lista_bst:
                print(f"    {nome}: {tel}")
            print("\n  AVL:")
            for nome, tel in lista_avl:
                print(f"    {nome}: {tel}")

        elif opcao == "5":
            rodar_benchmark(BST, AVL, exibir_arvore)

        elif opcao == "6":
            print("\nAté mais!")
            break

        else:
            print("Opção inválida.")