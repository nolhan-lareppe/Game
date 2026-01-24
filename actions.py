# Description: The actions module.
import random

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"



class Actions:

    #INVENTAIRE

    def show_inventory(game, list_of_words, number_of_parameters):
        
        player = game.player
        player.viewing_inventory = True
        game.player.inventory.list_items()
        
        return True
    
    def close_inventoty(game, list_of_words, number_of_parameters):
        """Fermer l'inventaire du player"""
        
        player = game.player
        print("\nVous quittez l'inventaire et retournez dans la salle :")
        print(player.current_room.get_long_description())
        return True

    
    #HEALTH


    def show_health(game, list_of_words, number_of_parameters):
        """Montre le nombre de PV"""
        player = game.player
        player.viewing_inventory = True
        game.player.health.show_health()
        return True 
    
    def close_health(game, list_of_words, number_of_parameters):

        player = game.player
        #print("\nVous quittez la jauge de vie et retournez en jeu :")
        print(player.current_room.get_long_description())
        return True

    #ECUS


    def show_gold(game, list_of_words, number_of_parameters):
        player = game.player
        print(f"\n💰 Tu possèdes actuellement {player.gold} écus.")
        return True

    
    
    
    
    
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player

        l = len(list_of_words)

        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            #command_word = list_of_words[0]
            print(MSG1.format(command_word=list_of_words[0]))
            return False

        target = list_of_words[1]
        current_room = player.current_room

        if target in player.current_room.exits:
            next_room = current_room.exits[target]

            # Passer game et valeurs par défaut pour que ça fonctionne
            if hasattr(player, "previous_rooms"):
                player.previous_rooms.append(current_room)
            else:
                player.previous_rooms = [current_room]

            player.current_room = next_room

            



            if hasattr(next_room, "on_enter") and callable(next_room.on_enter):
                next_room.on_enter(game)

            if player.milo_state == "suiveur":
                print("👣 Milo vous suit en regardant derrière lui.")


            print(next_room.get_long_description())
            return True


           


            
        
        
        
             
        
        

        print("Aucune porte ni action dans cette direction !", target)
        return False   

        
    
        

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    
    
    #Définition de Yes and No
    
    def Yes(game, list_of_words, number_of_parameters):
        """
        Passe à la salle liée à 'Yes' depuis la salle actuelle.
        """
        player = game.player
        current_room = player.current_room

        # Vérifie que la salle a une sortie 'Yes'
        

        
        #MILO
        
        
        if hasattr(player, "waiting_milo_choice") and player.waiting_milo_choice:
            print("\n🙂 Milo soupire de soulagement.")
            print("« M-merci… je ferai de mon mieux pour t’aider. »")

            player.milo_state = "suiveur"
            player.waiting_milo_choice = False
            return True
        
        
        
        
        
        if current_room.name == "enfant_talk":
            
            player.child_talk_count += 1

            
            
            if player.child_talk_count < 2:
                print("\nL'enfant recule encore... Il a peur de vous.")
                print("Essayer encore ? (Yes / No)")
                return True
            
            
                
            next_room = game.find_room("enfant_secret")
            player.current_room = next_room

            papier_name = {"name": "papier","description": "Un petit papier froissé où l’enfant a écrit dessus : HoooOOOoooOOO… Gaspard HoooOOOoooOOO…."}
            
            player.inventory.add_item(papier_name)


            print("\n✨ L'enfant prend confiance en vous...")
            print("\nIl vous donne un secret papier. ")
            print(next_room.get_long_description())
            return True

                
            
            
    
        if "Yes" not in current_room.exits:
            print("\nIl n'y a rien qui réponde à 'Yes' ici.") 
            return False

        next_room = current_room.exits["Yes"]
        player.current_room = next_room

        if hasattr(next_room, "on_enter") and callable(next_room.on_enter):
            next_room.on_enter(game)

        
        

        print("\n" + next_room.get_long_description())
        return True
    
        

        

            


    def No(game, list_of_words, number_of_parameters):
        """
        Passe à la salle liée à 'No' depuis la salle actuelle.
        """
        player = game.player
        current_room = player.current_room

        if hasattr(player, "waiting_milo_choice") and player.waiting_milo_choice:
            print("\n😢 Milo baisse la tête.")
            print("« D-d’accord… je vais me cacher alors… »")

            player.milo_state = "absent"
            player.waiting_milo_choice = False
            return True
        
        
        if "No" in current_room.exits:
            next_room = current_room.exits["No"]
            player.current_room = next_room
            print("\n" + next_room.get_long_description())
            return True

        
        
        
        
        print("\nIl n'y a rien qui réponde à 'No' ici.")
        return False
        

        

        
        

    def suite(game, list_of_words, number_of_parameters):
        """
        Passe à la salle liée à 'suite' depuis la salle actuelle.
        """
        player = game.player
        current_room = player.current_room

        if "suite" in current_room.exits:
            next_room = current_room.exits["suite"]
            player.current_room = next_room
            print("\n" + next_room.get_long_description())
            return True
        else:
            print("\nIl n'y a rien qui réponde à 'suite' ici.")
            return False
        
    
    def continuer(game, list_of_words, number_of_parameters):
        """
        Passe à la salle liée à 'suite' depuis la salle actuelle.
        """
        player = game.player
        current_room = player.current_room

        if "continuer" in current_room.exits:
            next_room = current_room.exits["continuer"]
            player.current_room = next_room
            print("\n" + next_room.get_long_description())
            return True
        else:
            print("\nIl n'y a rien qui réponde à 'continuer 'continuer' ici.")
            return False
        



        

    #Personnage
    def garde(game, list_of_words, number_of_parameters):
        
        player = game.player
        current_room = player.current_room

        if not hasattr(player, "visited_npcs"): 
        #and "Yes" in player.visited_npcs:
            player.visited_npcs = set()
            
        if "garde_talk" in player.visited_npcs:
            print("Le garde retourne à son poste et ne veut plus vous parler.")
            #del current_room.exits["garde_talk"]
            return False
        
    
        print("Le garde peut vous donner une clé.")
        print("Tape 'give' pour l’obtenir ou 'No' pour partir.")
        
        if "garde_talk" in player.visited_npcs:
            print("Le garde retourne à son poste et ne veut plus vous parler.")
            del current_room.exits["garde_talk"]  # On retire l’action 'garde'
            return False

        


        # Marque que le garde a été rencontré
        if not hasattr(player, "visited_npcs"):
            player.visited_npcs = set()

            # Marque que le garde a été rencontré
            player.visited_npcs.add("garde_talk")

        # Le garde a une clé DISPONIBLE
        current_room.has_key = True

        return True
    
    


    def give(game, list_of_words, number_of_parameters):
        """Donne la clé du joueur et l'ajoute dans son inventaire"""

        player = game.player
        room = player.current_room


        if not hasattr(room, "has_key"):
            room.has_key = True
        
        key_name = "Clé du garde"

        if key_name in player.inventory.items:
            print("❌ Vous avez déjà la clé du garde dans votre inventaire.")
            return False
        
        if getattr(room, "has_key", False):
            player.inventory.add_item(key_name)
            room.has_key  = False
            print(f"✨ Vous recevez {key_name} ! Elle est maintenant dans votre inventaire.")
            return True
        else:
            print("❌ La clé du garde n'est pas disponible ici.")
            return False









    #AUBERGE
    def barman(game, list_of_words, number_of_parameters):
        """
        Passe à la salle liée à 'Barman' depuis la salle actuelle.
        """
        player = game.player
        current_room = player.current_room

        auberge = game.find_room("auberge")



        if not hasattr(player, "visited_npcs"): 
            #and "barman" in player.visited_npcs:
            #print("Le barman ne peut plus vous servir d'autre verre.")
            player.visited_npcs = set()
            
            if "barman" in player.visited_npcs and not getattr(current_room, "has_verre", False):
                print("🍺 Le barman : « Désolé, je ne peux plus vous servir. »")
                print(auberge.get_long_description())
    
                return True
                
                #del current_room.exits["barman"]
            


        # Première rencontre
        print("Le barman vous sourit : 'Voulez-vous une bière pour seulement 5 écus.'")
        print("Tape 'buy' pour l’acheter ou 'No' pour repartir.")

        
        current_room.has_verre = True
        
        if "barman" in auberge.exits:
            del auberge.exits["barman"]
        return True
    
        
    

        

        
    def fee(game, list_of_words, number_of_parameters):
        """
    Interaction avec la fée : elle propose une potion magique à 20 écus.
    Le joueur peut acheter la potion avec la commande 'buy'.
    Après l'achat, la fée disparaît.
    """
        player = game.player
        current_room = player.current_room

        auberge = game.find_room("auberge")

        if not hasattr(player, "visited_npcs"):
            player.visited_npcs = set()


        # Vérifie si la fée a déjà été rencontrée
        if "fee" in player.visited_npcs:
            print("✨ La fée n’est plus ici, elle est déjà partie dans la forêt.")
            player.current_room = auberge
            print(auberge.get_long_description())

            
            return True

        # Première rencontre
        print("🧚‍♀️ La fée vous sourit : 'Je peux te vendre une potion magique pour 20 écus.'")
        print("Tape 'buy' pour l’acheter ou 'No' pour repartir.")

        player.visited_npcs.add("fee")
        current_room.has_potion = True

        if "fee" in auberge.exits:
            del auberge.exits["fee"] 

        return True
        
        # Indique que la fée a une potion disponible
        current_room.has_potion = True

        return True

        

    
    

        
    

    def viking(game, list_of_words, number_of_parameters):
        """Le joueur rencontre le viking et subit des dégâts."""
        player = game.player
        current_room = player.current_room

        if not hasattr(player, "visited_npcs"): #and "viking" in player.visited_npcs:
            print("✨ Vous ne voulez plus parler au viking.")
            return True
        player.visited_npcs.add("viking")


            # Le viking attaque !
        print("\n🪓 Le viking vous remarque et vous attaque !")
        
            # Le joueur prend des dégâts
        player.health.take_damage(10)
        
            # Étape 4 — Affiche les PV restants après le coup
        player.health.show_health()

            # Si le joueur est mort → fin du jeu
        if player.health.is_dead():
                print("\n💀 Le viking vous a vaincu... GAME OVER 💀")
                game.finished = True
                return True
            
        #del current_room.exits["viking"]
            

            
                
        print("\nLe viking éclate de rire et vous tourne le dos.")
        return True
            

            

        


#=============================================================
#GASPARD

    
    def gaspard_action(game, list_of_words, number_of_parameters):
        player = game.player
        room = player.current_room

        if not hasattr(player, "in_pfc"):
            player.in_pfc = False

        qm = player.quest_manager
        for quest in qm.active_quests:
            quest.complete_objective("Découvrir le secret de cette maison", player)

        if not player.in_pfc:
            print("\n👻 Gaspard ricane...")
            print("« Si tu veux mon trésor, bats-moi à Pierre / Papier / Ciseau ! »")
            print("Tape : pierre / papier / ciseau")
            player.in_pfc = True
            return True
        return True
        
    
    def pierre(game, list_of_words, numbers_of_parameters):
        return Actions._pfc(game, "pierre")
    
    def papier(game, list_of_words, numbers_of_parameters):
        return Actions._pfc(game, "papier")
    
    def ciseau(game, list_of_words, numbers_of_parameters):
        return Actions._pfc(game, "ciseau")
    

    def _pfc(game, choix_joueur):

        import random

        player = game.player
        room = player.current_room

        if not getattr(player, "in_pfc", False):
            print("❌ Personne ne joue à Pierre / Papier / Ciseau ici.")
            return False
        
        choix_gaspard = random.choice(["pierre", "papier", "ciseau"])

        print(f"\n🧠 Gaspard choisit : {choix_gaspard}")

        #Egalité
        
        if choix_joueur == choix_gaspard:
            print("😐 Égalité ! Rejouons...")
            return True
        
        #Victoire

        gagne = (
            (choix_joueur == "pierre" and choix_gaspard == "ciseau") or
            (choix_joueur == "papier" and choix_gaspard == "pierre") or
            (choix_joueur == "ciseau" and choix_gaspard == "papier")
        )

        if gagne:
            print("\n✨ Gaspard hurle de rage ! Tu as gagné !")

            reward = "Lame de spectre"
            player.inventory.add_item(reward)

            print(f"🗡️ Vous obtenez : {reward}")

            player.in_pfc = False

            if "gaspard" in room.exits:
                del room.exits["gaspard"]

            secret_room = game.find_room("gaspard_secret")
            if secret_room:
                player.current_room = secret_room
                print(secret_room.get_long_description())

            return True
        
        
        #Défaite

        print("\n💀 Gaspard éclate de rire ! Tu as perdu !")
        print("Une force spectrale te repousse hors de la maison...")
        player.in_pfc = False
        player.current_room = game.find_room("village2")
        print(player.current_room.get_long_description())
        return True
        







    #LIEU

    def village(game, list_of_words, number_of_parameters):
        """
        Passe à la salle liée à 'village' depuis la salle actuelle.
        """
        player = game.player
        current_room = player.current_room

        if "village" in current_room.exits:
            next_room = current_room.exits["village"]
            player.current_room = next_room
            print("\n" + next_room.get_long_description())
            return True
        else:
            print("\nIl n'y a rien qui réponde à 'village' ici.")
            return False
        

    def auberge(game, list_of_words, number_of_parameters):
        """
        Passe à la salle liée à 'auberge' depuis la salle actuelle.
        """
        player = game.player
        current_room = player.current_room

        if "auberge" in current_room.exits:
            next_room = current_room.exits["auberge"]
            player.current_room = next_room
            print("\n" + next_room.get_long_description())
            return True
        else:
            print("\nIl n'y a rien qui réponde à 'auberge' ici.")
            return False
        



    def maison(game, list_of_words, number_of_parameters):
        """
            Passe à la salle liée à 'maison hantee' depuis la salle actuelle.
            """
        player = game.player
        current_room = player.current_room

        if "maison" in current_room.exits:
            next_room = current_room.exits["maison"]
            player.current_room = next_room
            print("\n" + next_room.get_long_description())
            return True
        else:
            print("\nIl n'y a rien qui réponde à 'maison' ici.")
            return False
        



    def enter_maison(game, list_of_words, number_of_parameters):
        """Permet de rentrer dans la maison hantee si et seulement le joueur possède la 'Clé du garde'."""
        player = game.player
        current_room = player.current_room
        
        if current_room.name != "maison":
                print("❌ Vous ne pouvez pas entrer ici.")
                return False

        if "Clé du garde" not in game.player.inventory.items:
            
            player.current_room = game.find_room("village2")
            print("🔒 La porte est verrouillée. Il vous faut la clé du garde !")
            print("\nVous êtes renvoyé sur la place du village.")
            print(player.current_room.get_long_description())
            return False
        
        
        
        
        next_room = game.find_room("enter maison")
        player.current_room = next_room

        if hasattr(player, "quest_manager"):
            player.quest_manager.check_room_objectives("maison")


        print("🔑 Vous utilisez la clé du garde et entrez dans la maison hantée...")
        print(next_room.get_long_description())
        
            
        return True

            


        

#=================================================================================
    #Acheter/vendre/obtenir des objets :
    


    
    
    
    
    #Clé du garde

    def auto_give_guard_key(game):
        """Donne automatiquement la clé quand on entre dans garde_talk."""

        player = game.player
        room = player.current_room
        # Si la clé a déjà été donnée : ne rien faire
        
        if getattr(room, "has_given_key", False):
        
        #if room.has_given_key:
            return

        # Sinon, donner la clé
        key_name = "Clé du garde"
        player.inventory.add_item(key_name)

        print("\n🔑 Le garde vous tend une clé secrète...")
        print(f"Vous obtenez : {key_name} !")

        # Empêcher de la recevoir deux fois
        room.has_given_key = True

    

    def use_key(game, list_of_words, number_of_parameters):
        """"Utiliser la potion que vous avez acheter à la fée.\nVous redonne 20PV"""

        player = game.player
        key_name = "Clé du garde"

        if key_name in player.inventory.items:
            player.inventory.remove_item(key_name)
            print("✨ Vous avez utilisé la clé du garde.")
            return True
        else:
            print("❌ Vous n'avez pas de clé dans votre inventaire.")
            return False

            
    
    #Potion :
    
    def buy(game, list_of_words, number_of_parameters):
        """Permet d'acheter une potion uniquement lorsque la fée la propose."""
        player = game.player
        current_room = player.current_room
        

        # Vérifie que l'achat est possible uniquement dans la salle de la fée
        if hasattr(current_room, "has_potion") and current_room.has_potion:
            
            potion_price = 20
            potion_name = "Potion magique"
            
           

            # Vérifie l'argent du joueur
            if player.gold < potion_price:
                print("💸 Vous n'avez pas assez d'écus pour acheter la potion.")
                return False

            # Achat réussi
            player.gold -= potion_price
            player.inventory.add_item(potion_name)
            current_room.has_potion = False
            player.visited_npcs.add("fee")

            if "fee" in current_room.exits:
                del current_room.exits["fee"]
            auberge = game.find_room("auberge")
            player.current_room = auberge

            print(f"🧪 Vous avez acheté une {potion_name} pour {potion_price} écus.")
            print(f"💰 Il vous reste {player.gold} écus.")
            print("✨ La fée s’envole vers la forêt et disparaît dans un nuage scintillant...")
            return True

        #Verre
        
        if hasattr(current_room, "has_verre") and current_room.has_verre:
            verre_price = 5
            verre_name = "Bière"

            if player.gold < verre_price:
                print("💸 Vous n'avez pas assez pour une bière.")
                return False
            
            player.gold -= verre_price
            player.inventory.add_item(verre_name)
            current_room.has_verre = False

            print("🍺 Vous achetez une bière !")
            print(f"💰 Il vous reste {player.gold} écus.")

            if "barman" in current_room.exits:
                del current_room.exits["barman"]

            auberge = game.find_room("auberge")
            player.current_room = auberge
            
            print("\nVous retournez vous asseoir dans l’auberge.")
            print(current_room.get_long_description())
            
            return True
        

        # ================= FORGERON =================
        if getattr(game, "current_vendor", None) == "forgeron":
            
            
            if len(list_of_words) != 2:
                print("Usage : buy <arme>")
                return False

            item = list_of_words[1].lower()

            armes = Actions.FORGERON_ARMES

            
            if item not in armes:
                print("❌ Le forgeron ne vend pas cette arme.")
                return False

            arme = armes[item]

            if player.gold < arme["price"]:
                print("💸 Vous n'avez pas assez d'écus.")
                return False

        # Achat
            player.gold -= arme["price"]
            player.weapon = arme
            player.inventory.add_item(arme["name"])

            print(f"\n⚔️ Vous achetez : {arme['name']}")
            print(f"💥 Dégâts : {arme['damage']}")
            print(f"💰 Il vous reste {player.gold} écus")
    
    #FORGERON_ARMES = {"dague": { "name": "Dague", "damage": 10, "price": 15}, "epee": { "name": "Épée", "damage": 20,"price": 30},"marteau": { "name": "Marteau", "damage": 35, "price": 60}}

        return True
    
        

        



        


    def use_potion(game, list_of_words, number_of_parameters):
        """"Utiliser la potion que vous avez acheter à la fée.\nVous redonne 20PV"""

        player = game.player
        potion_name = "Potion magique"

        if potion_name in player.inventory.items:
            player.health.heal(20)
            player.inventory.remove_item(potion_name)
            print("✨ Vous avez bu la potion magique et récupéré 20 PV !")
            player.health.show_health()
            return True
        else:
            print("❌ Vous n'avez pas de potion magique dans votre inventaire.")
            return False
        

    def use(game, list_of_words, number_of_parameters):

        player = game.player

        if len(list_of_words) < 2:
            print("Utiliser quoi ?")
            return False
        
        objet = " ".join(list_of_words[1:]).lower()
        


        # POTION

        if "potion" in objet:
            if player.inventory.remove_item_by_name("potion"):
                
                print("🧪 Vous buvez la potion...")
                player.health.heal(20)
                player.health.show_health()
                player.inventory.remove_item_by_name
                print("✅ La potion a été consommée.")
                return True
            else:
                print("❌ Vous n'avez pas de potion.")
                return False
        

        print(f"❌ Vous ne pouvez pas utiliser '{objet}'.")
        return False
        
        
        




    #Objets/Actions


    def viking_damage(game, list_of_words, number_of_parameters):
        """Le joueur parle au viking et subit des dégâts."""
        player = game.player
        current_room = player.current_room

        if "viking" in current_room.exits:
            next_room = current_room.exits["viking"]
            player.current_room = next_room

        # ✅ Le viking attaque !
            print("\n🪓 Le viking vous remarque et vous attaque !")
            player.health.take_damage(30)

        # Si le joueur est mort, on arrête la partie
        if player.health.is_dead():
            print("\n💀 Le viking vous a vaincu... GAME OVER 💀")
            game.finished = True
            return True

        # Sinon, on montre la description de la salle
            
            print("\n" + next_room.get_long_description())
            return True
        else:
            print("\nIl n'y a pas de viking ici.")
            return False
        

    
    def enfant_talk_action(game, list_of_words, number_of_parameters):
        player = game.player
        room = player.current_room     
            
     

        # Incrémenter le compteur
        player.enfant_talk_count += 1

        # 1ère et 2ème tentative → l'enfant a peur
        if player.enfant_talk_count < 3:
            print("\nL'enfant recule, il a peur de vous...")
            print("Essayer encore ? (Yes / No)")
            return True

        # 3ème tentative → révélation
        else:
            secret_name = "Secret de l'enfant"
            player.inventory.add_item(secret_name)
            
            print("\nL'enfant finit par vous faire confiance...")
            print("Il vous donne un papier où un secret sur le village est écrit dessus !")


            player.current_room = game.rooms_by_name["enfant_secret"]
            print(player.current_room.get_long_description())
            return True
        
    

    def lire(game, list_of_words, number_of_parameters):
        player = game.player


        if  len(list_of_words) != 2:
            print("Usage : lire <objet>")
            return False


        
        objet = list_of_words[1]



             # Recherche dans l’inventaire
        for item in player.inventory.items:
            if isinstance(item, dict) and item["name"] == objet:
                print("\nVous lisez le papier :")
                print(f"📜 {item['description']}")
                return True

        print(f"❌ Vous n'avez aucun objet nommé '{objet}' dans votre inventaire.")
        return False




    def retour(game, params, nb_params):
        player = game.player
        
        if getattr(player, "in_boss_fight", False):
            print("❌ Impossible de faire marche arrière en plein combat !")
            return True
        
        




        if player.previous_rooms:
        # Prendre la dernière salle visitée
            last_room = game.player.previous_rooms.pop()
            game.player.current_room = last_room
            print(f"Vous retournez à la salle précédente : {last_room.name}")
            print(last_room.get_long_description())
        else:
            print("Vous n'avez pas de salle précédente.")


    FORGERON_ARMES = {"dague": { "name": "Dague", "damage": 10, "price": 15}, "epee": { "name": "Épée", "damage": 20,"price": 30},"marteau": { "name": "Marteau", "damage": 35, "price": 50}}


    def forgeron(game, list_of_words, number_of_parameters):

        player = game.player
        room = player.current_room


        print("\nLe forgeron vous regarde attentivement.")
        print("Je peux te vendre une arme :")
        print("- dague : 10 dégâts — 15 écus")
        print("- epee : 20 dégâts — 30 écus")
        print("- marteau : 35 dégâts — 60 écus")
        print("\nTape : buy dague / buy epee / buy marteau")
        print("Ou tape 'retour' pour partir.")

        # On indique au jeu que le joueur est chez le forgeron
        game.current_vendor = "forgeron"
        return True



    def look(game, list_of_words, number_of_parameters):

        player = game.player
        room = player.current_room

        print("\n" + room.description)

        if hasattr(room, "npcs") and room.npcs:
            print("\n👥Vous voyez ici :")
            for npc in room.npcs.keys():
                print(f"-{npc}")
        
            
            return True
        


    def talk(game, list_of_words, number_of_parameters):
        player = game.player
        room = player.current_room

        if len(list_of_words) != 2:
            print("Usage : talk <personne>")
            return False

        target = list_of_words[1]

        if not hasattr(room, "npcs") or target not in room.npcs:
            print(f"❌ Il n'y a personne nommé '{target}' ici.")
            return False

        npc_action = room.npcs[target]
    

        npc_action(game, [target], 0)

        return True


    def milo(game, list_of_words, number_of_parameters):
        player = game.player


        if player.milo_state == "absent":
            print("\n😰 Milo tremble :")
            print("« J-je suis perdu... Tu peux me protéger ? »")
            print("Tape Yes pour accepter, No pour refuser.")
            
            player.waiting_milo_choice = True
            return True
        elif player.milo_state == "suiveur":
            print("Milo est déjà avec vous.")
            return True


    def boss_final(game, list_of_words, nulber_of_parameters):
        player = game.player

        print("\n👹 Le boss final apparaît !")

        if player.milo_state == "suiveur":
            print("\n😨 Milo tremble derrière vous...")
            print("Puis il relève la tête.")
            print("« J’ai eu peur toute ma vie… mais pas cette fois ! »")

            player.milo_state = "courageux"

            print("✨ Milo attaque le boss par surprise !")
            print("💥 Le boss est affaibli !")

            # Exemple d’effet
            #boss.health -= 30

        print("\n⚔️ Le combat commence !")
        return True
    

    def milo_rumeur_boss(game):
        player = game.player
        room = player.current_room

        if room.name != "fin_village":
            return
        
        if getattr(player, "milo_has_talked_rumeur", False):
            return
        
        if player.milo_state in ["suiveur", "courageux"]:

            print("\n😰 Milo murmure à votre oreille :")
            print("« J’ai entendu une rumeur… Le boss final possède une arme capable de tout détruire !")
            print("Il faut être prudents… et ne pas se fier à ses forces seules. »")

            player.milo_has_talked_rumeur = True


    def boss_final(game, list_of_words=None, numnber_of_parameters=0):
        player = game.player

        print("\n👹 Le boss final apparaît !")

        player.in_boss_fight = True
        player.boss_health = 200

        print("\n⚔️ Le combat commence !")
        print("Tape : attaquer ou esquiver")
        print(f"💀 Boss : {player.boss_health} PV")
        print(f"❤️ Vous : {player.health.current_hp}/{player.health.max_hp} PV")


        return True
    
    
    def _boss_turn(game):
        player = game.player

        if player.boss_health <= 0:
            print("\n🎉 Vous avez vaincu le boss final !")
            player.in_boss_fight = False

             
            if hasattr(player, "quest_manager"):
                player.quest_manager.check_room_objectives("boss_final")
            
            
            return 
        
        if player.health.is_dead():
            print("\n💀 Vous êtes mort... GAME OVER.")
            game.finished = True
            return
        
        boss_choice = random.choice(["attaquer", "attaquer", "esquiver"])

        #Vérifie si le joueur a esquivé ce tour

        if getattr(player, "esquive_reussie", False):
            print("🛡️ Vous esquivez l'attaque du boss avec succès !")
            player.esquive_reussie = False



        else:
            if boss_choice == "attaquer":
                dmg = random.randint(10, 25)
                print(f"💀 Le boss vous attaque ! ({dmg} dégâts)")
                player.health.take_damage(dmg)

            else:
                print("👹 Le boss esquive et se prépare...")

        print(f"\n💀 Boss : {player.boss_health} PV")
        print(f"❤️ Vous : {player.health.current_hp}/{player.health.max_hp} PV")

            
            
            



       
        

    
    def attack_boss(game, list_of_words, number_of_parameters):
        player = game.player
        
        if not getattr(player, "in_boss_fight", False):
            print("Vous n'êtes pas en combat contre le boss.")
            return True
        
        # ATTAQUE SELON L'ARME CHOISIE

        if hasattr(player, "weapon") and player.weapon:
            dmg = player.weapon["damage"]
            print(f"⚔️ Vous attaquez le boss avec votre arme ! ({dmg} dégâts)")
        else:
            dmg = random.randint(5, 7) #dégat à main nue
            print(f"⚔️ Vous attaquez le boss à mains nues ! ({dmg} dégâts)")

        player.boss_health -= dmg
        if player.boss_health < 0:
            player.boss_health = 0

        Actions._boss_turn(game)
        return True


    def dodge_boss(game, list_of_words, number_of_parameters):
        player = game.player
        
        if not hasattr(game.player, "in_boss_fight"):
            print("Vous n'êtes pas en combat contre le boss.")
            return True
        
        print("🛡️ Vous tentez d'esquiver...")
        player.esquive_reussie = random.choice([True, False])
        Actions._boss_turn(game)
        return True

    
    FORGERON_ARMES_DMG = {"dague": { "name": "Dague", "damage": 10}, "epee": { "name": "Épée", "damage": 20},"marteau": { "name": "Marteau", "damage": 35}}



    def equip_weapon(game, list_of_words, number_of_parameters):
        player = game.player


        if number_of_parameters < 1:
            print("Équiper quoi ? Exemple : equiper epee")
            return True
        
        weapon_key = list_of_words[1].lower()
        armes = Actions.FORGERON_ARMES_DMG


        if weapon_key not in armes:
            print("Cette arme n'existe pas.")
            return True

        weapon = armes[weapon_key]

        inventory_lower = [item.lower() if isinstance(item, str) else item["name"].lower() for item in player.inventory.items]
        
        
        if weapon["name"].lower() not in inventory_lower:
            print("Vous ne possédez pas cette arme.")
            return True
        
        player.weapon = weapon

        print(f"🗡️ Vous équipez {weapon['name']}.")

        return True



    def quests(game, words, number_of_parameters):
        qm = game.player.quest_manager

        if not qm.quests:
            print("📜 Vous n'avez aucune quête.")
            return
        
        print("\n📜 Quêtes disponibles :")
        for quest in qm.quests:
            status = "✅ Active" if quest.is_active else "❌ Inactive"
            print(f"- {quest.title} ({status})")
        

    def quest(game, words, number_of_parameters):
        if len(words) < 2:

            print("❓ Quelle quête ? Exemple : quest Le secret de Gaspard")
            return
        
        quest_name = " ".join(words[1:])
       # quest_manager = game.player.quest_manager

        quest = game.player.quest_manager.get_quest_by_title(quest_name)

        if quest is None:
            print("❌ Quête introuvable.")
            return
        
        print(f"\n📜 {quest.title}")
        print(f"📝 {quest.description}\n")

        print("🎯 Objectifs :")
        for obj in quest.objectives:
            if obj in quest.completed_objectives:
                print(f"  ✅ {obj}")
            else:
                print(f"  ⬜ {obj}")
        print(f"\n🎁 Récompense : {quest.reward}")

        if quest.is_completed:
            print("🏆 Statut : TERMINÉE")
        elif quest.is_active:
            print("🔥 Statut : EN COURS")
        else:
            print("⏸️ Statut : NON ACTIVÉE")

    
    def activate(game, params, number_of_parameters):
        if len(params) < 2:
            print("\n⚠️ Veuillez préciser le nom de la quête à activer.\n")
            return
        
        quest_title = " ".join(params[1:])

        success = game.player.quest_manager.activate_quest(quest_title)
        if not success:
            print(f"\n❌ Quête '{quest_title}' introuvable ou déjà activée.\n")




    




            









        
        
            

       

        
