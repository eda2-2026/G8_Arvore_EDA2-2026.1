# Árvore AVL (auto-balanceada). Mesma interface da BST; acrescenta
# campo `altura` em cada nó e rotações para manter |FB| ≤ 1.
#
# Design de ponteiros: igual à BST — as rotações apenas *remapeiam
# ponteiros* entre nós existentes, nunca criam cópias dos dados.

class NodeAVL:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.esq = None
        self.dir = None
        self.altura = 0          # folha começa em 0


class AVL:
    def __init__(self):
        self.raiz = None

    # ------------------------------------------------------------------ #
    #  Utilitários de altura e fator de balanceamento                     #
    # ------------------------------------------------------------------ #

    def _altura(self, node):
        """Retorna node.altura (inteiro ≥ 0) ou -1 para None.
        Leitura de campo O(1) — a altura é mantida atualizada em cache."""
        if node is None:
            return -1
        return node.altura

    def _atualizar_altura(self, node):
        """Recalcula e armazena a altura de `node` a partir dos filhos.
        Chamado após qualquer modificação estrutural no nó."""
        node.altura = 1 + max(self._altura(node.esq), self._altura(node.dir))

    def _fb(self, node):
        """Fator de Balanceamento = altura(dir) − altura(esq).
        • FB > +1 → subárvore direita muito alta → rotação à esquerda
        • FB < −1 → subárvore esquerda muito alta → rotação à direita"""
        if node is None:
            return 0
        return self._altura(node.dir) - self._altura(node.esq)

    # ------------------------------------------------------------------ #
    #  Rotações — apenas remapeiam ponteiros, O(1)                        #
    # ------------------------------------------------------------------ #

    def _rot_esq(self, p):
        q = p.dir                  # q sobe
        p.dir = q.esq              # B migra para filho direito de p
        q.esq = p                  # p desce como filho esquerdo de q
        # ordem importa: atualizar p antes de q
        self._atualizar_altura(p)
        self._atualizar_altura(q)
        return q                   # devolve novo ponteiro para o pai

    def _rot_dir(self, p):
        q = p.esq                  # q sobe
        p.esq = q.dir              # B migra para filho esquerdo de p
        q.dir = p                  # p desce como filho direito de q
        self._atualizar_altura(p)
        self._atualizar_altura(q)
        return q

    def _rot_dir_esq(self, p):
        p.dir = self._rot_dir(p.dir)
        return self._rot_esq(p)

    def _rot_esq_dir(self, p):
        p.esq = self._rot_esq(p.esq)
        return self._rot_dir(p)

    # ------------------------------------------------------------------ #
    #  Rebalanceamento                                                     #
    # ------------------------------------------------------------------ #

    def _balancear(self, node):
        self._atualizar_altura(node)
        fb = self._fb(node)

        if fb == 2:                              # subárvore direita pesada
            if self._fb(node.dir) >= 0:
                return self._rot_esq(node)       # DD
            else:
                return self._rot_dir_esq(node)   # DE

        if fb == -2:                             # subárvore esquerda pesada
            if self._fb(node.esq) <= 0:
                return self._rot_dir(node)       # EE
            else:
                return self._rot_esq_dir(node)   # ED

        return node                              # já balanceado

    # ------------------------------------------------------------------ #
    #  Inserção                                                            #
    # ------------------------------------------------------------------ #

    def inserir(self, nome, telefone):
        """Ponto de entrada público."""
        self.raiz = self._inserir(self.raiz, nome, telefone)

    def _inserir(self, node, nome, telefone):
        """Insere recursivamente e rebalanceia no retorno (bottom-up).
        Retorna o ponteiro correto para o pai (pode mudar após rotação)."""
        if node is None:
            return NodeAVL(nome, telefone)        # novo nó; altura = 0
        if nome < node.nome:
            node.esq = self._inserir(node.esq, nome, telefone)
        elif nome > node.nome:
            node.dir = self._inserir(node.dir, nome, telefone)
        else:
            node.telefone = telefone              # atualiza sem criar nó
            return node                           # altura não muda
        return self._balancear(node)              # rebalanceia na volta

    # ------------------------------------------------------------------ #
    #  Remoção                                                             #
    # ------------------------------------------------------------------ #

    def remover(self, nome):
        """Ponto de entrada público."""
        self.raiz = self._remover(self.raiz, nome)

    def _remover(self, node, nome):
        """Remove recursivamente e rebalanceia na volta (bottom-up).
        Mesma lógica da BST; ao retornar, passa por _balancear."""
        if node is None:
            return None
        if nome < node.nome:
            node.esq = self._remover(node.esq, nome)
        elif nome > node.nome:
            node.dir = self._remover(node.dir, nome)
        else:
            if node.esq is None:
                return node.dir
            if node.dir is None:
                return node.esq
            # 2 filhos: substitui pelo sucessor in-order
            sucessor = self._minimo(node.dir)
            node.nome = sucessor.nome
            node.telefone = sucessor.telefone
            node.dir = self._remover(node.dir, sucessor.nome)
        return self._balancear(node)              # rebalanceia na volta

    def _minimo(self, node):
        """Retorna ponteiro para o nó mínimo da subárvore (sem copiar dados)."""
        while node.esq is not None:
            node = node.esq
        return node

    # ------------------------------------------------------------------ #
    #  Busca                                                               #
    # ------------------------------------------------------------------ #

    def buscar(self, nome):
        """Retorna o ponteiro para o NodeAVL encontrado, ou None."""
        return self._buscar(self.raiz, nome)

    def _buscar(self, node, nome):
        """Busca binária recursiva idêntica à BST — AVL não muda a busca."""
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
        """Percurso in-order acumula pares (nome, telefone) na lista."""
        if node is None:
            return
        self._em_ordem(node.esq, resultado)
        resultado.append((node.nome, node.telefone))
        self._em_ordem(node.dir, resultado)