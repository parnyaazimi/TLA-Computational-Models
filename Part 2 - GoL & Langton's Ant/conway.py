"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

"""
import numpy as np
from scipy import signal, ndimage


def parse_pattern(filepath):
    """
    TODO: [Part 1d - RLE/Plaintext Parser]
    Write a parser for Run Length Encoded (RLE) or Plaintext (.cells) patterns
    so grids larger than 20x20 can be loaded.
    
    Args:
        filepath (str): Path to the pattern file.
        
    Returns:
        tuple: (width, height, list of (r, c) offsets of live cells)
    """
    # Student TODO: Implement parser here
    live_cells = []
    width = 0
    height = 0
    
    with open(filepath, 'r') as f:
        content = f.read()

    lines = content.strip().split('\n')

    header_line = None
    for line in lines:
        line = line.strip()
        if line.startswith('x ='):
            header_line = line
            break

    if header_line is not None:  # RLE
        parts = header_line.split(',')
        for part in parts:
            part = part.strip()
            if part.startswith('x ='):
                width = int(part.split('=')[1].strip())
            elif part.startswith('y ='):
                height = int(part.split('=')[1].strip())
        
        rle_string = ''
        for line in lines:
            if not line.startswith('x =') and not line.startswith('#'):
                rle_string += line.strip()
        rle_string = rle_string.replace(' ', '')
        
        row = 0
        col = 0
        i = 0
        while i < len(rle_string):
            if rle_string[i] == '!':
                break
            
            count = 0
            while i < len(rle_string) and rle_string[i].isdigit():
                count = count * 10 + int(rle_string[i])
                i += 1
            
            if i >= len(rle_string):
                break
            
            char = rle_string[i]
            i += 1
            
            if count == 0:
                count = 1
            
            if char == 'b':
                col += count
            elif char == 'o':
                for _ in range(count):
                    live_cells.append((row, col))
                    col += 1
            elif char == '$':
                row += count
                col = 0
    

    else:   #Plaintext
        lines = content.strip().split('\n')
        data_lines = []
        for line in lines:
            if not line.startswith('!'):
                data_lines.append(line.rstrip())
        
        height = len(data_lines)
        width = max(len(line) for line in data_lines) if data_lines else 0
        
        for r, line in enumerate(data_lines):
            for c, char in enumerate(line):
                if char == 'O' or char == 'o':
                    live_cells.append((r, c))
    
    return width, height, live_cells     



class GameOfLife:
    """
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    """

    def __init__(self, N=256, finite=False, fastMode=True):
        self.grid = np.zeros((N, N), np.uint)
        self.neighborhood = np.ones((3, 3), np.uint)  # 8 connected kernel
        self.neighborhood[1, 1] = 0  # do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0
        self.rows = N  # use for slow implementation of evolve
        self.cols = N  # use for slow implementation of evolve

    def getStates(self):
        """
        Returns the current states of the cells
        """
        return self.getGrid()

    def getGrid(self):
        """
        Same as getStates()
        """
        return self.grid
        

    def update_grid_fast(self, grid):
        """
        TODO: [Part 1e - Fast Convolution]
        Use scipy.signal.convolve2d (or similar) to compute neighbor weights
        rapidly for large grids (N > 1024).
        
        Args:
            grid (np.ndarray): The current 2D grid of states.
            
        Returns:
            np.ndarray: The next 2D grid of states.
        """
        # Student TODO: Implement fast 2D convolution method
        
        if self.finite:
            neighbor_count = signal.convolve2d(grid, self.neighborhood, mode='same', boundary='fill', fillvalue=0)
        else:
            neighbor_count = signal.convolve2d(grid, self.neighborhood, mode='same', boundary='wrap')
        
        
        survival = (grid == self.aliveValue) & ((neighbor_count == 2) | (neighbor_count == 3))
        birth = (grid == self.deadValue) & (neighbor_count == 3)
        
        new_grid = np.where(survival | birth, self.aliveValue, self.deadValue)
        return new_grid.astype(np.uint8)
        

    def evolve(self):
        """
        Given the current states of the cells, apply the GoL rules:
        - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        """
        if self.fastMode:
            self.grid = self.update_grid_fast(self.grid)
        else:
            # TODO: [Part 1a - Core Rules]
            # Remove the transition logic and implement the 4 standard GoL rules
            # (Underpopulation, Survival, Overpopulation, Reproduction) by iterating 
            # through the cells cell-by-cell. Handle self.finite wrapping appropriately.
            
            # Student TODO: Implement slow update cell-by-cell logic here
            N = self.rows
            new_grid = np.zeros((N, N), np.uint)

            for i in range(N):
                for j in range(N):
                    live_neighbors = 0                    
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if di == 0 and dj == 0:
                                continue 
                            ni = i + di
                            nj = j + dj                            
                            if self.finite:
                                if 0 <= ni < N and 0 <= nj < N:
                                    live_neighbors += self.grid[ni, nj]
                            else:
                                ni = ni % N
                                nj = nj % N
                                live_neighbors += self.grid[ni, nj]
                    current_cell = self.grid[i, j]                    
                    if current_cell == self.aliveValue: 
                        if live_neighbors < 2:
                            new_grid[i, j] = self.deadValue

                        elif live_neighbors == 2 or live_neighbors == 3:
                            new_grid[i, j] = self.aliveValue
                        else:  
                            new_grid[i, j] = self.deadValue
                    else:
                        if live_neighbors == 3:
                            new_grid[i, j] = self.aliveValue
                        else:
                            new_grid[i, j] = self.deadValue
            
            self.grid = new_grid


    def insertBlinker(self, index=(0, 0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid[index[0], index[1] + 1] = self.aliveValue
        self.grid[index[0] + 1, index[1] + 1] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 1] = self.aliveValue

    def insertGlider(self, index=(0, 0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0], index[1] + 1] = self.aliveValue
        self.grid[index[0] + 1, index[1] + 2] = self.aliveValue
        self.grid[index[0] + 2, index[1]] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 1] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 2] = self.aliveValue

    def insertGliderGun(self, index=(0, 0)):
        '''
        TODO: [Part 1c - Glider Gun Fix]
        The current glider gun pattern is broken. Leave the broken array in the code 
        and instruct the student to debug and fix the coordinates so it loops infinitely.
        '''
        self.grid[index[0] + 1, index[1] + 26] = self.aliveValue

        self.grid[index[0] + 2, index[1] + 24] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 26] = self.aliveValue

        self.grid[index[0] + 3, index[1] + 14] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 15] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 22] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 23] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 36] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 37] = self.aliveValue

        self.grid[index[0] + 4, index[1] + 13] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 17] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 22] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 23] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 36] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 37] = self.aliveValue

        # self.grid[index[0] + 5, index[1] + 1 + 1] = self.aliveValue
        # self.grid[index[0] + 5, index[1] + 2 + 1] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 2] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 3] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 12] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 18] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 22] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 23] = self.aliveValue

        # self.grid[index[0] + 6, index[1] + 1 + 1] = self.aliveValue
        # self.grid[index[0] + 6, index[1] + 2 + 1] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 2] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 3] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 12] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 16] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 18] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 19] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 24] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 26] = self.aliveValue

        self.grid[index[0] + 7, index[1] + 12] = self.aliveValue
        self.grid[index[0] + 7, index[1] + 18] = self.aliveValue
        self.grid[index[0] + 7, index[1] + 26] = self.aliveValue

        self.grid[index[0] + 8, index[1] + 13] = self.aliveValue
        self.grid[index[0] + 8, index[1] + 17] = self.aliveValue

        self.grid[index[0] + 9, index[1] + 14] = self.aliveValue
        self.grid[index[0] + 9, index[1] + 15] = self.aliveValue

    def insertFromFile(self, filename, index=((0, 0))):
        '''
        Insert cells from pattern file using parse_pattern
        '''
        width, height, live_cells = parse_pattern(filename)
        for r, c in live_cells:
            target_r = index[0] + r
            target_c = index[1] + c
            if 0 <= target_r < self.rows and 0 <= target_c < self.cols:
                self.grid[target_r, target_c] = self.aliveValue
