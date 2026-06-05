# 🔫 AI Backshot Roulette

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![NumPy](https://img.shields.io/badge/numpy-required-orange)
![License](https://img.shields.io/badge/license-MIT-green)

A Python terminal-based strategy game inspired by the mechanics of *Buckshot Roulette*, featuring an artificial intelligence built and trained entirely from scratch without the use of pre-existing Machine Learning libraries (like TensorFlow or PyTorch).

## 🧠 About the Project

This project was built as a personal challenge to design and implement a custom mathematical optimization algorithm from the ground up. 

In this game, you play a tactical game of Russian Roulette against an AI using a shotgun loaded with a random sequence of **real** and **blank** bullets. You can choose to shoot yourself (to pass the turn and potentially skip a blank) or shoot the opponent. 

The core highlight of this project is the **`SimpleAi`** class. Instead of hard-coding the bot's decisions, the AI trains itself upon startup. It simulates thousands of game states, evaluates the absolute error of its choices, and uses a custom optimization logic (conceptually similar to **1D Gradient Descent / Hill Climbing**) to adjust its decision weights dynamically by calculating mathematical slopes.

## ✨ Features

- **Custom Machine Learning Model:** The AI calculates derivatives (slopes) empirically to minimize the error rate and adjust its aggression weight.
- **Object-Oriented Programming (OOP):** Modular architecture separating the Game Engine (`game.py`), the AI logic (`AI.py`), and the UI/Main Loop.
- **Dynamic ASCII Art:** Real-time visual representation of the bullets on the table right in the terminal.
- **Smart Turn Management:** Full handling of bullet counting, lifepoints, and automatic chamber reloading.

## 🚀 How the AI Works

The AI analyzes the remaining bullets array and multiplies it by an internal `weight`. 
During the `train()` phase:
1. The AI generates random scenarios and tests its current `weight`.
2. It calculates the `abs_error` (the percentage of times the chosen move leads to a loss).
3. It takes three nearby points (`weight - step`, `weight`, `weight + step`) and calculates the slopes (derivatives) between them.
4. It dynamically shifts the weight in the direction that minimizes the error until it hits a local minimum where both slopes are positive.

Once trained, if the calculated probability exceeds a specific `threshold`, the bot decides to shoot the enemy; otherwise, it shoots itself.

## 🛠️ Installation & Setup

### Prerequisites
You need Python 3.8+ installed on your system. The project also requires `numpy` for array mathematical operations.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-backshot-roulette.git
   cd ai-backshot-roulette
   ```

2. Install dependencies:
   ```bash
   pip install numpy
   ```

3. Run the game:
   ```bash
   python main.py
   ```
*(Note: replace `main.py` with the actual name of your runner file)*

## 🎮 How to Play

Upon running the game, the AI will perform a brief training session. After that, the game begins:
- Both you and the AI start with 5 lives.
- You will see the total bullets on the table.
- On your turn, you must choose:
  - `[0]`: **Shoot at yourself** (If it's a blank, you keep your turn).
  - `[1]`: **Shoot at the enemy** (If it's a real bullet, they lose a life; turn passes).
- The game continues until a player's lives reach 0.

## 📂 Project Structure

- `game.py`: Contains the `Game` class. Manages bullets, lives, turns, and game rules.
- `AI.py`: Contains the `SimpleAi` class. Handles the mathematical training loop and decision-making process.
- `main.py`: The entry point of the script. Handles user inputs, the `while` loops, and rendering the ASCII graphics.

## 🗺️ Roadmap & Future Improvements

- [ ] Rename `lifes` to `lives` to follow proper English syntax.
- [ ] Refactor repetitive code (DRY principle) by extracting bullet-reloading logic into a dedicated method.
- [ ] Add an iteration limit (epochs) to the `while True` loop inside the AI training method to prevent infinite loops in flat-gradient scenarios.
- [ ] Separate the win-state logic from `make_move()` to the main loop for better architecture.

## 👤 Author

Developed by a passionate high-school student in a single day as a personal coding and logic challenge. 

---
*Feel free to fork this project, submit pull requests, or use the code as inspiration for your own custom AI experiments!*
