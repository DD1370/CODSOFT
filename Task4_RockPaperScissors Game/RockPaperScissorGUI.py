import tkinter as tk
from tkinter import messagebox
import random

root =tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x700")
root.configure(bg="#EAF4FF")
root.resizable(False,False)



title_label=tk.Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=('Arial',20,"bold"),
    fg="#003366",
    bg="#EAF4FF"

)
title_label.pack(pady=10)

rules_label=tk.Label(
    root,
    text=(
        "Rules:\n"
        "• Rock beats Scissors\n"
        "• Paper beats Rock\n"
        "• Scissors beats Paper"
    ),
    font=('Arial',11),
    bg="#D6EBFF"
)
rules_label.pack(pady=10)

round_label=tk.Label(
    root,
    text="Round: 1",
    font=("Arial",12,"bold"),
    bg="#5895D6",
    fg="white"
)
round_label.pack()

score_label=tk.Label(
    root,
    text="Your Score: 0 ",
    font=("Arial",12,"bold"),
    bg="#2E5177",
    fg="white"
)
score_label.pack()

computer_score_label=tk.Label(
    root,
    text="Computer Score: 0",
    font=("Arial",12,"bold"),
    bg="#2E5177",
    fg="white"


)
computer_score_label.pack()
choice_title = tk.Label(
    root,
    text="Choose Your Move",
    font=("Arial",12,"bold"),
    bg="#EAF4FF"
)

choice_title.pack()

button_frame = tk.Frame(root,bg="#EAF4FF")
button_frame.pack(pady=20)

choice_label = tk.Label(
    root,
    text="Computer Choice: -",
    font=("Arial", 12,"bold"),
    bg="#EAF4FF",
    
)

choice_label.pack(pady=10)

status_label = tk.Label(
    root,
    text="Status: Waiting for your move...",
    font=("Arial", 12, "bold"),
    bg="white",
    relief="sunken",
    bd=2
)

status_label.pack(pady=10)

history_label = tk.Label(
    root,
    text="Game History",
    font=("Arial", 12, "bold"),
    bg="white",
    bd=2
)

history_label.pack()

history_listbox = tk.Listbox(
    root,
    width=55,
    height=6,
    bg="white",
    bd=2,
    font=("Arial",10)
)

history_listbox.pack(pady=10)

history_listbox.insert(
    tk.END,
    "Game started..."
)

player_score = 0
computer_score = 0
round_number = 1

options = ("Rock", "Paper", "Scissors")

def determine_winner(player, computer):

    if player == computer:
        return "Tie"

    elif player == "Rock" and computer == "Scissors":
        return "Win"

    elif player == "Paper" and computer == "Rock":
        return "Win"

    elif player == "Scissors" and computer == "Paper":
        return "Win"

    else:
        return "Lose"
    
def play_game(player_choice):

    global player_score
    global computer_score
    global round_number

    computer_choice = random.choice(options)
    result = determine_winner(player_choice,computer_choice)

    if result == "Win":
        player_score += 1

    elif result == "Lose":
        computer_score += 1

    choice_label.config(
        text=f"Computer Choice: {computer_choice}"
    )
    if result=="Tie":
        status_label.config(
        text=f"Status: It's a {result}!"
    )
    else:
        status_label.config(
        text=f"Status: You {result}!"
    )

    score_label.config(
        text=f"Your Score: {player_score}"
    )

    computer_score_label.config(
        text=f"Computer Score: {computer_score}"
    )

    history_message = (
        f"Round {round_number}: "
        f"{player_choice} vs {computer_choice} "
        f"→ {result}"
    )

    history_listbox.insert(
        tk.END,
        history_message
    )

    history_listbox.see(tk.END)

    round_number += 1

    round_label.config(
        text=f"Round: {round_number}"
    )
def end_game():
    if not messagebox.askyesno(
    "Exit Game",
    "Are you sure you want to end the game?"
    ):
        return

    if player_score > computer_score:
        winner = "🏆 You Won The Match!"

    elif computer_score > player_score:
        winner = "💻 Computer Won The Match!"

    else:
        winner = "🤝 The Match Is A Tie!"

    messagebox.showinfo(
        "Game Over",
        f"Your Score: {player_score}\n"
        f"Computer Score: {computer_score}\n\n"
        f"{winner}"
    )

    root.destroy()

def reset_game():
    global player_score
    global computer_score
    global round_number

    player_score = 0
    computer_score = 0
    round_number = 1

    round_label.config(text="Round: 1")

    score_label.config(text="Your Score: 0")

    computer_score_label.config(
        text="Computer Score: 0"
    )

    choice_label.config(
        text="Computer Choice: -"
    )

    status_label.config(
        text="Status: Waiting for your move..."
    )

    history_listbox.delete(0, tk.END)
    history_listbox.insert(
    tk.END,
    "Game restarted..."
    )

rock_button = tk.Button(
        button_frame,
        text="🪨",
        width=4,
        height=1,
        font=("Arial",22),
        command=lambda: play_game("Rock"),
        bg="#B3D9FF",
        activebackground="#80BFFF"
)
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(
        button_frame,
        text="📃",
        font=("Arial",22),
        width=4,
        height=1,
        command=lambda: play_game("Paper"),
        bg="#B3D9FF",
        activebackground="#80BFFF"
    )
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(
        button_frame,
        text="✂️",
        width=4,
        height=1,
        font=("Arial",22),
        command=lambda: play_game("Scissors"),
        bg="#B3D9FF",
        activebackground="#80BFFF"
)
scissors_button.grid(row=0, column=2, padx=5)
button_bottom_frame = tk.Frame(root, bg="#EAF4FF")
button_bottom_frame.pack(pady=10)
reset_button = tk.Button(
    button_bottom_frame,
    text="Reset Game",
    width=15,
    command=reset_game
)
reset_button.grid(row=0,column=0,padx=10)

exit_button = tk.Button(
    button_bottom_frame,
    text="Exit Game",
    width=15,
    command=end_game,
    bg="#FF9999",
    activebackground="#FF6666"
)
exit_button.grid(row=0,column=1,padx=10)

root.mainloop()