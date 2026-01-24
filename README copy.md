Ce repo contient la première version (minimale) du jeu d’aventure TBA.

Les lieux sont au nombre de 6. Il n'y a pas encore d’objets ni de personnages autres que le joueur et très peu d’interactions. Cette première version sert de base à ce qui va suivre, et sera améliorée au fur et à mesure.


## Structuration

Il y a pour le moment 5 modules contenant chacun une classe.

- `game.py` / `Game` : description de l'environnement, interface avec le joueur ;
- `room.py` / `Room` : propriétés génériques d'un lieu  ;
- `player.py` / `Player` : le joueur ;
- `command.py` / `Command` : les consignes données par le joueur ;
- `actions.py` / `Action` : les interactions entre .
- `weapon.py` / `Weapon` : l'équipement d'armes.
- `inventaire.py` / `Inventaire` : permet de stocker des objets/armes
- `health.py` / `Health` : point de vie du joueur ;



## GAME

C'est un jeu narratif avec des interractions avec des personnages non joueur, certains personnages peuvent proposer des objets, des jeux ou alors des indices. 


## COMMANDE


- `go` : permet le déplacement entre une Room à l'autre
- `help` : permet de voir les commandes 
- `quit` : permet de quitter le jeu
- `inventaire` : permet de regarder ce que l'on a dans son inventaire
- `



## DIAGRAMME 



classDiagram
    class Game {
        -rooms : list
        -player : Player
        -commands : dict
        -health : Health
        +setup()
        +play()
        +process_command(command_string)
        +find_room(name)
    }

    class Player {
        -name : str
        -current_room : Room
        -inventory : Inventory
        -quest_manager : QuestManager
        -health : Health
        +add_reward(reward)
    }

    class Room {
        -name : str
        -description : str
        -exits : dict
        -npcs : dict
        -on_enter : function
        -has_given_key : bool
        +get_long_description()
    }

    class Inventory {
        -items : list
        +add_item(item)
        +remove_item(item)
        +show_inventory()
    }

    class Health {
        -points : int
        +show_health()
        +modify_health(amount)
    }

    class Quest {
        -title : str
        -description : str
        -objectives : list
        -is_active : bool
        -is_completed : bool
        -completed_objectives : list
        -reward : str
        +activate()
        +complete_objective(objective)
        +check_room_objective(room_name)
        +check_action_objective(action, target)
        +check_counter_objective(counter_name, current_count)
        +get_status()
        +get_details()
    }

    class QuestManager {
        -quests : list
        -active_quests : list
        -player : Player
        +add_quest(quest)
        +activate_quest(title)
        +check_room_objectives(room_name)
        +check_action_objectives(action, target)
        +check_counter_objectives(counter_name, current_count)
        +get_active_quests()
        +show_quests()
        +show_quest_details(title)
    }

    Game --> Player
    Game --> Room
    Game --> QuestManager
    Player --> Inventory
    Player --> QuestManager
    Room --> "0..*" NPCs
    QuestManager --> Quest


 





## OPTIMISAITON

- Quelques optimisation peuvent être faite au niveau du jeu, notamment avec le côté interractif. Au lieu d'utiliser "go" utiliser une commande immersif permettant de répondre directement au PNJ.

- Ajout de plus d'items pour plus de diversité au jeu.

- Au niveau du garde, donner la clé automatiquement plutôt d'utiliser "give"
