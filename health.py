# health.py

class Health:
    def __init__(self, max_hp=100):
        """
        Initialise la santé du joueur.
        Args:
            max_hp (int): nombre de points de vie maximum.
        """
        self.max_hp = max_hp
        self.current_hp = max_hp

    def take_damage(self, amount):
        """
        Réduit les points de vie du joueur.
        """
        self.current_hp -= amount
        if self.current_hp < 0:
            self.current_hp = 0
        print(f"💥 Vous perdez {amount} points de vie. ({self.current_hp}/{self.max_hp})")

    def heal(self, amount):
        """
        Soigne le joueur.
        """
        self.current_hp += amount
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
        print(f"💖 Vous récupérez {amount} points de vie. ({self.current_hp}/{self.max_hp})")

    def is_dead(self):
        """
        Vérifie si le joueur est mort.
        """
        return self.current_hp <= 1

    def show_health(self):
        """
        Affiche les points de vie actuels.
        """
        print(f"❤️ Santé : {self.current_hp}/{self.max_hp}")


    
