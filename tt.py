import tkinter as tk
from tkinter import font

def draw_card_gui(name, category_stats):
    root = tk.Tk()
    root.title("Top Trumps Card")

    canvas = tk.Canvas(root, width=300, height=400, bg="white")
    canvas.pack()

    # Card border
    canvas.create_rectangle(20, 20, 280, 380, outline="black", width=3)

    # Title
    title_font = font.Font(family="Helvetica", size=18, weight="bold")
    canvas.create_text(150, 50, text=name, font=title_font, fill="blue")

    # Stats
    stat_font = font.Font(family="Helvetica", size=14)
    y_pos = 100
    for category, value in category_stats.items():
        canvas.create_text(100, y_pos, text=category, font=stat_font, anchor="w")
        canvas.create_text(250, y_pos, text=str(value), font=stat_font, anchor="e")
        y_pos += 40

    root.mainloop()


# Example usage
card_name = "Dragon"
stats = {
    "Strength": 95,
    "Speed": 80,
    "Magic": 70,
    "Defense": 88
}

draw_card_gui(card_name, stats)