import tkinter as tk
from tkinter import font
import random

# --- Global Game Variables ---
user_score = 0
computer_score = 0
choices = ["rock", "paper", "scissors"]

# Using emojis for hand display - ensure your system/font supports them
emojis = {
    "rock": "✊",
    "paper": "🖐️", # or "✋"
    "scissors": "✌️"
}
default_hand = "❓" # Placeholder before first choice

# --- Game Logic Functions ---
def get_computer_choice():
    """Generates a random choice for the computer."""
    return random.choice(choices)

def determine_winner(player_choice, comp_choice):
    """Determines the winner of the round."""
    if player_choice == comp_choice:
        return "tie"
    elif (player_choice == "rock" and comp_choice == "scissors") or \
         (player_choice == "scissors" and comp_choice == "paper") or \
         (player_choice == "paper" and comp_choice == "rock"):
        return "player"
    else:
        return "computer"

def play_round(player_choice_str):
    """Handles the logic for playing a single round."""
    global user_score, computer_score

    computer_choice_str = get_computer_choice()

    # Update hand displays
    user_hand_label.config(text=emojis[player_choice_str])
    computer_hand_label.config(text=emojis[computer_choice_str])

    winner = determine_winner(player_choice_str, computer_choice_str)

    result_text = ""
    if winner == "player":
        user_score += 1
        result_text = "You Win!"
        result_message_label.config(fg="#2ecc71") # Green for win
    elif winner == "computer":
        computer_score += 1
        result_text = "You Lose!"
        result_message_label.config(fg="#e74c3c") # Red for lose
    else:
        result_text = "It's a Tie!"
        result_message_label.config(fg="white") # White for tie

    # Update score displays and result message
    user_score_display_label.config(text=str(user_score))
    computer_score_display_label.config(text=str(computer_score))
    result_message_label.config(text=result_text)

# --- UI Setup ---
window = tk.Tk()
window.title("PYTHON - Rock Paper Scissors")
window.geometry("700x650")  # Width x Height
window.configure(bg="#9b59b6")  # Medium purple background (inspired by screenshot)

# --- Fonts (adjust family and size as needed) ---
title_font = font.Font(family="Arial", size=18, weight="bold")
label_font = font.Font(family="Arial", size=14) # For general labels if needed
score_font = font.Font(family="Arial", size=24, weight="bold")
hand_font = font.Font(family="Arial", size=80) # For emoji hands
button_font = font.Font(family="Arial", size=12, weight="bold")
result_font = font.Font(family="Arial", size=18, weight="bold")
footer_font = font.Font(family="Verdana", size=16, weight="bold") # Different font for banner

# --- Main Display Area (Computer vs User) ---
main_display_frame = tk.Frame(window, bg=window["bg"]) # Use window's bg
main_display_frame.pack(pady=30) # Add padding around this frame

# Computer Area
computer_frame = tk.Frame(main_display_frame, bg=window["bg"])
computer_frame.grid(row=0, column=0, padx=40, sticky="n") # sticky North for top alignment

computer_title_label = tk.Label(computer_frame, text="COMPUTER", font=title_font, bg=window["bg"], fg="white")
computer_title_label.pack(pady=(0,10)) # Padding: (top, bottom)

# Frame to simulate the colored "circle" background for computer's hand
computer_hand_bg = tk.Frame(computer_frame, bg="#f1c40f", width=150, height=150) # Yellow
computer_hand_bg.pack_propagate(False) # Prevent frame from shrinking to fit content
computer_hand_bg.pack()
computer_hand_label = tk.Label(computer_hand_bg, text=default_hand, font=hand_font, bg="#f1c40f", fg="white")
computer_hand_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # Center emoji in the frame

computer_score_display_label = tk.Label(computer_frame, text=str(computer_score), font=score_font, bg=window["bg"], fg="white")
computer_score_display_label.pack(pady=(10,0))


# User Area
user_frame = tk.Frame(main_display_frame, bg=window["bg"])
user_frame.grid(row=0, column=1, padx=40, sticky="n") # Grid for side-by-side placement

user_title_label = tk.Label(user_frame, text="USER", font=title_font, bg=window["bg"], fg="white")
user_title_label.pack(pady=(0,10))

# Frame for user's hand "circle"
user_hand_bg = tk.Frame(user_frame, bg="#e74c3c", width=150, height=150) # Red
user_hand_bg.pack_propagate(False)
user_hand_bg.pack()
user_hand_label = tk.Label(user_hand_bg, text=default_hand, font=hand_font, bg="#e74c3c", fg="white")
user_hand_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

user_score_display_label = tk.Label(user_frame, text=str(user_score), font=score_font, bg=window["bg"], fg="white")
user_score_display_label.pack(pady=(10,0))


# --- Choice Buttons Area ---
button_frame = tk.Frame(window, bg=window["bg"])
button_frame.pack(pady=30)

# Button styling values
btn_width = 10
btn_height = 2
btn_padx = 10

rock_button = tk.Button(button_frame, text="ROCK", font=button_font, bg="#e74c3c", fg="white", width=btn_width, height=btn_height, command=lambda: play_round("rock"))
rock_button.grid(row=0, column=0, padx=btn_padx)

# Paper button: Yellow with black text, as per screenshot
paper_button = tk.Button(button_frame, text="PAPER", font=button_font, bg="#f1c40f", fg="black", width=btn_width, height=btn_height, command=lambda: play_round("paper"))
paper_button.grid(row=0, column=1, padx=btn_padx)

# Scissor button: Blue/Teal, as per screenshot
scissors_button = tk.Button(button_frame, text="SCISSOR", font=button_font, bg="#3498db", fg="white", width=btn_width, height=btn_height, command=lambda: play_round("scissors"))
scissors_button.grid(row=0, column=2, padx=btn_padx)


# --- Result Message Area ---
result_message_label = tk.Label(window, text="Choose your weapon!", font=result_font, bg=window["bg"], fg="white")
result_message_label.pack(pady=20)

# --- Footer Banner (like in screenshot) ---
footer_banner_label = tk.Label(window, text="ROCK, SCISSOR & PAPER GAME", font=footer_font, bg="#6c3483", fg="#f1c40f", pady=10) # Darker purple, yellow/gold text
footer_banner_label.pack(side=tk.BOTTOM, fill=tk.X, pady=(10,0)) # Add padding on top only


# Initialize scores on UI for the first launch
user_score_display_label.config(text=str(user_score))
computer_score_display_label.config(text=str(computer_score))

# Start the Tkinter event loop
window.mainloop()