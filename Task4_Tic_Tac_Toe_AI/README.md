# Task 4 – Tic-Tac-Toe AI

## Overview

This project is a console-based Tic-Tac-Toe game developed using Python. The player competes against an AI opponent.

The AI uses the **Minimax algorithm** to select optimal moves. **Alpha-Beta pruning** is also implemented to improve the efficiency of the Minimax search.

## Features

* Human vs AI gameplay
* Tic-Tac-Toe game logic
* Minimax algorithm
* Alpha-Beta pruning
* Easy difficulty
* Medium difficulty
* Hard difficulty
* Input validation
* Win, lose, and draw detection

## Technologies Used

* Python
* Minimax Algorithm
* Alpha-Beta Pruning

## Difficulty Levels

### Easy

The AI selects a random available position.

### Medium

The AI sometimes makes a random move and sometimes uses the Minimax algorithm.

### Hard

The AI uses the Minimax algorithm with Alpha-Beta pruning to select an optimal move.

## How to Run

Open PowerShell and navigate to the project folder:

```bash
cd Task4_Tic_Tac_Toe_AI
```

Run the program:

```bash
python tic_tac_toe.py
```

Choose a difficulty level:

```text
1. Easy
2. Medium
3. Hard
```

Then enter a board position from 1 to 9.

## Board Positions

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

The human player uses **X** and the AI uses **O**.

## Minimax Algorithm

The Minimax algorithm evaluates possible future moves and selects the move that provides the best outcome for the AI.

The AI gives scores to game states:

* Positive score → AI advantage
* Negative score → Player advantage
* Zero → Draw

The algorithm searches through possible future moves before selecting the AI's move.

## Alpha-Beta Pruning

Alpha-Beta pruning improves Minimax by avoiding branches of the game tree that cannot affect the final decision.

This reduces unnecessary calculations while maintaining the same optimal decision as Minimax.

## Example

```text
===================================
       TIC-TAC-TOE AI
===================================

You are X.
The AI is O.

Choose difficulty:
1. Easy
2. Medium
3. Hard
```

## Project Structure

```text
Task4_Tic_Tac_Toe_AI/
│
├── tic_tac_toe.py
└── README.md
```

## Learning Outcome

This project demonstrates game development concepts, decision-making algorithms, recursion, Minimax search, and Alpha-Beta pruning using Python.
