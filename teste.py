import tkinter as tk
import random

class RomanticApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Romantic App")
        self.root.geometry("600x400")
        self.root.configure(bg="pink")

        self.button_clicks = 0

        self.label = tk.Label(root, text="Clique no botão para abrir a caixa!", 
                              font=("Helvetica", 16), bg="pink", fg="red")
        self.label.pack(pady=20)

        self.button = tk.Button(root, text="Abrir Caixa", font=("Helvetica", 14), 
                                bg="red", fg="white", command=self.on_button_click)
        self.button.place(x=250, y=150)

        self.root.bind("<Motion>", self.move_button)

    def move_button(self, event):
        if self.button_clicks < 5:
            # Coordenadas do mouse
            mouse_x, mouse_y = event.x, event.y
            # Coordenadas do botão
            button_x, button_y = self.button.winfo_x(), self.button.winfo_y()
            button_width, button_height = self.button.winfo_width(), self.button.winfo_height()

            # Verifica se o mouse está dentro da área próxima ao botão
            if (button_x - 50 <= mouse_x <= button_x + button_width + 50 and
                button_y - 50 <= mouse_y <= button_y + button_height + 50):
                # Move o botão para uma nova posição aleatória
                x = random.randint(0, self.root.winfo_width() - button_width)
                y = random.randint(0, self.root.winfo_height() - button_height)
                self.button.place(x=x, y=y)

    def on_button_click(self):
        self.button_clicks += 1
        if self.button_clicks >= 5:
            self.label.config(text="Te amo ❤️")
            self.button.config(text="Sim!", command=self.accept_proposal)

    def accept_proposal(self):
        self.label.config(text="❤️")
        self.button.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RomanticApp(root)
    root.mainloop()