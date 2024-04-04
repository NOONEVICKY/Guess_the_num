import random as rn
import tkinter as tk
from tkinter import messagebox

def generate_number():
    return rn.randint(1, 100)

def check_guess(guess, target, chance):
  """
    check game
  """
    

def guess_from_entry():
  """
     guess_from_entry
  """
    guess = int(entry_guess.get())
    if check_guess(guess, target_number, remaining_chances.get()):
        root.quit()  # Exit the application if the correct number is guessed
   
def play_game():
    """
    play game 
    """
    global target_number
    target_number = generate_number()
    remaining_chances.set(max_attempts)

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
