import Noeud

class ListeChainee:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        s = ""
        currentNode = self.head
            
        while currentNode:
            s += str(currentNode.data) + "->"
            currentNode = currentNode.next

        return s

    def ajouter(self, value):
        newNode = Noeud.Noeud(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def inserer(self, value, k):
        newNode = Noeud.Noeud(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        elif k == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            currentNode = self.head
            count = 0

            for i in range (k-1):
                currentNode = currentNode.next
            
            newNode.next = currentNode.next
            currentNode.next = newNode

liste = ListeChainee()
liste.ajouter("32")
liste.ajouter("45")
liste.ajouter("167")
liste.inserer("33", 1)
liste.inserer("666", 2)

print(liste)