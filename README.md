## Tik-Tak-AI: A Heuristic-Based Tic-Tac-Toe AI Player

This repository showcases a Tic-Tac-Toe AI player implemented using heuristic rules. The AI leverages strategic decision-making to compete effectively against human players.

**Key Features:**

* **Heuristic Evaluation:** The AI employs a utility-based approach, assigning values to board positions based on their win potential for the AI or blocking potential for the opponent.
* **Strategic Gameplay:** The AI prioritizes winning moves, followed by moves that hinder the opponent's winning opportunities. It also considers less advantageous positions if necessary.
* **Performance Optimization:** Through heuristic guidance, the AI significantly reduces the number of explorable game states compared to a brute-force approach.

**Getting Started:**

1. **Clone the Repository:** Use `git clone https://github.com/princegbabuwo/Tik-Tak-AI.git` to clone the code.
2. **Run the Script:** Navigate to the cloned directory (`cd tik-tak-ai`) and execute `python main.py` to play against the AI.

**Target Audience:**

This project caters to data science professionals and potential employers seeking candidates with proficiency in:

* Heuristic design
* Algorithmic optimization
* Python programming
* Game AI concepts

This project was inspired by the coursework from the Udemy course: Artificial Intelligence and Machine Learning Fundamentals by Packt Publishing (https://www.udemy.com/course/artificial-intelligence-and-machine-learning-fundamentals/).

**Performance Metrics:**

According to www.half-real.net/tictactoe, there are 255,168 possible unique Tic-Tac-Toe games. This project's heuristic approach significantly reduces the number of game states explored by the AI while maintaining strong performance. Here's a breakdown:

* **Reduced Game States:** The heuristic guidance reduces the explorable games from 255,168 (original) to 2,240 (with heuristics). This represents a **99.1%** efficiency improvement.
* **Win Rate:** When the AI plays first, it achieves a win rate of 224 wins out of 248 games (roughly 90%). This indicates a strong performance against the human player.
* **Draw Rate:** The draw rate remains at around 344 games regardless of the AI's starting position.

The `gameCounts()` function, included in the `main.py` script, calculates these game state counts using a `Depth-First-Search` approach.
