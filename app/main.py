from bst import BST
from avl import AVL
from interface import menu

if __name__ == "__main__":
    bst = BST()
    avl = AVL()
    menu(bst, avl, BST, AVL)  # passa as classes também para o benchmark poder criar instâncias limpas
