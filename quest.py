class Quest:
    """Classe représentant une quête."""

    def __init__(self, title, description, objectives, reward=None):
        self.title = title
        self.description = description
        self.objectives = objectives  # liste de strings
        self.reward = reward

        # Attributs harmonisés
        self.is_active = False
        self.is_completed = False
        self.completed_objectives = []

    def activate(self):
        """Active la quête."""
        self.is_active = True
        print(f"\n🗡️  Nouvelle quête activée: {self.title}")
        print(f"📝 {self.description}\n")

    def complete_objective(self, objective, player=None):
        """Marque un objectif comme accompli."""
        if objective in self.objectives and objective not in self.completed_objectives:
            self.completed_objectives.append(objective)
            print(f"✅ Objectif accompli: {objective}")

            # Vérifie si tous les objectifs sont terminés
            if len(self.completed_objectives) == len(self.objectives):
                self.complete_quest(player)

            return True
        return False

    def complete_quest(self, player=None):
        """Marque la quête comme complétée et donne la récompense au joueur."""
        if not self.is_completed:
            self.is_completed = True
            print(f"\n🏆 Quête terminée: {self.title}")
            if self.reward:
                print(f"🎁 Récompense: {self.reward}")
                if player:
                    player.add_reward(self.reward)
            print()

    def check_room_objective(self, room_name, player=None):
        """Vérifie si visiter une salle complète un objectif."""
        room_objectives = [
            f"Visiter {room_name}",
            f"Explorer {room_name}",
            f"Aller à {room_name}",
            f"Entrer dans {room_name}"
        ]
        for obj in room_objectives:
            if self.complete_objective(obj, player):
                return True
        return False

    def get_status(self):
        if not self.is_active:
            return f"❓ {self.title} (Non activée)"
        if self.is_completed:
            return f"✅ {self.title} (Terminée)"
        return f"⏳ {self.title} ({len(self.completed_objectives)}/{len(self.objectives)} objectifs)"


class QuestManager:
    """Gère toutes les quêtes du joueur."""

    def __init__(self, player=None):
        self.quests = []
        self.active_quests = []
        self.player = player

    def add_quest(self, quest):
        self.quests.append(quest)

    def activate_quest(self, quest_title):
        for quest in self.quests:
            if quest.title.lower() == quest_title.lower() and not quest.is_active:
                quest.activate()
                self.active_quests.append(quest)
                return True
        return False

    def check_room_objectives(self, room_name):
        """Vérifie tous les objectifs liés aux salles pour toutes les quêtes actives."""
        for quest in self.active_quests[:]:  # copie pour éviter la modification pendant itération
            quest.check_room_objective(room_name, self.player)
            if quest.is_completed:
                self.active_quests.remove(quest)

    def show_quests(self):
        if not self.quests:
            print("\nAucune quête disponible.\n")
            return
        print("\n📋 Liste des quêtes:")
        for quest in self.quests:
            print(f"  {quest.get_status()}")
        print()


    def get_quest_by_title(self, title):
        title = title.strip().lower()
        for quest in self.quests:
            if quest.title.lower() == title:
                return quest
            return None