class Noeud:

    def __init__(self, value):
        self.data = value
        self.next = None

    def __repr__(self):
        return f"Contenu du noeud : {self.data}"
    