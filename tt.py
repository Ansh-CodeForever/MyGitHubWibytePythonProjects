import turtle

def validation_failed():
    def draw_kahoot_incorrect_icon(radius=50):
        """Draws a red circle with a white cross inside (Kahoot-style)."""
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.speed(0)

        # Draw red circle
        pen.penup()
        pen.goto(0, -radius)  # Move to bottom of circle
        pen.pendown()
        pen.fillcolor("red")
        pen.begin_fill()
        pen.circle(radius)
        pen.end_fill()

        # Draw white cross inside
        pen.pensize(radius // 5)  # Thickness proportional to size
        pen.color("white")

        # First diagonal
        pen.penup()
        pen.goto(-radius * 0.6, radius * 0.6)
        pen.pendown()
        pen.goto(radius * 0.6, -radius * 0.6)

        # Second diagonal
        pen.penup()
        pen.goto(radius * 0.6, radius * 0.6)
        pen.pendown()
        pen.goto(-radius * 0.6, -radius * 0.6)

    def show_validation_failed():
        try:
            # Create screen
            screen = turtle.Screen()
            screen.title("Validation Status")
            screen.bgcolor("black")  # Black background
            screen.setup(width=800, height=600)

            # Draw the Kahoot-style incorrect icon
            draw_kahoot_incorrect_icon(radius=120)

            # Write the message
            pen = turtle.Turtle()
            pen.hideturtle()
            pen.penup()
            pen.color("white")
            pen.goto(0, -200)
            pen.write("Validation Failed", align="center", font=("Arial", 30, "bold"))
            pen.penup()
            pen.goto(0, -215)
            pen.write("There was an error", align="center", font=("Arial", 15, "bold"))

            # Console output
            print("Validation Failed")

            screen.mainloop()

        except turtle.Terminator:
            print("Turtle graphics window closed unexpectedly.")
        except Exception as e:
            print(f"An error occurred: {e}")

    if __name__ == "__main__":
        show_validation_failed()