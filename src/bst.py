"""Implementation of a Binary Search Tree."""

from my_queue import Queue
from stack import Stack


class Node(object):
    """Node class."""

    def __init__(self, val):
        """Node instantiation."""
        self.val = val
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree(object):
    """Binary Search Tree Class."""

    def __init__(self):
        """Binary Search Tree instantiation."""
        self.root = None
        self._size = 0

    def insert(self, val):
        """Insert value into Binary Search Tree."""
        if not self.root:
            self.root = Node(val)
        else:
            self._insert_node(val, self.root)
        self._size += 1

    def _insert_node(self, val, node):
        """Insert a node when not at the root."""
        if val < node.val:
            if node.leftChild:
                self._insert_node(val, node.leftChild)
            else:
                node.leftChild = Node(val)
        else:
            if node.rightChild:
                self._insert_node(val, node.rightChild)
            else:
                node.rightChild = Node(val)

    def depth(self):
        """Call helper depth method."""
        return self._depth_node(self.root) - 1

    def _depth_node(self, root, depth=0):
        """Depth method the takes in root node."""
        if root is None:
            return depth
        return max(self._depth_node(root.leftChild, depth + 1),
                   self._depth_node(root.rightChild, depth + 1))

    def contains(self, val):
        """Return True if val is in the BST, False if not."""
        return self.search(val) is not None

    def balance(self):
        """Return 1, 0 or -1 that represents how well balanced the tree is."""
        if self.root is None:
            return 0
        return self._depth_node(self.root.leftChild) - self._depth_node(self.root.rightChild)

    def size(self):
        """Return size of bst."""
        return self._size

    def search(self, val):
        """Search if node exist in tree and return if present, otherwise None."""
        curr_node = self.root
        while curr_node:
            if curr_node.val == val:
                return curr_node
            elif val > curr_node.val:
                curr_node = curr_node.rightChild
            else:
                curr_node = curr_node.leftChild
        return None

    def breadthfirst(self):
        """Breadth First Traversal for Binary Search Tree."""
        q = Queue()
        q.enqueue(self.root)
        while q.size():
            node = q.dequeue()
            yield node.val
            if node.leftChild is not None:
                q.enqueue(node.leftChild)
            if node.rightChild is not None:
                q.enqueue(node.rightChild)

    def preorder(self):
        """Preorder generator."""
        node = self.root
        if node is None:
            return
        s = Stack()
        s.push(node)
        while s.size():
            node = s.pop()
            yield node.val
            if node.rightChild is not None:
                s.push(node.rightChild)
            if node.leftChild is not None:
                s.push(node.leftChild)

    def postorder(self):
        """Postorder generator."""
        node = self.root
        s = []
        last_visited = None
        while s or node is not None:
            if node is not None:
                s.append(node)
                node = node.leftChild
            else:
                peek_node = s[-1]
                if peek_node.rightChild is not None and last_visited is not peek_node.rightChild:
                    node = peek_node.rightChild
                else:
                    yield peek_node.val
                    last_visited = s.pop()

    def inorder(self):
        """In order generator."""
        node = self.root
        s = Stack()
        while s.size() or node is not None:
            if node is not None:
                s.push(node)
                node = node.leftChild
            else:
                node = s.pop()
                yield node.val
                node = node.rightChild

   # Delete Node

    def delete(self, val):
        """Delete a node."""
        if self.root is None:
            return None
        elif self.root.val == val:
            if self.root.leftChild is None and self.root.rightChild is None:
                self.root = None==
            elif self.root.leftChild and self.root.rightChild is None:
                self.root = self.root.leftChild
            elif self.root.rightChild and self.root.rightChild is None:
                self.root = self.root.rightChild
            else:
                del_node_parent = self.root
                del_node = self.root.rightChild
                while del_node.leftChild:
                    del_node_parent = del_node
                    del_node = del_node.leftChild

                self.root.val = del_node.val
                if del_node.rightChild:
                    if del_node_parent.val > del_node.val:
                        del_node_parent.leftChild = del_node.rightChild
                    elif del_node_parent.val < del_node.val:
                        del_node_parent.rightChild = del_node.rightChild
                else:
                    if del_node.val < del_node_parent.val:
                        del_node_parent.leftChild = None
                    else:
                        del_node_parent.rightChild = None

            return True

        parent = None
        node = self.root

        while node and node.val != val:
            parent = node
            if val < node.val:
                node = node.leftChild
            elif val > node.val:
                node = node.rightChild

        # if node not found in tree
        if node is None:
            return None

        # if node to delete has no children
        elif node.leftChild is None and node.rightChild is None:
            if val < parent.val:
                parent.leftChild = None
            else:
                parent.rightChild = None
            return

        # node to delete has only a left child
        elif node.leftChild and node.rightChild is None:
            if val < parent.val:
                parent.leftChild = node.leftChild
            else:
                parent.rightChild = node.leftChild
            return

        # node to delete has only a right child
        elif node.rightchild and node.leftChild is None:
            if val < parent.val:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild
            return

        # node to delete has both left and right children
        else:
            if self._depth_node(node.leftChild) < self._depth_node(node.rightChild):
                curr = node.rightChild
                innermost_direction = 'leftChild'
                outer_direction = 'rightChild'
            else:
                curr = node.leftChild
                innermost_direction = 'rightChild'
                outer_direction = 'leftChild'
            parent = curr
            while curr:
                if parent == curr:
                    replacement_node = curr
                    curr = getattr(curr, innermost_direction)
                    continue
                replacement_node = curr
                curr = getattr(curr, innermost_direction)
                if curr:
                    parent = getattr(parent, innermost_direction)

            node.val = replacement_node.val
            setattr(parent, innermost_direction, getattr(replacement_node, outer_direction))

    # Rotations

    def right_rotation(self, subtree_root):
        """Right rotation given root and pivot nodes."""
        parent = subtree_root
        pivot = parent.left
        grandparent.rightChild = parent

        """Given root and pivot nodes, complete a right rotation."""
        pivot = subtree_root.left
        if subtree_root is self.root:
            self.root = pivot
        pivot.parent = sub_root.parent
        subtree_root.left = None
        if pivot.right:
            pivot.right.parent = subtree_root
            subtree_root.left = pivot.right
        pivot.right = subtree_root
        subtree_root.parent = pivot

    def left_rotation(self, subtree_root):
        """Left rotation given root and pivot nodes."""
        pivot = subtree_root.right
        if subtree_root is self.root:
            self.root = pivot
        pivot.parent = subtree_root.parent
        subtree_root.right = None
        if pivot.left:
            pivot.left.parent = subtree_root
            subtree_root.right = pivot.left
        pivot.left = subtree_root
        subtree_root.parent = pivot

    def tree_balance(self, node):
        """Check tree balance."""
        while node:
            tree_bal = self.balance(node)
            if abs(tree_bal) > 1:
                self.balance_tree(node, tree_bal)
            node = node.parent

    def balance_tree(self, start_node, bal):
        """Balance the subtree."""
        balance_lst_left = []
        balance_lst_right = []
        curr = self.root

        if tree_bal > 0:
            while curr:
                if _insert_node.val > curr.val:
                    curr = curr.right
                    balance_lst_right.append(curr)
                else:
                    curr = curr.left
                    balance_lst_left.append(curr)

            while balance_lst_left.size():
                node = balance_lst_left.pop()
            return balance_lst_left.size()

            while balance_lst_right.size():
                node = balance_lst_right.pop()
            return balance_lst_right.size()

            tree_balance = abs(balance_lst_left.size() - balance_lst_right.size())
            if tree_balance > 1:
                right_rotation()




        if bal > 0:                             # < --- Heavy on the left.
            subtree_bal = self.balance(start_node.left)
            if subtree_bal < 0:                     # < --- Sub, right heavy
                self._rotate_left(start_node.left)
            self._rotate_right(start_node)
        else:                                   # < --- Heavy on the right.
            subtree_bal = self.find_balance(start_node.right)
            if subtree_bal > 0:                     # < --- Sub, left heavy
                self._rotate_right(start_node.right)
            self._rotate_left(start_node)
