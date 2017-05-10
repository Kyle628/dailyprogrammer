class node:
    def __init__(self, key, value, left, right, parent=None):
        self.key = key
        self.value = value
        self.left=left
        self.right = right
        self.parent = parent

class bst:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if (self.root == None):
            self.root = node(key, value, None, None)
        else:
            self._insert(key, value, self.root)

    def _insert(self, key, value, curr_node):
        if (key < curr_node.key):
            if curr_node.left:
                self._insert(key, value, curr_node.left)
            else:
                curr_node.left = node(key, value, None, None, curr_node)
        else:
            if curr_node.right:
                self._insert(key, value, curr_node.right)
            else:
                curr_node.right = node(key, value, None, None, curr_node)

    def preorder(self, curr_node):
        print(curr_node.key)
        if curr_node.left:
            self.preorder(curr_node.left)
        if curr_node.right:
            self.preorder(curr_node.right)

    def inorder(self, curr_node):
        if curr_node.left:
            self.preorder(curr_node.left)
        print(curr_node.key)
        if curr_node.right:
            self.preorder(curr_node.right)

    def postorder(self, curr_node):
        if curr_node.left:
            self.preorder(curr_node.left)
        if curr_node.right:
            self.preorder(curr_node.right)
        print(curr_node.key)

    '''def delete(self, key):
        if (self.root == None):
            return
        else:
            self._delete(key, self.root)

    def _delete(self, key, curr_node):
        if (key == curr_node.key):
            if (curr_node.parent.key > key):
                curr_node.parent.left = None
            else:
                curr_node.parent.right = None
            return
        elif (curr_node.left == None and curr_node.right == None):
            return
        if (key < curr_node.key):
            self._delete(key, curr_node.left)
        else:
            self._delete(key, curr_node.right)'''






my_tree = bst()
my_tree.insert("oconnor", "kyle")
my_tree.insert("banana", "caroline")
my_tree.insert("apple", "nom")
my_tree.insert("carrot", "root")
my_tree.preorder(my_tree.root)
