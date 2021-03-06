# Binary Node implementation

class BinaryNode:
    def __init__(self, value = None):
        # create a binary node
        self.value = value
        self.left = None
        self.right = None
        
    def add(self, val):
        # Adds a new node to the tree containing this value
        if val <= self.value:
            if self.left:
                self.left.add(val)
            else:
                self.left = BinaryNode(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = BinaryNode(val)
                
    def delete(self):
        # Remove value of self from BinaryTree. Works in conjunction with remove method in BinaryTree
        
        # check if node is a leaf
        if self.left == self.right == None:
            return None
        if self.left == None:
            return self.right
        if self.right == None:
            return self.left
        
        # finding the max value in the left branch by always searching for grandchild on the right
        child = self.left
        grandchild = child.right
        if grandchild:
            while grandchild.right:
                child = grandchild
                grandchild = child.right
            self.value = grandchild.value
            child.right = grandchild.left
        else:
            self.left = child.left
            self.value = child.value
            
        return self
    
    
    def inorder(self):
        # In order traversal of tree rooted at given node.
        if self.left:
            for n in self.left.inorder():
                yield n
                
        yield self.value
        
        if self.right:
            for n in self.right.inorder():
                yield n
                
                
# Binary Search Tree implementation

class BinaryTree:
    def __init__(self):
        # Create empty binary tree
        self.root = None
        
    def add(self, value):
        # Insert value into proper location in Binary Tree
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)
            
    def contains(self, target):
        # Check whether BST contains target value
        node = self.root
        while node:
            if target == node.value:
                return True
            if target < node.value:
                node = node.left
            else:
                node = node.right
        return False
    
    def remove(self, value):
        # remove value from tree
        
        if self.root:
            self.root = self.removeFromParent(self.root, value)
            
    def removeFromParent(self, parent, value):
        # remove value from tree rooted at parent
        if parent is None:
            return None
        
        if value == parent.value:
            return parent.delete()
        elif value < parent.val:
            parent.left = self.removeFromParent(parent.left, value)
        else:
            parent.right = self.removeFromParent(parent.right, value)
            
        return
    
    def __iter__(self):
        # In order traversal of elements in the tree
        if self.root:
            return self.root.inorder()
    
import random    
def performance2():
    n = 1024
    while n <= 65536:
        bt = BinaryTree()
        for i in list(range(n)):
            bt.add(random.randint(1, n))
            
        now = time()
        bt.contains(random.randint(1, n))
        print(n, (time()-now)*1000)
        
        n *= 2
    