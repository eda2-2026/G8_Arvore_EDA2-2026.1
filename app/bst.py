# bst.py - Pessoa 1
# Árvore Binária de Busca simples (sem balanceamento).
#
# Design: cada nó guarda apenas nome + telefone; as operações de
# inserção/remoção/busca trocam *ponteiros para nós*, nunca copiam
# os dados de um nó para outro (exceto na remoção por sucessor, onde
# apenas os campos de dados são copiados — o nó-alvo é reutilizado).

class NodeBST:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.esq = None
        self.dir = None


class BST:
    def __init__(self):
        self.raiz = None

    # ------------------------------------------------------------------ #
    #  Inserção                                                            #
    # ------------------------------------------------------------------ #

    def inserir(self, nome, telefone):
        """Ponto de entrada público: atualiza self.raiz com o ponteiro
        retornado pelo helper recursivo."""
        self.raiz = self._inserir(self.raiz, nome, telefone)

    def _inserir(self, node, nome, telefone):
        """Desce recursivamente até a posição correta, cria o nó e
        devolve o ponteiro para o nó atual (sem alterá-lo se já existe)."""
        if node is None:
            return NodeBST(nome, telefone)        # novo nó alocado aqui
        if nome < node.nome:
            node.esq = self._inserir(node.esq, nome, telefone)
        elif nome > node.nome:
            node.dir = self._inserir(node.dir, nome, telefone)
        # nome == node.nome → atualiza telefone sem criar novo nó
        else:
            node.telefone = telefone
        return node                               # devolve o mesmo ponteiro

    # ------------------------------------------------------------------ #
    #  Remoção                                                             #
    # ------------------------------------------------------------------ #

    def remover(self, nome):
        """Ponto de entrada público."""
        self.raiz = self._remover(self.raiz, nome)

    def _remover(self, node, nome):
        """Remove o nó de chave `nome` e devolve o ponteiro correto para
        o pai recompor a ligação.  Três casos clássicos:
          • folha  → devolve None
          • 1 filho → devolve o filho (o nó é 'bypassado')
          • 2 filhos → copia dados do sucessor in-order para o nó atual
                       e remove o sucessor na subárvore direita."""
        if node is None:
            return None                           # chave não encontrada
        if nome < node.nome:
            node.esq = self._remover(node.esq, nome)
        elif nome > node.nome:
            node.dir = self._remover(node.dir, nome)
        else:
            # Nó encontrado — três casos
            if node.esq is None:
                return node.dir                   # caso 0/1 filho (dir)
            if node.dir is None:
                return node.esq                   # caso 1 filho (esq)
            # Caso 2 filhos: substitui pelo sucessor in-order (mínimo da dir)
            sucessor = self._minimo(node.dir)
            # Copia apenas os dados; o ponteiro `node` permanece no lugar
            node.nome = sucessor.nome
            node.telefone = sucessor.telefone
            # Remove o sucessor da subárvore direita
            node.dir = self._remover(node.dir, sucessor.nome)
        return node

    def _minimo(self, node):
        """Desce sempre à esquerda até encontrar o nó mínimo.
        Retorna o ponteiro para esse nó (não copia dados)."""
        while node.esq is not None:
            node = node.esq
        return node

    # ------------------------------------------------------------------ #
    #  Busca                                                               #
    # ------------------------------------------------------------------ #

    def buscar(self, nome):
        """Retorna o ponteiro para o NodeBST encontrado, ou None."""
        return self._buscar(self.raiz, nome)

    def _buscar(self, node, nome):
        """Busca binária recursiva; retorna o ponteiro do nó ou None."""
        if node is None:
            return None
        if nome < node.nome:
            return self._buscar(node.esq, nome)
        if nome > node.nome:
            return self._buscar(node.dir, nome)
        return node                               # ponteiro para o nó achado

    # ------------------------------------------------------------------ #
    #  Percurso em ordem                                                   #
    # ------------------------------------------------------------------ #

    def em_ordem(self):
        """Retorna lista de (nome, telefone) em ordem alfabética crescente."""
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado

    def _em_ordem(self, node, resultado):
        """Percurso in-order (esq → raiz → dir) acumula pares na lista."""
        if node is None:
            return
        self._em_ordem(node.esq, resultado)
        resultado.append((node.nome, node.telefone))
        self._em_ordem(node.dir, resultado)

    # ------------------------------------------------------------------ #
    #  Altura                                                              #
    # ------------------------------------------------------------------ #

    def altura(self, node):
        """Retorna a altura do nó (folha = 0, None = -1).
        Calcula recursivamente — O(n) — adequado para BST sem cache."""
        if node is None:
            return -1
        return 1 + max(self.altura(node.esq), self.altura(node.dir))