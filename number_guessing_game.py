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

def reset_game():
    global random_number, attempts
    random_number = random.randint(1, 100)
    attempts = 0
    entry_guess.delete(0, tk.END)
    label_feedback.config(text="Guess the number between 1 and 100", fg="black")
    button_guess.config(state="normal")

def increase_value():
    try:
        value = int(entry_guess.get())
    except ValueError:
        value = 0
    entry_guess.delete(0, tk.END)
    entry_guess.insert(0, str(value + 1))

def decrease_value():
    try:
        value = int(entry_guess.get())
    except ValueError:
        value = 0
    entry_guess.delete(0, tk.END)
    entry_guess.insert(0, str(value - 1))

random_number = random.randint(1, 100)
attempts = 0

window = tk.Tk()
window.title("Number Guessing Game")
window.iconbitmap("D:/Projects/PYTHON/GO2COD/numbers_ico.ico")
window.geometry("400x300")
window.config(bg="#f0f0f0")

label_title = tk.Label(window, text="Guess the Number Game", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#4A4A4A")
label_title.pack(pady=20)

label_instruction = tk.Label(window, text="Enter a number between 1 and 100:", font=("Helvetica", 12), bg="#f0f0f0")
label_instruction.pack()

frame = tk.Frame(window, bg="#f0f0f0")
frame.pack(pady=10)

button_decrease = tk.Button(frame, text="<", command=decrease_value, font=("Helvetica", 12, "bold"), width=2, bg="#D3D3D3", fg="black")
button_decrease.pack(side="left", padx=5)

entry_guess = tk.Entry(frame, width=5, font=("Helvetica", 14), justify="center", bg="#D3D3D3")
entry_guess.pack(side="left")

button_increase = tk.Button(frame, text=">", command=increase_value, font=("Helvetica", 12, "bold"), width=2, bg="#D3D3D3", fg="black")
button_increase.pack(side="left", padx=5)

button_guess = tk.Button(window, text="Guess", command=check_guess, font=("Helvetica", 12, "bold"), bg="#4CAF50",
                         fg="white", activebackground="#45a049")
button_guess.pack(pady=5)

label_feedback = tk.Label(window, text="Guess the number between 1 and 100", font=("Helvetica", 12), bg="#f0f0f0",
                          fg="black")
label_feedback.pack(pady=20)

button_reset = tk.Button(window, text="Reset Game", command=reset_game, font=("Helvetica", 12, "bold"), bg="#2196F3",
                         fg="white", activebackground="#1976D2")
button_reset.pack(pady=5)

window.mainloop()
