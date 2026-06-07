# avl.py - Pessoa 1
# Árvore AVL (balanceada). Herda a lógica base da BST e adiciona
# cálculo de fator de balanceamento + rotações.

class NodeAVL:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.esq = None
        self.dir = None
        self.altura = 0


class AVL:
    def __init__(self):
        self.raiz = None

    # ------------------------------------------------------------------ #
    #  Utilitários                                                         #
    # ------------------------------------------------------------------ #

    def _altura(self, node):
        # TODO Pessoa 1: retorna node.altura ou -1 se None
        pass

    def _atualizar_altura(self, node):
        # TODO Pessoa 1: recalcula node.altura com base nos filhos
        pass

    def _fb(self, node):
        # TODO Pessoa 1: fator de balanceamento = altura(dir) - altura(esq)
        pass

    # ------------------------------------------------------------------ #
    #  Rotações                                                            #
    # ------------------------------------------------------------------ #

    def _rot_esq(self, p):
        # TODO Pessoa 1: rotação simples à esquerda; retorna nova raiz
        pass

    def _rot_dir(self, p):
        # TODO Pessoa 1: rotação simples à direita; retorna nova raiz
        pass

    def _rot_dir_esq(self, p):
        # TODO Pessoa 1: rotação dupla direita-esquerda; retorna nova raiz
        pass

    def _rot_esq_dir(self, p):
        # TODO Pessoa 1: rotação dupla esquerda-direita; retorna nova raiz
        pass

    # ------------------------------------------------------------------ #
    #  Rebalanceamento                                                     #
    # ------------------------------------------------------------------ #

    def _balancear(self, node):
        # TODO Pessoa 1: verifica FB e aplica a rotação correta (casos 1 e 2)
        pass

    # ------------------------------------------------------------------ #
    #  Operações públicas                                                  #
    # ------------------------------------------------------------------ #

    def inserir(self, nome, telefone):
        # TODO Pessoa 1: chama _inserir e atualiza self.raiz
        pass

    def _inserir(self, node, nome, telefone):
        # TODO Pessoa 1: insere recursivamente e rebalanceia no retorno
        pass

    def remover(self, nome):
        # TODO Pessoa 1: chama _remover e atualiza self.raiz
        pass

    def _remover(self, node, nome):
        # TODO Pessoa 1: remove recursivamente e rebalanceia no retorno
        pass

    def _minimo(self, node):
        # TODO Pessoa 1: retorna o nó com menor chave (usado na remoção)
        pass

    def buscar(self, nome):
        # TODO Pessoa 1: retorna NodeAVL com o nome dado, ou None
        pass

    def _buscar(self, node, nome):
        # TODO Pessoa 1: helper recursivo de busca
        pass

    def em_ordem(self):
        # TODO Pessoa 1: retorna lista de (nome, telefone) em ordem alfabética
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado

    def _em_ordem(self, node, resultado):
        # TODO Pessoa 1: helper recursivo do percurso em ordem
        pass
