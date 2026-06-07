# AI Buckshot Roulette

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Numba](https://img.shields.io/badge/numba-JIT_Compiler-red)
![NumPy](https://img.shields.io/badge/numpy-required-orange)

A Python terminal-based strategy game inspired by the mechanics of *Buckshot Roulette*, featuring an artificial intelligence built, trained, and optimized entirely from scratch without relying on high-level Machine Learning frameworks like TensorFlow or PyTorch.

## About the Project

This project serves as a proof-of-concept for building custom mathematical optimization algorithms and implementing extreme performance optimizations in Python. 

The application simulates a tactical game of Russian Roulette. The player and the AI compete using a shotgun loaded with a hidden, randomized sequence of real and blank bullets. The strategic depth lies in the choice to shoot oneself (to pass the turn and potentially skip a blank) or shoot the opponent.

The core of the project relies on a custom mathematical model that trains itself upon startup through stochastic simulation, evaluating hundreds of millions of game states to dynamically adjust its decision weights via an empirical implementation of Gradient Descent / Hill Climbing.

## Key Features & Technical Highlights

- **Custom Machine Learning Model:** The AI calculates discrete mathematical derivatives (slopes) empirically. It tests weight variations, calculates the absolute error (loss function), and shifts the parameters toward the local minimum to optimize the win rate.
- **Just-In-Time (JIT) Compilation:** The game engine (`game.py`) and the testing environment are compiled directly to LLVM machine code using **Numba** (`@njit` and `@jitclass`). This bypasses the Python interpreter's Global Interpreter Lock (GIL) and type-checking overhead.
- **Static Typing & Memory Management:** Standard Python lists are replaced with `numba.typed.List` and strict `int64` typing to ensure maximum C-level execution speed. Array broadcasting (NumPy) inside the hot-loops was refactored into raw compiled `for` loops to prevent memory allocation bottlenecks during execution.
- **I/O Telemetry Optimization:** The training and testing loops feature real-time ETA calculation using carriage return (`\r`) buffering, avoiding standard system calls (like `os.system('cls')`) to prevent CPU bottlenecks and maintain maximum iteration throughput.

## How the AI Works

The AI reads the remaining bullets in the chamber and multiplies the values by an internal continuous variable (`weight`). 

During the `train()` phase:
1. The parameter is initialized with a positive integer to avoid the "flat gradient" problem (zero-slope region in the loss landscape).
2. The model simulates extensive game batches and evaluates the `abs_error` (percentage of critical failures/losses).
3. It evaluates three adjacent points on the function (`weight - step`, `weight`, `weight + step`) to extract the empirical slope.
4. The weight is updated iteratively until the algorithm detects a local minimum (both slopes returning positive values).

During gameplay, if the calculated dot product between the remaining bullets and the optimized weight exceeds a hardcoded `threshold`, the AI shoots the opponent. Otherwise, it executes a self-shot to cycle the chamber.

## Installation & Setup

### Prerequisites
Python 3.8 or higher is required. The project relies on `numpy` for standard mathematical operations and `numba` for JIT compilation.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-backshot-roulette.git
   cd ai-backshot-roulette
   ```

2. Install dependencies:
   ```bash
   pip install numpy numba matplotlib
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## How to Play

Upon execution, the AI will perform a dynamic training session to adjust its internal weights based on the specified parameters.
- Players start with 5 lives.
- A dynamic ASCII representation of the chamber is printed to the terminal.
- On your turn, select an action:
  - `[0]`: **Shoot at yourself**. If it is a blank, you retain your turn. If real, you lose a life.
  - `[1]`: **Shoot at the enemy**. If it is a real bullet, the enemy loses a life. The turn passes to the opponent regardless.
- The simulation terminates when a player's lifepoints reach zero.

## Project Structure

- `game.py`: The core physics and rules engine. Strictly typed and JIT-compiled for maximum execution speed.
- `AI.py`: Contains the `SimpleAi` class handling the gradient descent logic and inference.
- `test_gradient.py`: A dedicated telemetry module to benchmark the loss function landscape across tens of millions of stochastic iterations, rendering the output via Matplotlib.
- `main.py`: The entry point. Handles the UI loop, I/O sanitization, and ASCII rendering.
