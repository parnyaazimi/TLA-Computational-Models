# -*- coding: utf-8 -*-
"""
Glider-based Logic Gates Student Template Module.

"""
import numpy as np
from conway import GameOfLife


class GliderLogicGates:
    """
    TODO: [Extension - Logic Gates]
    Instruct the student to:
    1. Initialize a grid and precisely place "Glider" streams (signals represented by gliders)
       such that their collision simulates:
       - An AND gate (produces a specific output pattern only when both inputs A and B are active).
       - A NOT gate (produces an output signal/glider only when input A is inactive).
    2. Prove the Turing completeness of Conway's Game of Life by demonstrating these logic gates.
    """
    def __init__(self):
        # glider shapes: down-right and its mirror (down-left)
        self.se_glider = [(0,1),(1, 2),(2 , 0),(2 , 1),(2 , 2)]
        self.sw_glider = [(r,2-c) for r,c in self.se_glider]

        # AND gate params
        self.and_a = (11,8)
        self.and_b = (8,15)
        self.and_out = (13,18,9,14)
        self.and_steps = 60

        # NOT gate params
        self.not_ctrl = (11,11)
        self.not_a = (9,17)
        self.not_out = (20,27,20,27)
        self.not_steps = 40

    # Helper method to place a glider on the board
    def add_glider(self , board ,shape,pos, val):
        row,col= pos
        for r,c in shape:
            board[row+r , col+c]= val


    def setup_and_gate(self, grid_size=35, input_a_present=False, input_b_present=False):
        """
        Set up the Game of Life grid for an AND gate.
        
        Args:
            grid_size (int): Size of the simulation grid.
            input_a_present (bool): If True, place glider for Input A.
            input_b_present (bool): If True, place glider for Input B.
            
        Returns:
            GameOfLife: Initialized GameOfLife object.
        """
        # Student TODO: Setup glider(s) on the grid
        life = GameOfLife(N=grid_size,finite=True,fastMode=True)

        if input_a_present:
            self.add_glider(life.grid,self.se_glider,self.and_a,life.aliveValue)
            
        if input_b_present:
            self.add_glider(life.grid,self.sw_glider,self.and_b, life.aliveValue)

        return life

    def setup_not_gate(self, grid_size=35, input_a_present=False):
        """
        Set up the Game of Life grid for a NOT gate.
        
        Args:
            grid_size (int): Size of the simulation grid.
            input_a_present (bool): If True, place glider for Input A.
            
        Returns:
            GameOfLife: Initialized GameOfLife object.
        """
        # Student TODO: Setup control glider and input glider(s)
        life = GameOfLife(N=grid_size,finite=True,fastMode=True)

        self.add_glider(life.grid, self.se_glider , self.not_ctrl , life.aliveValue)

        if input_a_present:
            self.add_glider(life.grid , self.sw_glider , self.not_a , life.aliveValue)

        return life

    def run_and_gate(self, input_a_present, input_b_present):
        """
        Run the AND gate simulation for a specific number of steps and return the output.
        
        Args:
            input_a_present (bool): Input A state.
            input_b_present (bool): Input B state.
            
        Returns:
            bool: True if output is active (e.g. glider/block formed in output region), False otherwise.
        """
        # Student TODO: Evolve simulation and evaluate output
        life = self.setup_and_gate(35 , input_a_present , input_b_present)

        for _ in range(self.and_steps):
            life.evolve()

        r0,r1,c0,c1 = self.and_out
        output_region = life.grid[r0:r1 , c0:c1]

        if np.sum(output_region) !=4:
            return False

        next_grid = life.update_grid_fast(life.grid)
        next_region = next_grid[r0:r1 , c0:c1]

        return np.array_equal(next_region, output_region)

    def run_not_gate(self, input_a_present):
        """
        Run the NOT gate simulation for a specific number of steps and return the output.
        
        Args:
            input_a_present (bool): Input A state.
            
        Returns:
            bool: True if output is active, False otherwise.
        """
        # Student TODO: Evolve simulation and evaluate output
        life = self.setup_not_gate(35 , input_a_present)

        for _ in range(self.not_steps):
            life.evolve()

        r0,r1,c0,c1 = self.not_out
        output_region = life.grid[r0:r1 , c0:c1]

        return np.sum(output_region)> 0
