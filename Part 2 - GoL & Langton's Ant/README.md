# Part 2: Cellular Automata — Conway's Game of Life and Langton's Ant

This project explores **cellular automata as models of computation**, focusing on Conway's Game of Life, Langton's Ant, and the use of cellular automata to represent digital logic. It demonstrates how simple local rules can produce complex patterns and how cellular systems can be used to explore fundamental concepts in computation theory.

## Overview

**Cellular automata** are discrete mathematical systems made up of cells arranged on a grid. Each cell has a state that changes over time according to a set of rules and, in many cases, the states of neighboring cells.

Although their rules can be simple, cellular automata can exhibit complex behavior, including stable structures, repeating patterns, moving signals, and computational universality.

This project is organized around three main topics:

- **Conway's Game of Life:** A two-dimensional cellular automaton in which cells are either alive or dead and evolve according to their neighboring cells.
- **Langton's Ant:** A grid-based system in which an ant moves and changes cell states according to simple turning rules.
- **Computational Logic in Game of Life:** An exploration of how interactions between moving patterns, known as gliders, can represent logical operations.

## Project Components

### 1. Conway's Game of Life

Conway's Game of Life is a cellular automaton introduced by mathematician John Conway. The system evolves in discrete generations, with every cell determined by its current state and the number of living cells in its eight-cell neighborhood.

The rules are:

1. **Underpopulation:** A living cell with fewer than two living neighbors dies.
2. **Survival:** A living cell with two or three living neighbors remains alive.
3. **Overpopulation:** A living cell with more than three living neighbors dies.
4. **Reproduction:** A dead cell with exactly three living neighbors becomes alive.

These rules can generate a wide range of behaviors, from stable configurations and oscillators to moving patterns and structures that continuously produce new patterns.

The project includes the Game of Life simulation in `conway.py`, visualization support through `pygame_gol.py`, and pattern-related utilities.

### 2. Langton's Ant

Langton's Ant is a cellular automaton that consists of an ant moving across a grid of cells. The ant's direction and the state of each cell determine how the system evolves.

In the classic two-color version:

- On a white cell, the ant changes the cell to black, turns right, and moves forward.
- On a black cell, the ant changes the cell to white, turns left, and moves forward.

Despite these simple deterministic rules, the system produces complex behavior. Its movement initially appears irregular, but after many steps it develops a repeating diagonal path commonly known as the **highway**.

The project explores this behavior through `langton.py` and its visualization interface, `langton_pygame.py`. The system also provides a context for studying variations that use multiple cell colors and different turning rules.

### 3. Logic Gates and Turing Completeness

One of the most interesting properties of Conway's Game of Life is its ability to support universal computation. Moving patterns called **gliders** can carry information across the grid and interact with other patterns.

By arranging these interactions carefully, Game of Life configurations can represent logical operations.

This project includes `logic_gates.py`, which is associated with exploring logic gates through interactions between Game of Life patterns, including:

- **AND gate:** Produces a true output only when both inputs are true.
- **NOT gate:** Produces the opposite of its input.

AND and NOT operations can be combined to represent more complex Boolean functions. Such constructions illustrate how a system governed by local cellular rules can express general-purpose computation.

### 4. Pattern Files and Visualization

The project contains pattern files that represent predefined cellular configurations. These patterns make it possible to explore well-known structures and observe how they evolve over successive generations.

The available visualization utilities include:

- `pygame_gol.py` — graphical visualization of Conway's Game of Life.
- `langton_pygame.py` — graphical visualization of Langton's Ant.
- `pygame_viewer.py` — a viewer for cellular automaton patterns.

The pattern collection includes examples of spaceships, oscillators, and glider-related structures. Pattern files use cellular pattern representations such as plaintext `.cells` and, where supported, Run Length Encoded (RLE) data.

## Project Structure

```text
Part 2 - GoL & Langton's Ant/
├── conway.py
├── langton.py
├── langton_pygame.py
├── logic_gates.py
├── pygame_gol.py
├── pygame_viewer.py
├── test_gameoflife_glider_simple.py
├── test_gameoflife_glider.py
├── test_gameoflife_glider_large.py
├── *.cells
└── README.md
```

## Running the Visualizations

Run the following commands from this directory, assuming the required dependencies are installed.

**Conway's Game of Life**

```bash
python pygame_gol.py
```

**Langton's Ant**

```bash
python langton_pygame.py
```

**Pattern Viewer**

```bash
python pygame_viewer.py
```

The graphical interfaces provide a way to observe cellular evolution and explore the behavior of different configurations.

## Technologies

- **Python 3** — implementation of the simulations and related utilities.
- **NumPy** — numerical arrays and grid-based data.
- **Pygame** — graphical visualization and interaction.
- **SciPy** — scientific computing utilities, where used by the simulation.

## Key Concepts

- **Cellular Automata:** Discrete systems whose states evolve according to local rules.
- **Emergence:** Complex global behavior arising from simple local interactions.
- **Determinism:** Systems whose evolution is determined by their current state and transition rules.
- **Pattern Formation:** The development of stable, repeating, or moving structures.
- **Computational Universality:** The ability of a computational system to represent general computation.
- **Boolean Logic:** Logical operations represented through interactions between cellular patterns.

## References and Further Reading

- Moore, C. and Mertens, S. (2011). *The Nature of Computation*. Oxford University Press.
- [LifeWiki](https://conwaylife.com/wiki/Main_Page) — a reference for Conway's Game of Life patterns and concepts.
- [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
- [Langton's Ant](https://en.wikipedia.org/wiki/Langton%27s_ant)

---

*This directory forms the cellular automata component of the Theory of Languages and Automata practical project.*
