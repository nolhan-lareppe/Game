#Importation
from inventaire import Inventory
from health import Health
from weapon import Weapon



# Define the Player class.


class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory() #inventaire vide 
        self.health = Health(100) #Le joueur commence avec 100PV
        self.visited_npcs = set() # Les PNJ que le joueur à rencontrer
        self.gold = 50 #💰 Le joueur commence avec 50 écus

        self.child_talk_count = 0 #initialisation du compteur de fois pour parler à l'enfant
        self.current_room = None
        self.previous_rooms = []

        self.milo_state = "absent"

        self.in_boss_fight = False
        self.last_action = None # garde la dernière action du joueur pour le tour par tour
        
        self.weapon = None
    # Define the move method.


    def move(self, direction, game=None):
        # Get the next room from the exits dictionary of the current room.
        
        if direction not in self.current_room.exits:
            #if direction not in self.current_room.exits:
                print("Aucune porte dans cette direction !")
                return False

        
        
        
        # Déplacement
        self.current_room = self.current_room.exits[direction]
        

        # Appelle on_enter si défini
        if hasattr(self.current_room, "on_enter") and callable(self.current_room.on_enter) and game:
            self.current_room.on_enter(game)

        # Affiche la description de la salle
        print(self.current_room.get_long_description())
        return True
    

    def equip_weapon(self, weapon):
         self.weapon = weapon
         print(f"🗡️ Vous équipez : {weapon.name}")
         
    
            
        
        
        
        
        
        #if direction in self.current_room.exits:
         #   print("\nAucune porte dans cette direction !\n")
         #   #next_room = self.current_room.exits[direction]
         #   return False
        #
        #next_room = self.current_room.exits[direction]
        #self.current_room = next_room

        #if hasattr(next_room, "on_enter") and callable(next_room.on_enter):
        #    next_room.on_enter(self.game)

        #print(self.current_room.get_long_description())
        #return True











        #if hasattr(self.current_room, "on_enter") and self.current_room.on_enter:
        #    self.current_room.on_enter(game)

        # If the next room is None, print an error message and return False.
        #if next_room is None:
            #print("\nAucune porte dans cette direction !\n")
            #return False
        
        #next_room 
        
        # Set the current room to the next room.
        #self.current_room = next_room
        #print(self.current_room.get_long_description())
        #return True

    