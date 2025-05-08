
# ASD-UniTN

**ASD-UniTN** is a Python-based roguelike project developed as part of the Algorithms and Data Structures course at the University of Trento.  
The game features procedural dungeon generation, enemy AIs powered by various pathfinding algorithms, and a modular structure designed for experimentation and learning.

---

## 🧩 Project Structure

The repository contains the following key folders:

- **RougueLike/src/**: Core game implementation.
  - `main.py`: Main game loop and setup.
  - `map.py`: Handles dungeon generation, rooms, corridors, and MST logic.
  - `player.py`: Player class and movement logic.
  - `enemy.py`: Basic enemy AI using A* pathfinding.
  - `enemyMST.py`: Advanced enemy AI using MST-based movement and greedy pathfinding with memoization.

- **BFS/DFS and graphs/**: BFS, DFS, and graph-related exercises.

- **DP/**: Dynamic Programming exercises and implementations.

- **weighted graphs/**: Weighted graph problems and algorithms.

---

## 🎮 Features

- **Procedural Dungeon Generation**: Based on Kruskal's algorithm with room overlap prevention and corridor connection.
- **Enemy AI**:
  - `Enemy`: Tracks the player using A*.
  - `enemyMST`: Moves between rooms via MST, uses greedy search with memoization.
- **Player Control**: Move with arrow keys or WASD.
- **Graphical Interface**: Uses Pygame for tile-based rendering.

---

## 🛠 Requirements

- Python 3.6+
- Pygame

---

## 🚀 How to Run

```bash
git clone https://github.com/ismacarbo/ASD-UniTN.git
cd ASD-UniTN/RougueLike/src
pip install pygame
python main.py
```

---

## 🎯 Project Goals

- Practice real-world application of algorithms and data structures.
- Implement and compare various pathfinding strategies (A*, greedy, memoization).
- Use modular Python design.
- Develop a fun, expandable roguelike engine.

---

## 📁 Folder Overview

```
ASD-UniTN/
├── BFS/ DFS and graphs/
├── DP/
├── RougueLike/
│   └── src/
│       ├── enemy.py
│       ├── enemyMST.py
│       ├── main.py
│       ├── map.py
│       └── player.py
└── weighted graphs/
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📄 License

MIT License – see [LICENSE](LICENSE) for details.

---

For any questions, contact the author via GitHub: [ismacarbo](https://github.com/ismacarbo)
