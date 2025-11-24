# Description: The actions module.

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

from room import Room
from inventaire import Inventory
from health import Health


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
        print("\nVous quittez la jauge de vie et retournez en jeu :")
        print(player.current_room.get_long_description())
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
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1]
        # Move the player in the direction specified by the parameter.
        player.move(direction)
        return True

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
        #if "Yes" not in current_room.exits:
            
        #    print("\nIl n'y a rien qui réponde à 'Yes' ici.")
        #    return False

        #next_room = current_room.exits["Yes"]
        #player.current_room = next_room
            
            
        
        #if hasattr(next_room, "on_enter") and callable(next_room.on_enter):
        #    next_room.on_enter(game)  # <-- ici on passe bien room
        

        if current_room.name == "enfant_talk":
            
            player.child_talk_count += 1

            #if not hasattr(player, "child_talk_count"):
            #    player.child_talk.count = 0
            
            
            if player.child_talk_count < 2:
                print("\nL'enfant recule encore... Il a peur de vous.")
                print("Essayer encore ? (Yes / No)")
                return True
            
            
                
            next_room = game.find_room("enfant_secret")
            player.current_room = next_room

            papier_name = {
            "name": "papier","description": "Un petit papier froissé où l’enfant a écrit dessus : HoooOOOoooOOO… Gaspard HoooOOOoooOOO…."}
            
            player.inventory.add_item(papier_name)


            print("\n✨ L'enfant prend confiance en vous...")
            print("\nIl vous donne un secret papier. ")
            print(next_room.get_long_description())
            return True

                # Sinon, reste dans enfant_talk
            next_room = current_room
            player.current_room = next_room
            #print("\nL'enfant reste silencieux mais semble un peu plus détendu.")
            
            #if hasattr(next_room, "on_enter"):
            #    next_room.on_enter(game)
            #print("\n" + next_room.get_long_description())
            #return True
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

        if "No" in current_room.exits:
            next_room = current_room.exits["No"]
            player.current_room = next_room
            print("\n" + next_room.get_long_description())
            return True
        else:
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

        if hasattr(player, "visited_npcs") and "Yes" in player.visited_npcs:
            print("Le garde retourne à son poste et ne veut plus vous parler.")
            del current_room.exits["garde_talk"]
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





    #AUBERGE
    def barman(game, list_of_words, number_of_parameters):
        """
        Passe à la salle liée à 'Barman' depuis la salle actuelle.
        """
        player = game.player
        current_room = player.current_room

        #if "barman" in current_room.exits:
        #    next_room = current_room.exits["barman"]
        #    player.current_room = next_room
        #    print("\n" + next_room.get_long_description())
        #    return True
        #else:
        #    print("\nIl n'y a rien qui réponde à 'barman' ici.")
        #    return False



        if hasattr(player, "visited_npcs") and "barman" in player.visited_npcs:
            print("Le barman ne peut plus vous servir d'autre verre.")
            del current_room.exits["barman"]
            
            return False

        # Première rencontre
        print("Le barman vous sourit : 'Voulez-vous une bière pour seulement 5 écus.'")
        print("Tape 'buy' pour l’acheter ou 'No' pour repartir.")
    
        # Marque que le barman a été rencontrée
        if not hasattr(player, "visited_npcs"):
            player.visited_npcs = set()
            
        player.visited_npcs.add("barman")

        # Indique que le barman a un verre de disponible
        current_room.has_verre = True

        return True

        
        

        
    def fee(game, list_of_words, number_of_parameters):
        """
    Interaction avec la fée : elle propose une potion magique à 20 écus.
    Le joueur peut acheter la potion avec la commande 'buy'.
    Après l'achat, la fée disparaît.
    """
        player = game.player
        current_room = player.current_room

        if not hasattr(player, "visited_npcs"):
            player.visited_npcs = set()


        # Vérifie si la fée a déjà été rencontrée
        if "fee" in player.visited_npcs:
            print("✨ La fée n’est plus ici, elle est déjà partie dans la forêt.")
            if "fee" in current_room.exits:
                del current_room.exits["fee"]

            
            return False

        # Première rencontre
        print("🧚‍♀️ La fée vous sourit : 'Je peux te vendre une potion magique pour 20 écus.'")
        print("Tape 'buy' pour l’acheter ou 'No' pour repartir.")

        # Indique que la fée a une potion disponible
        current_room.has_potion = True

        return True

        

    
    

        
    

    def viking(game, list_of_words, number_of_parameters):
        """Le joueur rencontre le viking et subit des dégâts."""
        player = game.player
        current_room = player.current_room

        if hasattr(player, "visited_npcs") and "viking" in player.visited_npcs:
            print("✨ Vous ne voulez plus parler au viking.")
            return False

        # Vérifie si la sortie "viking" existe depuis la salle actuelle
        if "viking" in current_room.exits:
            next_room = current_room.exits["viking"]
            player.current_room = next_room

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
            
            del current_room.exits["viking"]
            

            
                
            
            # Sinon, on affiche la salle du viking
            print("\n" + next_room.get_long_description())

            
            return True
        else:
            print("\nIl n'y a pas de viking ici.")
            return False
        


    
    def gaspard_action(game, list_of_words, number_of_parameters):
        player = game.player
        room = player.current_room

        if not hasattr(player, "gaspard_try"):
            player.gaspard_try = 0

        player.gaspard_try += 1


        if player.gaspard_try > 3:

            print("\n👻 Gaspard pousse un hurlement spectral !")
            print("Une force invisible vous projette hors de la maison hantée !")
            player.current_room = game.find_room("village2")
            print("\nVous vous retrouvez sonné sur la place du village...")
            print(player.current_room.get_long_description())
            return True
        
        if player.gaspard_try < 3:

            print("\n👻 Gaspard vous fixe avec méfiance...")
            print("Essayer encore ? (Yes / No)")
            return True
        
        if player.gaspard_try == 3:

            print("\n✨ Le fantôme Gaspard vous accepte enfin...")
            print("Il laisse tomber un objet spectral au sol !")

            reward = "Lame de spectre"
            player.inventory.add_items(reward)


            if "gaspard" in room.exits:
                del room.exits["gaspard"]


            
            secret_room = game.find_room("gaspard_secret")
            if secret_room:
                player.current_room = secret_room
                print(secret_room.get_long_description())
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
            print("🔒 La porte est verrouillée. Il vous faut la clé du garde !")
            player.current_room = game.find_room("village2")
            print("\nVous êtes renvoyé sur la place du village.")
            print(player.current_room.get_long_description())
            return False
        
        
        next_room = game.find_room("enter maison")
        player.current_room = next_room

        print("🔑 Vous utilisez la clé du garde et entrez dans la maison hantée...")
        print(next_room.get_long_description())
        return True

            #print("\nVous utilisez la Clé du garde et entrez dans la maison hantée... ")
            

            #print("\nVous ne possédez pas la clé pour rentrer dans cette maison !\nVous décidez de retourner au village.")
            #village_room = game.find_room("maison hantee")
            #game.player.current_room = village_room
            #print(village_room.get_long_description())


        

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
            
            #print("❌ Vous ne pouvez acheter une potion qu’en parlant à la fée.")
            #return False

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
            return True
        
        
         # Rien à acheter ici
        print("❌ Il n'y a rien à acheter ici.")
        return False

        


        # Mise à jour : la fée disparaît
        current_room.description = "Vous êtes dans l’auberge chaleureuse du village.\nDes rires résonnent, des bougies éclairent les tables, et l’odeur de bière flotte dans l’air.\nLe barman vous salue d’un signe de tête."
        print("✨ La fée s’envole vers la forêt et disparaît dans un nuage scintillant...")

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




        

    
