# Genetic Algorithm Solver for 8-Puzzle Variation

This project implements a basic **Genetic Algorithm (GA)** in Python to solve a simplified version of the 8-puzzle problem. It uses population initialization, fitness evaluation, crossover, and mutation to evolve potential solutions over generations.

---

## 🧩 Problem Overview

Each board is represented as a 1D list of 9 integers ranging from 0 to 8. The goal is to evolve this list so that each number matches its correct position (i.e., `genes[i] == i + 1` for the first 8 positions and `genes[8] == 0`).

---

## 📌 Features

- Random board generation
- Fitness evaluation based on number placement
- Crossover of parent boards at two different cutoffs
- Random mutation to maintain diversity
- Iterative evolution until an optimal board is found

---

## 🔧 How It Works

1. **Initialize** a population of random boards.
2. **Evaluate** their fitness scores.
3. **Sort** the population by fitness.
4. **Crossover** pairs of boards to create new generations.
5. **Mutate** new boards with a random chance.
6. **Repeat** until a board reaches the perfect fitness score of `9`.

---

## 🧬 Genetic Operators

- **Fitness Function:**  
  +1 for each correctly placed number.  
  +1 if the last number is 0.

- **Crossover:**  
  Combines part of parent A and part of parent B to create a child.

- **Mutation:**  
  Randomly changes one gene value in a board.

---

## 🖥️ Output Example
Initialized Population
[1, 2, 5]
[3, 6, 0]
[4, 7, 8]
Fitness: 4

...

Solved Board is: [1, 2, 3, 4, 5, 6, 7, 8, 0]

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/genetic-8puzzle.git
   cd genetic-8puzzle
   python main.py


