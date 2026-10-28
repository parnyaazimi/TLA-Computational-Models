# -*- coding: utf-8 -*-
"""
Langton's Ant Student Template Module.
"""
import numpy as np


class LangtonsAnt:
    """
    TODO: [Part 2 - Langton's Ant]
    Create the LangtonsAnt class.
    
    Instruct students to:
    1. Implement the core rules:
       - If on a white square, toggle the color of the square and turn 90 degrees clockwise ('R'), then move forward one unit.
       - If on a black square, toggle the color of the square and turn 90 degrees counter-clockwise ('L'), then move forward one unit.
    2. Extend it to handle multi-color states (representing rulesets like RLR, LLRR, LRRRRRLLR, etc.).
       - A ruleset dictionary maps: {current_color: (next_color, turn_direction)}
       - Where turn_direction is 'R' or 'L'.
    3. Ensure wrapping at the boundaries (toroidal grid).
    """

    def __init__(self, N, ant_position, rules):
        """
        Initialize the Langton's Ant simulation.
        
        Args:
            N (int): The grid size (NxN).
            ant_position (tuple): Starting coordinate of the ant as (r, c).
            rules (dict): Dictionary defining transition rules.
                          Format: {current_color: (next_color, turn_direction)}
        """
        # Student TODO: Implement initialization
        self.N = N
        self.r, self.c = ant_position
        self.rules = rules
        self.grid = np.zeros((N, N), dtype=int)
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.current_direction = 0

    def get_states(self):
        """
        Returns the current state grid of the cells.
        
        Returns:
            np.ndarray: The NxN cellular grid.
        """
        # Student TODO: Return grid state
        return self.grid

    def get_current_position(self):
        """
        Returns the ant's current position as a tuple (r, c).
        
        Returns:
            tuple: Current coordinates of the ant.
        """
        # Student TODO: Return current position
        return (self.r, self.c)

    def step(self):
        """
        Perform a single simulation step following the ruleset.
        """
        # Student TODO: Implement the ant's movement and cell state updates
        current_color = self.grid[self.r, self.c]
        if current_color not in self.rules:
            return
        next_color, turn_direction = self.rules[current_color]
        self.grid[self.r, self.c] = next_color
        if turn_direction == 'R':
            self.current_direction = (self.current_direction + 1) % 4
        elif turn_direction == 'L':
            self.current_direction = (self.current_direction - 1) % 4
        dr, dc = self.directions[self.current_direction]
        self.r = self.r + dr
        self.c = self.c + dc
        self.r = self.r % self.N
        self.c = self.c % self.N


    def update(self):
        """
        Alias for step() to support standard animation.
        """
        self.step()
