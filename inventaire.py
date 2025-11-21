class Inventory:

    def __init__(self, capacity=10):
        """
        Initialise un inventaire vide.
        Args:
            capacity (int): nombre maximum d'objets dans l'inventaire.
        """
        self.items = []
        self.capacity = capacity


    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"Vous avez ajouté '{item}' à votre inventaire.")
            return True
        else:
            print("Votre inventaire est plein | Impossible d'ajouter un objet.")
            return False
        
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print("Vous avez retiré '{item}' de votre inventaire.")
            return True
        else: 
            print("'{item} n'est pas dans votre inventaire")
            return False
    
    def list_items(self):
        """Affiche le contenu de l'inventaire"""
        if not self.items:
            print("Votre est inventaire est vide.")
        else:
            print("Inventaire :")
            for i, item in enumerate(self.items, start=1):
                print(f"{i}.{item}" )