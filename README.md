# Theory of Languages and Automata - Practical Project

A comprehensive practical project exploring the theory of computation through implementation of Turing machines and cellular automata.

## Project Overview

This project is part of the Theory of Languages and Automata (TLA) course at Iran University of Science and Technology (IUST), taught by Dr. Farzaneh Ghayour Baghbani.

The project consists of two main parts that explore fundamental concepts in theoretical computer science:

1. **Part 1: Turing Machines and the Busy Beaver Problem** - Implementation of a Turing machine simulator with applications to mathematical computations and exploration of the undecidable Busy Beaver problem.

2. **Part 2: Cellular Automata and Universal Computation** - Implementation of two famous cellular automata (Conway's Game of Life and Langton's Ant) and exploration of computational universality through digital logic gates.

## Course Information

- **University**: Iran University of Science and Technology (IUST)
- **Course**: Theory of Languages and Automata (TLA)
- **Instructor**: Dr. Farzaneh Ghayour Baghbani
- **Academic Level**: Bachelor's Degree
- **Project Type**: Team University Course Project
- **Completion Date**: July 14, 2026

## Project Structure

```text
.
├── Part 1 - Busy Beaver/          # Turing machines and Busy Beaver problem
│   ├── README.md                  # Part 1 documentation
│   ├── turing_machine.py          # Turing machine simulator
│   ├── busy_beaver.py             # Busy Beaver implementations
│   ├── student_test_turing.py     # Self-assessment tests
│   ├── test_turing_machine_example*.py
│   ├── test_turing_adder.py       # Unary addition test
│   ├── test_turing_multiplier.py  # Unary multiplication test
│   └── test_busy_beaver_2.py      # Busy Beaver test
│
├── Part 2 - GoL & Langton's Ant/  # Cellular automata
│   ├── README.md                  # Part 2 documentation
│   ├── conway.py                  # Game of Life implementation
│   ├── langton.py                 # Langton's Ant implementation
│   ├── logic_gates.py             # Logic gates using Game of Life
│   ├── pygame_gol.py              # GUI for Game of Life
│   ├── pygame_viewer.py           # Pattern viewer utility
│   ├── langton_pygame.py           # GUI for Langton's Ant
│   ├── test_gameoflife_glider*.py # Game of Life tests
│   └── *.cells                    # Pattern files (RLE/Plaintext format)
│
└── README.md                       # This file
```

## Key Concepts

### Part 1: Turing Machines

A **Turing Machine** is a mathematical model of computation that represents a fundamental model of a computer. Key components include:

- **Finite state machine**: A set of states determining machine behavior
- **Tape**: An infinite or semi-infinite memory where symbols are read and written
- **Head**: A pointer that reads and writes symbols on the tape
- **Transition rules**: Rules that determine state changes based on the current state and symbol

In this part, the project explores:

- A Turing machine simulator with support for bidirectional tape
- Mathematical computations: addition and multiplication using unary representation
- The **Busy Beaver problem**: investigating Turing machines that maximize the number of 1s written on their tape before halting, illustrating the connection between computation and undecidability

### Part 2: Cellular Automata

**Cellular Automata** are discrete computational models consisting of a grid of cells, each with a finite set of states. The next state of each cell depends on its current state and neighboring cells.

#### Conway's Game of Life

A two-dimensional cellular automaton governed by four rules:

1. **Underpopulation**: A live cell with fewer than 2 live neighbors dies.
2. **Survival**: A live cell with 2 or 3 live neighbors survives.
3. **Overpopulation**: A live cell with more than 3 live neighbors dies.
4. **Reproduction**: A dead cell with exactly 3 live neighbors becomes alive.

Despite its simple rules, the Game of Life exhibits complex emergent behavior and can support universal computation.

#### Langton's Ant

Langton's Ant is a two-dimensional cellular automaton in which an ant moves across a grid and changes cell states according to simple rules. Its behavior demonstrates how simple local interactions can produce complex patterns.

#### Turing Completeness

The project explores computational universality through logic-gate constructions, including AND and NOT gates using gliders in Conway's Game of Life.

## Learning Outcomes

Through this project, students explore how to:

- Understand Turing machines and their role in theoretical computer science
- Implement simulators for abstract computational models
- Explore universality and Turing completeness
- Investigate computability and undecidability through the Busy Beaver problem
- Observe how simple local rules can produce complex global behavior
- Understand connections between different computational models

## Technical Stack

- **Language**: Python 3
- **Visualization**: Pygame for graphical simulations
- **Scientific Computing**: NumPy and SciPy for cellular automata computation
- **File Formats**: RLE (Run Length Encoded) and plaintext formats for Game of Life patterns

## Getting Started

For detailed instructions on running and exploring each part, see the corresponding README files:

- [Part 1 - Busy Beaver](Part%201%20-%20Busy%20Beaver/README.md) - Turing machine implementation and Busy Beaver experiments
- [Part 2 - GoL & Langton's Ant](Part%202%20-%20GoL%20%26%20Langton's%20Ant/README.md) - Cellular automata and logic-gate experiments

## Teamwork & Acknowledgements

This project was developed collaboratively with a teammate as part of the Theory of Languages and Automata course. We divided the project tasks between us and worked together on the implementation and development of the different components.

I appreciate my teammate's collaboration and contributions throughout the project.

## References

- Moore, C. and Mertens, S. (2011). *The Nature of Computation*. Oxford University Press.
- Conway's Game of Life - Wikipedia and LifeWiki
- Langton's Ant - Wikipedia
- Busy Beaver problem and related databases

## Additional Resources

- Computerphile: Turing Machine Primer
- Computerphile: Busy Beaver Turing Machines
- Turing completeness tutorials and visualizations
- Digital logic gates in Conway's Game of Life

---

*This project was completed as part of the Theory of Languages and Automata course at Iran University of Science and Technology (IUST).*
