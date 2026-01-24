# 🏰 TBA – The Brave Adventure

## 📖 Présentation du projet

**TBA (The Brave Adventure)** est un jeu d’aventure textuel développé en **Python**.  
Le joueur incarne un héros explorant un village mystérieux, interagissant avec des PNJ, accomplissant des quêtes et affrontant un boss final.

Le projet repose sur une architecture orientée objet et intègre :
- un système de **quêtes dynamiques**
- un **combat contre un boss**
- un **inventaire**
- des **récompenses**


---

## ⚙️ Installation

### Prérequis
- Python **3.10 ou plus**
- Lancement en **local recommandé** (surtout pour l’interface graphique)

### Installation
```bash
git clone https://github.com/nolhan-lareppe/Game.git
cd Game
python game.py
```

## 🎮 Comment jouer

```bash
Entrez votre nom:

```

Vous interagissez ensuite avec le jeu via des commandes textuelles.


## 🧭 Univers du jeu


Vous arrivez dans un village médiéval mystérieux :

- une auberge

- une forge

- une maison hantée

- des habitants étranges

- une rumeur sur un boss final…

Vos choix influencent votre progression.


## 🕹️ Commandes principales

# Déplacements

```bash
go <lieu>
retour
```

# Observation et interaction

```bash
look
talk <pnj>
Yes / No
gaspard
buy
lire <item>
```

# Combat

```bash
attaquer
esquiver
pierre / papier / ciseau
```

# inventaire et statistiques

```bash
inventaire
equiper <arme>
health
ecus
use <item>
```

# 📜 Système de quêtes

## Voir toutes les quêtes

```bash
quests
```

## Activer une quête

```bash
activate <nom de la quête>
```

## Voir le détail d'une quête

```bash
quest <nom de la quête>
```




## Quête : Grand Explorateur

Objectifs :

- Visiter l'auberge
- Visiter la forge

Récompense : 

- 🏅 Titre de Grand Explorateur

Les objectifs se valident automatiquement lorsque le joueur entre dans les lieux concernés.


## Quête : Découvreur de Secrets

Objectifs : 

- Visiter la maison
- Découvrir le secret de la maison hantée

💡 Le secret est découvert lorsque le joueur tape gaspard dans la maison hantée.

Récompense :

- 🗡️ Lame Spectrale

## ⚔️ Quête : Boss final 

Objectif :

- Vaincre le boss final

La quête se valide automatiquement à la fin du combat

- 🏆 Titre de Grand Héros du Village



## 🏆 Conditions de victoire et de défaite


Victoire

- Le boss final est vaincu

- Les quêtes peuvent être complétées

Défaite

- Le joueur perd tous ses points de vie

# 🧑‍💻 Guide développeur

## Architecteur du projet 

Classes principales : 

- ```Game``` : boucle principale du jeu
- ```Player``` : joueur, inventaire, quêtes
- ```Room``` : lieux, sorties et événements
- ```Quest``` : logique d'une quête
- ```QuestManager``` : gestion des quêtes
- ```Actions``` : toutes les commandes du joueur
- ```Inventaire``` : inventaire du joueur
- ```Health``` : point de vie
- ```Weapon``` : 



classDiagram
    direction LR

    class Game {
        -finished : bool
        -rooms : list[Room]
        -commands : dict[str, Command]
        -player : Player
        +setup()
        +play()
        +process_command()
        +find_room()
    }

    class Player {
        +name : str
        +current_room : Room
        +inventory : Inventory
        +health : Health
        +quest_manager : QuestManager
        +add_reward()
    }

    class Room {
        +name : str
        +description : str
        +exits : dict
        +npcs : dict
        +on_enter()
        +get_long_description()
    }

    class Command {
        +name : str
        +description : str
        +action : function
        +number_of_parameters : int
        +execute()
    }

    class Actions {
        <<static>>
        +go()
        +attack_boss()
        +enter_maison()
        +gaspard_action()
        +quests()
        +quest()
        +activate()
    }

    class QuestManager {
        +quests : list[Quest]
        +active_quests : list[Quest]
        +add_quest()
        +activate_quest()
        +get_quest_by_title()
        +check_room_objectives()
    }

    class Quest {
        +title : str
        +description : str
        +objectives : list[str]
        +completed_objectives : list[str]
        +reward : str
        +is_active : bool
        +is_completed : bool
        +activate()
        +complete_objective()
        +complete_quest()
    }

    class Inventory {
        +items : list
        +add_item()
        +remove_item()
        +show()
    }

    class Health {
        +hp : int
        +max_hp : int
        +lose_hp()
        +heal()
    }

    %% Relations
    Game --> Player
    Game --> Room
    Game --> Command
    Command --> Actions

    Player --> Inventory
    Player --> Health
    Player --> QuestManager

    QuestManager --> Quest
    Room --> Actions





# 🚀 Perspectives d’évolution

- Finaliser l'interface graphique
- Dialogues plus complexes avec les PNJ
- Amélioration du Boss final pour plus de difficulté
- Ajout de nouvelles zones et quêtes secondaires
- Dialogue plus immersif


#### Projet réalisé par Nolhan Lareppe