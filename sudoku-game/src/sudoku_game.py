"""
Sudoku Game Implementation
A complete Sudoku game with generator, solver, and validation functionality.
This module provides the core game logic for a console-based Sudoku experience.
"""

import random
import copy
from typing import List, Tuple, Optional


class SudokuGame:
    """
    A Sudoku game implementation with puzzle generation, solving, and validation.
    
    This class handles all aspects of a Sudoku game including:
    - Puzzle generation with different difficulty levels
    - Game validation and rule checking
    - Solving algorithms
    - Player interaction and game state management
    """
    
    def __init__(self) -> None:
        """Initialize a new Sudoku game with an empty 9x9 grid."""
        self.grid: List[List[int]] = [[0 for _ in range(9)] for _ in range(9)]
        self.original_grid: List[List[int]] = [[0 for _ in range(9)] for _ in range(9)]
        self.difficulty_levels = {
            'easy': 40,      # 40 numbers removed (41 remaining)
            'medium': 50,    # 50 numbers removed (31 remaining)
            'hard': 60       # 60 numbers removed (21 remaining)
        }
    
    def is_valid_move(self, row: int, col: int, num: int) -> bool:
        """
        Check if placing a number at the given position is valid according to Sudoku rules.
        
        Args:
            row: Row index (0-8)
            col: Column index (0-8)
            num: Number to place (1-9)
            
        Returns:
            True if the move is valid, False otherwise
        """
        # Check row constraint
        for c in range(9):
            if self.grid[row][c] == num:
                return False
        
        # Check column constraint
        for r in range(9):
            if self.grid[r][col] == num:
                return False
        
        # Check 3x3 box constraint
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if self.grid[r][c] == num:
                    return False
        
        return True
    
    def solve(self) -> bool:
        """
        Solve the current Sudoku puzzle using backtracking algorithm.
        
        Returns:
            True if puzzle is solvable, False otherwise
        """
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid_move(row, col, num):
                            self.grid[row][col] = num
                            if self.solve():
                                return True
                            self.grid[row][col] = 0
                    return False
        return True
    
    def generate_full_grid(self) -> None:
        """Generate a complete valid Sudoku grid using randomized solving."""
        # Start with empty grid
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        
        # Fill diagonal 3x3 boxes first (they don't interfere with each other)
        for box in range(0, 9, 3):
            self._fill_box(box, box)
        
        # Fill remaining cells
        self.solve()
    
    def _fill_box(self, row: int, col: int) -> None:
        """Fill a 3x3 box with random numbers 1-9."""
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        
        for i in range(3):
            for j in range(3):
                self.grid[row + i][col + j] = numbers[i * 3 + j]
    
    def generate_puzzle(self, difficulty: str = 'medium') -> None:
        """
        Generate a new Sudoku puzzle with the specified difficulty.
        
        Args:
            difficulty: Difficulty level ('easy', 'medium', or 'hard')
        """
        if difficulty not in self.difficulty_levels:
            difficulty = 'medium'
        
        # Generate a complete grid
        self.generate_full_grid()
        
        # Store the complete solution
        solution = copy.deepcopy(self.grid)
        
        # Remove numbers to create puzzle
        cells_to_remove = self.difficulty_levels[difficulty]
        cells = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(cells)
        
        for r, c in cells[:cells_to_remove]:
            self.grid[r][c] = 0
        
        # Store original puzzle state
        self.original_grid = copy.deepcopy(self.grid)
    
    def make_move(self, row: int, col: int, num: int) -> bool:
        """
        Make a move on the game board if valid.
        
        Args:
            row: Row index (0-8)
            col: Column index (0-8)
            num: Number to place (1-9, or 0 to clear)
            
        Returns:
            True if move was made successfully, False otherwise
        """
        # Check if position is modifiable (not part of original puzzle)
        if self.original_grid[row][col] != 0:
            return False
        
        # Clear cell if num is 0
        if num == 0:
            self.grid[row][col] = 0
            return True
        
        # Validate move
        if num < 1 or num > 9:
            return False
        
        # Temporarily place the number to check validity
        old_value = self.grid[row][col]
        self.grid[row][col] = 0  # Clear cell first for validation
        
        if self.is_valid_move(row, col, num):
            self.grid[row][col] = num
            return True
        else:
            self.grid[row][col] = old_value
            return False
    
    def is_complete(self) -> bool:
        """
        Check if the puzzle is completely and correctly filled.
        
        Returns:
            True if puzzle is complete and valid, False otherwise
        """
        # Check if all cells are filled
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return False
        
        # Check if solution is valid
        return self.is_valid_solution()
    
    def is_valid_solution(self) -> bool:
        """
        Check if the current grid state represents a valid Sudoku solution.
        
        Returns:
            True if the solution is valid, False otherwise
        """
        # Check all rows
        for row in range(9):
            if not self._is_valid_unit([self.grid[row][col] for col in range(9)]):
                return False
        
        # Check all columns
        for col in range(9):
            if not self._is_valid_unit([self.grid[row][col] for row in range(9)]):
                return False
        
        # Check all 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_numbers = []
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        box_numbers.append(self.grid[r][c])
                if not self._is_valid_unit(box_numbers):
                    return False
        
        return True
    
    def _is_valid_unit(self, numbers: List[int]) -> bool:
        """Check if a list of 9 numbers contains exactly 1-9 with no duplicates."""
        return sorted(numbers) == list(range(1, 10))
    
    def get_hint(self) -> Optional[Tuple[int, int, int]]:
        """
        Get a hint for the next move.
        
        Returns:
            Tuple of (row, col, number) for a valid move, or None if no hint available
        """
        # Create a copy of the grid to solve
        temp_grid = copy.deepcopy(self.grid)
        temp_game = SudokuGame()
        temp_game.grid = temp_grid
        
        # Try to solve and find the first difference
        if temp_game.solve():
            for row in range(9):
                for col in range(9):
                    if (self.grid[row][col] == 0 and 
                        temp_game.grid[row][col] != 0 and
                        self.original_grid[row][col] == 0):
                        return (row, col, temp_game.grid[row][col])
        
        return None
    
    def reset_to_original(self) -> None:
        """Reset the game to the original puzzle state."""
        self.grid = copy.deepcopy(self.original_grid)
    
    def display_grid(self) -> str:
        """
        Create a formatted string representation of the Sudoku grid.
        
        Returns:
            Formatted string showing the current game state
        """
        result = []
        result.append("    1 2 3   4 5 6   7 8 9")
        result.append("  ╔═══════╦═══════╦═══════╗")
        
        for row in range(9):
            if row == 3 or row == 6:
                result.append("  ╠═══════╬═══════╬═══════╣")
            
            line = f"{row + 1} ║ "
            for col in range(9):
                if col == 3 or col == 6:
                    line += "│ "
                
                cell_value = self.grid[row][col]
                if cell_value == 0:
                    line += "· "
                else:
                    # Highlight original numbers differently
                    if self.original_grid[row][col] != 0:
                        line += f"{cell_value} "
                    else:
                        line += f"{cell_value} "
                
                if col == 8:
                    line += "║"
            
            result.append(line)
        
        result.append("  ╚═══════╩═══════╩═══════╝")
        return "\n".join(result)