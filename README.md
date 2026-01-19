# TBA

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

C'est un jeu narratif avec des interractions avec des personnages non joueur





## OPTIMISAITON

- Quelques optimisation peuvent être faite au niveau du jeu, notamment avec le côté interractif. Au lieu d'utiliser "go" utiliser une commande immersif permettant de répondre directement au PNJ.

- Ajout de plus d'items pour plus de diversité au jeu.

- Au niveau du garde, donner la clé automatiquement plutôt d'utiliser "give"git 



