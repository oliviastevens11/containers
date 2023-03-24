'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than
the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__(xs)
        self.height = []

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that
        all nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if node is None:
            return True
        bfactor = AVLTree._balance_factor(node)
        if bfactor not in [-1, 0, 1]:
            return False

        r_satisfied = AVLTree._is_avl_satisfied(node.right)
        l_satisfied = AVLTree._is_avl_satisfied(node.left)

        return r_satisfied and l_satisfied

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code
        is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node is None or node.right is None:
            return node

        new_root = Node(node.right.value)
        new_root.right = node.right.right
        newleft = Node(node.value)
        newleft.left = node.left
        newleft.right = node.right.left
        new_root.left = newleft
        return new_root

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function. Similar pattern to book, but dont
        have parent function and dont want to modify original tree

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree
        code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node is None or node.left is None:
            return node

        new_root = Node(node.left.value)
        new_root.left = node.left.left
        newright = Node(node.value)
        newright.right = node.right
        newright.left = node.left.right
        new_root.right = newright

        return new_root

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of
        how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code
        is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for
        your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        Lecture code:
        First do BST insert
        For each ancestor of the inserted node,
        if balance factor is either -2 or 2, then call rebalance
        may need to rebalance many times
        different for root vs. child
        '''
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = AVLTree._insert(self.root, value)

    @staticmethod
    def _insert(node, value):
        if node is None:
            return None
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                node.left = AVLTree._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                node.right = AVLTree._insert(node.right, value)

        AVLTree._rebalance(node)
        bfactor = AVLTree._balance_factor(node)
        if bfactor > 1 and value < node.left.value:
            return AVLTree._right_rotate(node)
        if bfactor < -1 and value > node.right.value:
            return AVLTree._left_rotate(node)
        if bfactor > 1 and value > node.left.value:
            node.left = AVLTree._left_rotate(node.left)
            return AVLTree._right_rotate(node)
        if bfactor < -1 and value < node.right.value:
            node.right = AVLTree._right_rotate(node.right)
            return AVLTree._left_rotate(node)
        return node

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if AVLTree._balance_factor(node) < 0:
            if AVLTree._balance_factor(node.right) > 0:
                AVLTree._right_rotate(node.right)
                AVLTree._left_rotate(node)
            else:
                AVLTree._left_rotate(node.left)
        elif AVLTree._balance_factor(node) > 0:
            if AVLTree._balance_factor(node.left) < 0:
                AVLTree._left_rotate(node.left)
                AVLTree._right_rotate(node)
            else:
                AVLTree._right_rotate(node)
