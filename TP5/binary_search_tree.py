# printTree and display_aux are from : https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python

def printTree(T):
        if not T.root:
            print("")
            return
         
        lines, *_ = display_aux(T.root)
        s = ""
        for line in lines:
            s += line + "\n"
        print(s)
    
def display_aux(N):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if N.right is None and N.left is None:
        line = '%s' % N
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if N.right is None:
        lines, n, p, x = display_aux(N.left)
        s = '%s' % N
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if N.left is None:
        lines, n, p, x = display_aux(N.right)
        s = '%s' % N
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = display_aux(N.left)
    right, m, q, y = display_aux(N.right)
    s = '%s' % N
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


def insert_compare_and_swap(node, newNode, newValue):
    if (newValue < node.value):
        if (node.left == None):
            node.left = newNode
        else:
            insert_compare_and_swap(node.left, newNode, newValue)
    else:
        if (node.right == None):
            node.right = newNode
        else:
            insert_compare_and_swap(node.right, newNode, newValue)

def search_in_tree(node, value):
        if not node:
            return False
        elif (node.value == value):
            return node
        elif (value < node.value):
            return search_in_tree(node.left, value)
        elif (value > node.value):
            return search_in_tree(node.right, value)

def get_the_leftmost(node):
    while node.left:
        node = node.left
    return node

def delete_recursive(node, value):
    if node is None:
        return None 
    
    if value < node.value:
        node.left = delete_recursive(node.left, value)
    elif value > node.value:
        node.right = delete_recursive(node.right, value)
    else:
        node = delete_from_tree(node)
    
    return node

def delete_from_tree(node):
    if (node.left == None and node.right == None):
        return None
    elif ((node.left == None and node.right != None) or (node.right == None and node.left != None)):
        if (node.left != None):
            return node.left
        else:
            return node.right
    else:
        successor = get_the_leftmost(node.right)
        node.value = successor.value
        node.right = delete_recursive(node.right, successor.value)
        return node
            

class Noeud:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return f"{self.value}"

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Noeud(value)
        if not self.root:
            self.root = newNode
        else:
            insert_compare_and_swap(self.root, newNode, value)
        
    def search(self, value):
        return search_in_tree(self.root, value)
    
    def delete(self, value):
        self.root = delete_recursive(self.root, value)

    


newTree = BinarySearchTree()
newTree.insert(25)
newTree.insert(60)
newTree.insert(35)
newTree.insert(10)
newTree.insert(5)
newTree.insert(20)
newTree.insert(65)
newTree.insert(45)
newTree.insert(70)
newTree.insert(40)
newTree.insert(50)
newTree.insert(55)
newTree.insert(30)
newTree.insert(15)
printTree(newTree)
newTree.delete(35)
printTree(newTree)
newTree.delete(25)
printTree(newTree)