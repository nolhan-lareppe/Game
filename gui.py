import tkinter as tk
from game import Game

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🗡️ Aventure Textuelle")

        self.game = Game()
        self.game.setup()

        # Zone de texte
        self.text_area = tk.Text(root, height=25, width=80, wrap="word")
        self.text_area.pack(padx=10, pady=10)
        self.text_area.config(state="disabled")

        # Champ de commande
        self.entry = tk.Entry(root, width=70)
        self.entry.pack(side="left", padx=10)
        self.entry.bind("<Return>", self.run_command)

        # Bouton
        self.button = tk.Button(root, text="Valider", command=self.run_command)
        self.button.pack(side="left")

        # Affichage initial
        self.print_text(self.game.player.current_room.get_long_description())

    def print_text(self, text):
        self.text_area.config(state="normal")
        self.text_area.insert(tk.END, text + "\n\n")
        self.text_area.config(state="disabled")
        self.text_area.see(tk.END)

    def run_command(self, event=None):
        command = self.entry.get()
        self.entry.delete(0, tk.END)

        self.print_text(f"> {command}")
        self.game.process_command(command)

        if self.game.finished:
            self.print_text("🎮 Fin de la partie")




if __name__ == "__main__":
    root = tk.Tk()
    GameGUI(root)
    root.mainloop()