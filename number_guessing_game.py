import tkinter as tk
import random
def check_guess():
    global attempts
    try:
        guess = int(entry_guess.get())
        attempts += 1

        if guess < random_number:
            label_feedback.config(text="Too low! Try again.", fg="red")
        elif guess > random_number:
            label_feedback.config(text="Too high! Try again.", fg="red")
        else:
            label_feedback.config(text=f"Correct! You guessed it in {attempts} attempts.",
                                  fg="green")
            button_guess.config(state="disabled")
    except ValueError:
        label_feedback.config(text="Invalid input! Please enter a valid number.", fg="red")

    entry_guess.delete(0, tk.END)


def reset_game():
    global random_number, attempts
    random_number = random.randint(1, 100)
    attempts = 0
    entry_guess.delete(0, tk.END)
    label_feedback.config(text="Guess the number between 1 and 100", fg="black")
    button_guess.config(state="normal")


random_number = random.randint(1, 100)
attempts = 0

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.config(bg="#f0f0f0")

label_title = tk.Label(root, text="Guess the Number Game", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#4A4A4A")
label_title.pack(pady=20)

label_instruction = tk.Label(root, text="Enter a number between 1 and 100:", font=("Helvetica", 12), bg="#f0f0f0")
label_instruction.pack()

entry_guess = tk.Entry(root, width=5, font=("Helvetica", 14), justify="center", bg="#d9f2d9")
entry_guess.pack(pady=10)

button_guess = tk.Button(root, text="Guess", command=check_guess, font=("Helvetica", 12, "bold"), bg="#4CAF50",
                         fg="white", activebackground="#45a049")
button_guess.pack(pady=5)

label_feedback = tk.Label(root, text="Guess the number between 1 and 100", font=("Helvetica", 12), bg="#f0f0f0",
                          fg="black")
label_feedback.pack(pady=20)

button_reset = tk.Button(root, text="Reset Game", command=reset_game, font=("Helvetica", 12, "bold"), bg="#2196F3",
                         fg="white", activebackground="#1976D2")
button_reset.pack(pady=5)

root.mainloop()
