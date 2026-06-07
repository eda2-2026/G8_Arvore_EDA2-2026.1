# bst.py - Pessoa 1
# Árvore Binária de Busca simples (sem balanceamento).

class NodeBST:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.esq = None
        self.dir = None


class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, nome, telefone):
        # TODO Pessoa 1: implementar inserção recursiva (chave = nome)
        pass

    def _inserir(self, node, nome, telefone):
        # TODO Pessoa 1: helper recursivo de inserção
        pass

    def remover(self, nome):
        # TODO Pessoa 1: implementar remoção recursiva
        pass

    def _remover(self, node, nome):
        # TODO Pessoa 1: helper recursivo de remoção
        pass

    def _minimo(self, node):
        # TODO Pessoa 1: retorna o nó com menor chave numa subárvore
        pass

    def buscar(self, nome):
        # TODO Pessoa 1: retorna o nó com o nome dado, ou None
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

    def altura(self, node):
        # TODO Pessoa 1: retorna a altura do nó (None = -1)
        pass
