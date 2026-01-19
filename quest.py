class Quest:

    class Quest:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.started = False
        self.completed = False

    def start(self):
        self.started = True
        print(f"📜 Quête commencée : {self.name}")
        print(self.description)

    def complete(self):
        self.completed = True
        print(f"✅ Quête terminée : {self.name}")
