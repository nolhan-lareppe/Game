# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from inventaire import Inventory
from health import Health
from quest import Quest


class Game:

    # Constructor
    def __init__(self):
        #self.player = Player(input("\nEntrez votre nom:"))
        
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.health = Health(100)
        
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go

        #Inventaire
        
        inventaire = Command("inventaire", ": afficher votre inventaire", Actions.show_inventory, 0)
        self.commands["inventaire"] = inventaire

        close_inv = Command("back", " : fermer l'inventaire et retourner dans la salle + permet de remettre les propositions de sorties", Actions.close_inventoty, 0)
        self.commands["back"] = close_inv

        #HEALTH

        health = Command("pv", " : affiche votre nombre de PV", Actions.show_health, 0)
        self.commands["health"] = health

        close_health = Command("back", " : ferme la jauge de PV", Actions.close_health,0)
        self.commands["back"] = close_health
        
        
        #Ecus

        gold = Command("ecus", " : afficher le nombre d'écus", Actions.show_gold, 0)
        self.commands["ecus"] = gold
        
        #Objets

        

        #Réponses
        
        yes = Command("Yes", " : répondre oui",Actions.Yes, 0)
        self.commands["Yes"] = yes
        no = Command("No", " : répondre non",Actions.No, 0)
        self.commands["No"] = no
        suite = Command("suite", " : passer à la suite", Actions.suite, 0)
        self.commands["suite"] = suite
        continuer = Command("continuer"," : avancer dans le village", Actions.continuer, 0)
        self.commands["continuer"] = continuer

        #Choix multiple de personnage

        #barman = Command("barman", " : aller voir le barman",Actions.barman, 0)
        #self.commands["barman"] = barman



        




        
        #fee = Command("fee" ," : aller voir la fée", Actions.fee, 0)
        #self.commands["fee"] = fee

        #viking = Command("viking" ," :  aller voir le viking",Actions.viking, 0)
        #self.commands["viking"] = viking
        

        gaspard = Command("gaspard", " : permet d'appeler Gaspard.", Actions.gaspard_action, 0)
        self.commands["gaspard"] = gaspard
        
        #LIEU
        
        #village = Command("village" ," : aller dans le village",Actions.village, 0)
        #self.commands["village"] = village

        #auberge = Command("auberge", " : aller à l'auberge du village.", Actions.auberge, 0)
        #self.commands["auberge"] = auberge

        #maison = Command("maison", " : aller à la maison hantée.", Actions.maison, 0)
        #self.commands["maison"] = maison
        

        #OBJETS

        give_key = Command("give", " : donne la clé du garde", Actions.give, 0)
        self.commands["give"] = give_key



        use_key = Command("utiliser_key", " : utiliser la clé.", Actions.use_key, 0)
        self.commands["utiliser_key"] = use_key
        
        #buy_potion = Command("buy", " : acheter une potion", Actions.buy, 0)
        #self.commands["buy"] =buy_potion

        #buy_verre = Command("buy" , " acheter une consommation", Actions.buy, 1)
        #self.commands["buy"] =buy_verre

        buy = Command("buy", " : acheter un objet", Actions.buy, 0)
        self.commands["buy"] =buy

 

        use_potion = Command("utiliser_potion", " : consommer une potion", Actions.use, 1)
        self.commands["use"] = use_potion

        #maison_hantee_cmd = Command("enter", " : entrer dans la maison hantee", Actions.enter_maison, 0)
        #self.commands["enter"] = maison_hantee_cmd

        enter = Command("enter", "entrer dans la maison", Actions.enter_maison, 0)
        self.commands["enter"] = enter

        lire = Command("lire"," lire le papier", Actions.lire, 0)
        self.commands["lire"] = lire


        retour_cmd = Command("retour", " : revenir dans la room précédente", Actions.retour, 0)
        self.commands["retour"] = retour_cmd

        look = Command("look", "regarde ce qu'il y'a dans l'environnement au autour de soi", Actions.look, 0)
        self.commands["look"] = look


        talk = Command("talk", "aller parler à un PNJ", Actions.talk, 0)
        self.commands["talk"] = talk


        pierre = Command("pierre", "choisir pierre", Actions.pierre, 0)
        self.commands["pierre"] = pierre

        papier = Command("papier", "choisir papier", Actions.papier, 0)
        self.commands["papier"] = papier

        ciseau = Command("ciseau", "choisir ciseau", Actions.ciseau, 0)
        self.commands["ciseau"] = ciseau

        attaquer = Command("attaquer", ": permet d'attaquer le boss", Actions.attack_boss, 0)
        self.commands["attaquer"] = attaquer
        
        esquiver = Command("esquiver", ": permet d'esquiver le boss",Actions.dodge_boss, 0)
        self.commands["esquiver"] = esquiver


        equip = Command("equiper", " : permet d'équiper une arme", Actions.equip_weapon, 1)
        self.commands["equiper"] = equip

        quests = Command("quests", " : fficher la listes des quêtes", Actions.quests, 0)
        self.commands["quests"] = quests

        quest = Command("quest", " : afficher les détails d'une quête", Actions.quest, 1)
        self.commands["quest"] = quest

        activate = Command("activate", " : activer une quête", Actions.activate, 1)
        self.commands["activate"] = activate

        
  





        
        # Setup rooms

        """forest = Room("Forest", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(forest)
        tower = Room("Tower", "dans une immense tour en pierre qui s'élève au dessus des nuages.")
        self.rooms.append(tower)
        cave = Room("Cave", "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
        self.rooms.append(cave)
        cottage = Room("Cottage", "dans un petit chalet pittoresque avec un toit de chaume. Une épaisse fumée verte sort de la cheminée.")
        self.rooms.append(cottage)
        swamp = Room("Swamp", "dans un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
        self.rooms.append(swamp)
        castle = Room("Castle", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(castle)"""



        #Room de mon jeu

        entree_village = Room("entree_village", "Vous arrivez à l'entrée d'un village et un garde est entrain de dormir.\n Voulez-vous lui parler ou passer discrètement à côté de lui ?")
        self.rooms.append(entree_village)



        garde_talk = Room("garde_talk", "Il vous donne des informations à propos de la vie au village. Et vous donnes une clé secrète.")
        self.rooms.append(garde_talk)

        garde_talk.has_given_key = False
        garde_talk.on_enter = Actions.auto_give_guard_key

        garde_dodge = Room("garde_dodge", "Vous entrez dans le village discrètement.")
        self.rooms.append(garde_dodge)


        village_center = Room("village_center", "Vous êtes maintenant dans le village et apercevez une auberge au loin.\n Y aller ?" )
        self.rooms.append(village_center)
        #fin entrée du village

        #Début auberge

        auberge = Room("auberge", "Vous rentrez dans l'auberge et trois personnes sont dedans un barman, une fée et un viking")
        self.rooms.append(auberge)
        auberge.on_enter = lambda game: game.player.quest_manager.check_room_objectives("auberge")


        barman = Room("barman", "Barman : Désirez-vous prendre un verre ?")
        self.rooms.append(barman)
        verre = Room("verre", "Le barman vous offre un verre pour seulement 5 écu")
        self.rooms.append(verre)


        #barman_room = Room("barman_room", "Vous vous approchez du barman derrière son comptoir.")
        #barman_room.on_enter = Actions.barman
        #self.rooms.append(barman_room)

        
        fee = Room("fee", "Vous donne une potion magique dont vous ne connaissez pas les effets.")        
        self.rooms.append(fee)
        
        potion = Room("potion", "Fee : La potion n'est pas gratuite, si tu la veux donne moi 20 écu.\nPrendre la potion ?")
        self.rooms.append(potion)

        viking = Room("viking", "Le viking étant bourré il se bat contre et vous perdez 10 PV")
        self.rooms.append(viking)

        #Fin auberge

        #Retour au village
        village = Room("village", "Vous êtes de retour sur la place du village")
        self.rooms.append(village)

        #suite auberge x not auberge

        enfant = Room("enfant", "Un enfant se balade dans le village et a peur de vous.\n Lui parler ?")
        self.rooms.append(enfant)

        enfant_talk = Room("enfant_talk", "L'enfant n'ose pas vous parler.\n Essayer quand même de lui parler ?")
        self.rooms.append(enfant_talk) #faire un for avec i = 3/5 pour cacher un secret sur le village

        enfant_secret = Room("enfant_secret", "L'enfant a pris confiance en vous et vous dévoile le secret du village. " )
        self.rooms.append(enfant_secret)

        #FIN ENFANT_SECREt

        #RETOUR AU VILLAGE PARTIE 2

        village2 = Room("village2", "Vous arrivez à la deuxième partie du village.")
        self.rooms.append(village2)

        village3 = Room("village3", "Vous décidez d'avancé dans le village.")
        self.rooms.append(village3)
        


        maison = Room("maison", "Une maison qui semble avoir une malédiction.")
        self.rooms.append(maison)
        #maison.on_enter = lambda game: game.player.quest_manager.check_room_objectives("maison")


        enter_maison = Room("enter maison", "Vous rentrez dans la maison hantée et vous entendez une sorte de voix.")#Si et seulement si possède la Clé du garde
        self.rooms.append(enter_maison)
        enter_maison.on_enter = lambda game: game.player.quest_manager.check_room_objectives("maison")



        gaspard_room = Room("Gaspard", "Vous rencontrez Gaspard, un petit garçon mystérieux. Il semble prêt à vous confier un objet secret.")
        self.rooms.append(gaspard_room)
        gaspard_room.on_enter = lambda game: game.player.quest_manager.check_room_objectives_by_title("Découvreur de Secrets", "Visiter maison")



        forge_room = Room("Forge", "Vous entrez dans la forge")
        self.rooms.append(forge_room)
        forge_room.on_enter = lambda game: game.player.quest_manager.check_room_objectives("forge")




        forgeron = Room("Forgeron", "Vous demandez des renseignements auprès du forgeron.\n Le forgeron vous propose plusieurs armes :\n- Dague : 10 dégâts — 15 écus\n- Épée : 20 dégâts — 30 écus\n- Marteau : 35 dégâts — 60 écus")
        self.rooms.append(forgeron)



        #Auberge

        barman_room = Room("barman_room", " Barman  ")
        barman_room.on_enter = Actions.barman
        self.rooms.append(barman_room)

        fee_room = Room("fee_room", "Fée")
        fee_room.on_enter = Actions.fee
        self.rooms.append(fee_room)

        viking_room = Room("viking_room", "Viking")
        viking_room.on_enter = Actions.viking
        self.rooms.append(viking_room)

        milo_room = self.find_room("village")
        if not hasattr(milo_room, "npcs"):
            milo_room.npcs = {}
        milo_room.npcs["milo"] = Actions.milo

        fin_village = Room("fin_village", "Vous arrivez à la fin du village ...")
        fin_village.on_enter = Actions.milo_rumeur_boss
        self.rooms.append(fin_village)


        boss_room = Room("boss_final", "Vous entrez dans la caverne du boss final, l'air est changé de tension...")
        boss_room.on_enter = Actions.boss_final
        self.rooms.append(boss_room)

        fin_village.exits["boss"] = boss_room

        

        

        


        






        # Create exits for rooms

        """forest.exits = {"N" : cave, "E" : tower, "S" : castle, "O" : None}
        tower.exits = {"N" : cottage, "E" : None, "S" : swamp, "O" : forest}
        cave.exits = {"N" : None, "E" : cottage, "S" : forest, "O" : None}
        cottage.exits = {"N" : None, "E" : None, "S" : tower, "O" : cave}
        swamp.exits = {"N" : tower, "E" : None, "S" : None, "O" : castle}
        castle.exits = {"N" : forest, "E" : swamp, "S" : None, "O" : None}"""


        #Exists mes rooms

        #Début de l'histoire
        entree_village.exits = { "village" : village_center}
        entree_village.npcs = {"garde" : Actions.garde}

        #garde_talk.exits = { "suite" : village_center}
        #garde_talk.npcs = {"garde" : Actions.garde}
        
        garde_dodge.exits = { "suite" : village_center}
        
        village_center.exits = {"auberge" : auberge, "village":village3}
        
        village_center = self.find_room("village_center")
        
        if not hasattr(village_center, "npcs"):
            village_center.npcs = {}

        village_center.npcs["milo"] = Actions.milo

        
        

        


    
        
        

        auberge.exits = {"village": village}
        auberge.npcs = {"barman" : Actions.barman, "fee" : Actions.fee, "viking" : Actions.viking}
        
        #barman.on_enter = Actions.barman
        #barman.exits = {"Yes": verre, "No" : auberge} #en retirant barman du dico d'auberge

        
        
        verre.exits = {"suite" : auberge}
        

        fee.exits = {"Yes" : potion, "No" : auberge} #en retirant fee du dico d'auberge
        potion.exits = {"Yes": auberge, "No" : auberge} #en retirant le nb écu si yes de l'inventaire 

        viking.exits = {"suite" : auberge}

        #Fin auberge
        
        village.exits = { "auberge" : auberge, "continuer" : enfant}
        

        #Suite auberge

        village3.exits = {"continuer" : enfant}
        
        continuer_exits = {"continuer" : enfant, "auberge" : auberge} #en retirant les personnes déjà vu
        
        enfant.exits = {"Yes" : enfant_talk, "No" : village2} #faire un for pour persister et obtenir des infos

        enfant_talk.exits = {"Yes" : enfant_secret, "No" : village2}

        enfant_secret.exits = {"village" : village2}

        #FIN ENFANT

        #DEBUT PARTIE 2 DU VILLAGE

        village2.exits = {"maison": maison, "forge" : forge_room, "fin" : fin_village}

        
        
        maison = self.find_room("maison")
        enter_maison = self.find_room("enter maison")
        gaspard_room = self.find_room("Gaspard")
        gaspard_secret = self.find_room("gaspard_secret")

        village2 = self.find_room("village2")
        
        
        maison.exits = {"enter" : self.find_room("maison"), "village" : village2}
        enter_maison.exits = {"Gaspard" : self.find_room("gaspard_room"), "village" : village2}
        

        gaspard_room.exits= {"Gaspard" : self.find_room("gaspard"), "village":village2}


        #Forge

        forge_room.exits = {"village" : village2}
        forge_room.npcs = {"forgeron" : Actions.forgeron}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = entree_village
        self._setup_quests()

        







#QUETES

    def _setup_quests(self):
        """Initialize all quests."""
        exploration_quest = Quest(
            title="Grand Explorateur",
            description="Explorez tous les lieux dans ce village.",
            objectives=["Visiter auberge"
                        , "Visiter forge"],
            reward="Titre de Grand Explorateur"
        )

        discovery_quest = Quest(
            title="Découvreur de Secrets",
            description="Découvrez le secret de la maison hantée.",
            objectives=["Visiter maison", "Découvrir le secret de cette maison"],
            reward="Lame Spectrale"
        )

        boss_quest = Quest(
            title = "Boss final", 
            description="Vaincre le boss dans sa caverne.",
            objectives=["Vaincre le boss final"],
            reward="Titre du Grand Héros du Village"
        )

        # Add quests to player's quest manager
        self.player.quest_manager.add_quest(exploration_quest)
        #self.player.quest_manager.add_quest(travel_quest)
        self.player.quest_manager.add_quest(discovery_quest)
        self.player.quest_manager.add_quest(boss_quest)


        
    














        

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]

        


        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

   
   
   
    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

    def find_room(self, name):
        for room in self.rooms:
            if room.name == name:
                return room
        return None

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
