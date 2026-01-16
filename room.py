# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

        
        self.npcs = {}
        self.on_enter = None

        self.has_given_key = False





    def on_enter(self, game):
        pass
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        
        if hasattr(self, "on_enter") and self.on_enter is not None:
            # Appeler l’action automatique SANS arguments
            self.on_enter_callback = True
        return f"\n{self.description}\n\n{self.get_exit_string()}\n"
