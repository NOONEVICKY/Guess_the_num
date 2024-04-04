import random as rn
import tkinter as tk
from tkinter import messagebox

def generate_number():
    return rn.randint(1, 100)

def check_guess(guess, target, chance):
  """
    check game
  """
    if guess < target:
        messagebox.showinfo("Too Low", f"Too Low! Try again. You have {chance} more chances.")
    elif guess > target:
        messagebox.showinfo("Too High", f"Too High! Try again. You have {chance} more chances.")
    else:
        messagebox.showinfo("Correct", f"{guess} is the Correct Number! You completed within {chance} chances.")
        return True  # Indicates that the correct number is guessed
    return False
    
def guess_from_entry():
  """
     guess_from_entry
  """
   
def play_game():
    """
    play game 
    """

root = tk.Tk()
root.title("Number Guessing Game")

max_attempts = 10
remaining_chances = tk.IntVar()

label_instruction = tk.Label(root, text="Guess the number between 1 and 100:")
label_instruction.pack()

entry_guess = tk.Entry(root)
entry_guess.pack()

button_guess = tk.Button(root, text="Guess", command=guess_from_entry)
button_guess.pack()

play_game()  # Start the game when the application starts

root.mainloop()
