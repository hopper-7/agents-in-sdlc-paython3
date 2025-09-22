"""
Unit tests for Sudoku Game functionality.
Tests all core game features including puzzle generation, validation, solving, and game mechanics.
"""

import unittest
import sys
import os
from typing import List, Dict, Any, Optional

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from sudoku_game import SudokuGame


class TestSudokuGame(unittest.TestCase):
    """Test cases for the SudokuGame class."""
    
    # Test data - valid and invalid Sudoku grids
    TEST_DATA: Dict[str, Any] = {
        "valid_complete_grid": [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ],
        "invalid_grid_row_duplicate": [
            [5, 3, 4, 6, 7, 8, 9, 1, 5],  # Row has duplicate 5
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ],
        "puzzle_with_solution": [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
    }
    
    def setUp(self) -> None:
        """Set up test environment with a fresh game instance."""
        self.game = SudokuGame()
    
    def tearDown(self) -> None:
        """Clean up after each test."""
        # No database cleanup needed for Sudoku game
        pass
    
    def test_initialization(self) -> None:
        """Test that SudokuGame initializes correctly."""
        self.assertEqual(len(self.game.grid), 9)
        self.assertEqual(len(self.game.grid[0]), 9)
        self.assertEqual(len(self.game.original_grid), 9)
        self.assertEqual(len(self.game.original_grid[0]), 9)
        
        # Grid should be empty initially
        for row in range(9):
            for col in range(9):
                self.assertEqual(self.game.grid[row][col], 0)
                self.assertEqual(self.game.original_grid[row][col], 0)
    
    def test_is_valid_move_success(self) -> None:
        """Test valid move detection with empty grid."""
        # Empty grid should allow any number in any position
        self.assertTrue(self.game.is_valid_move(0, 0, 1))
        self.assertTrue(self.game.is_valid_move(4, 4, 5))
        self.assertTrue(self.game.is_valid_move(8, 8, 9))
    
    def test_is_valid_move_row_conflict(self) -> None:
        """Test move validation with row conflicts."""
        # Place a number and test row conflict
        self.game.grid[0][0] = 5
        self.assertFalse(self.game.is_valid_move(0, 1, 5))  # Same row
        self.assertTrue(self.game.is_valid_move(3, 3, 5))   # Different row, different box
    
    def test_is_valid_move_column_conflict(self) -> None:
        """Test move validation with column conflicts."""
        # Place a number and test column conflict
        self.game.grid[0][0] = 5
        self.assertFalse(self.game.is_valid_move(1, 0, 5))  # Same column
        self.assertTrue(self.game.is_valid_move(3, 3, 5))   # Different column, different box
    
    def test_is_valid_move_box_conflict(self) -> None:
        """Test move validation with 3x3 box conflicts."""
        # Place a number and test box conflict
        self.game.grid[0][0] = 5
        self.assertFalse(self.game.is_valid_move(1, 1, 5))  # Same box
        self.assertTrue(self.game.is_valid_move(3, 3, 5))   # Different box
    
    def test_is_valid_solution_complete_valid(self) -> None:
        """Test validation of a complete valid Sudoku solution."""
        self.game.grid = self.TEST_DATA["valid_complete_grid"]
        self.assertTrue(self.game.is_valid_solution())
        self.assertTrue(self.game.is_complete())
    
    def test_is_valid_solution_invalid_grid(self) -> None:
        """Test validation of an invalid Sudoku grid."""
        self.game.grid = self.TEST_DATA["invalid_grid_row_duplicate"]
        self.assertFalse(self.game.is_valid_solution())
    
    def test_is_complete_incomplete_grid(self) -> None:
        """Test completion check on incomplete grid."""
        self.game.grid = self.TEST_DATA["puzzle_with_solution"]
        self.assertFalse(self.game.is_complete())
    
    def test_solve_solvable_puzzle(self) -> None:
        """Test solving a solvable puzzle."""
        self.game.grid = [row[:] for row in self.TEST_DATA["puzzle_with_solution"]]
        self.assertTrue(self.game.solve())
        self.assertTrue(self.game.is_complete())
        self.assertTrue(self.game.is_valid_solution())
    
    def test_solve_already_complete(self) -> None:
        """Test solving an already complete puzzle."""
        self.game.grid = [row[:] for row in self.TEST_DATA["valid_complete_grid"]]
        self.assertTrue(self.game.solve())
        self.assertTrue(self.game.is_complete())
    
    def test_make_move_valid(self) -> None:
        """Test making a valid move."""
        # Set up a puzzle state
        self.game.original_grid = [row[:] for row in self.TEST_DATA["puzzle_with_solution"]]
        self.game.grid = [row[:] for row in self.TEST_DATA["puzzle_with_solution"]]
        
        # Try to make a valid move in an empty cell
        self.assertTrue(self.game.make_move(0, 2, 4))
        self.assertEqual(self.game.grid[0][2], 4)
    
    def test_make_move_invalid_number(self) -> None:
        """Test making a move with invalid number."""
        self.game.original_grid = [row[:] for row in self.TEST_DATA["puzzle_with_solution"]]
        self.game.grid = [row[:] for row in self.TEST_DATA["puzzle_with_solution"]]
        
        # Invalid number range
        self.assertFalse(self.game.make_move(0, 2, 10))
        self.assertFalse(self.game.make_move(0, 2, -1))
    
    def test_make_move_original_cell(self) -> None:
        """Test attempting to modify original puzzle cells."""
        self.game.original_grid = [row[:] for row in self.TEST_DATA["puzzle_with_solution"]]
        self.game.grid = [row[:] for row in self.TEST_DATA["puzzle_with_solution"]]
        
        # Try to modify a cell that's part of the original puzzle
        self.assertFalse(self.game.make_move(0, 0, 7))  # Cell (0,0) has value 5 in original
        self.assertEqual(self.game.grid[0][0], 5)  # Should remain unchanged
    
    def test_make_move_clear_cell(self) -> None:
        """Test clearing a cell with 0."""
        self.game.original_grid = [row[:] for row in self.TEST_DATA["puzzle_with_solution"]]
        self.game.grid = [row[:] for row in self.TEST_DATA["puzzle_with_solution"]]
        
        # Place a number first
        self.game.make_move(0, 2, 4)
        self.assertEqual(self.game.grid[0][2], 4)
        
        # Clear it
        self.assertTrue(self.game.make_move(0, 2, 0))
        self.assertEqual(self.game.grid[0][2], 0)
    
    def test_make_move_sudoku_rule_violation(self) -> None:
        """Test making a move that violates Sudoku rules."""
        self.game.original_grid = [row[:] for row in self.TEST_DATA["puzzle_with_solution"]]
        self.game.grid = [row[:] for row in self.TEST_DATA["puzzle_with_solution"]]
        
        # Try to place a number that conflicts with existing numbers
        self.assertFalse(self.game.make_move(0, 2, 5))  # 5 already exists in row 0
    
    def test_generate_puzzle_different_difficulties(self) -> None:
        """Test puzzle generation with different difficulty levels."""
        difficulties = ['easy', 'medium', 'hard']
        
        for difficulty in difficulties:
            with self.subTest(difficulty=difficulty):
                self.game.generate_puzzle(difficulty)
                
                # Count empty cells
                empty_cells = sum(1 for row in range(9) for col in range(9) 
                                if self.game.grid[row][col] == 0)
                
                # Verify appropriate number of empty cells for difficulty
                expected_empty = self.game.difficulty_levels[difficulty]
                self.assertEqual(empty_cells, expected_empty)
                
                # Original grid should match current grid
                self.assertEqual(self.game.grid, self.game.original_grid)
    
    def test_generate_puzzle_invalid_difficulty(self) -> None:
        """Test puzzle generation with invalid difficulty defaults to medium."""
        self.game.generate_puzzle('invalid')
        
        empty_cells = sum(1 for row in range(9) for col in range(9) 
                        if self.game.grid[row][col] == 0)
        
        # Should default to medium difficulty
        self.assertEqual(empty_cells, self.game.difficulty_levels['medium'])
    
    def test_reset_to_original(self) -> None:
        """Test resetting game to original puzzle state."""
        # Generate a puzzle
        self.game.generate_puzzle('easy')
        original_state = [row[:] for row in self.game.grid]
        
        # Make some moves
        for row in range(9):
            for col in range(9):
                if self.game.grid[row][col] == 0:
                    # Try to place a valid number
                    for num in range(1, 10):
                        if self.game.is_valid_move(row, col, num):
                            self.game.make_move(row, col, num)
                            break
                    break
        
        # Grid should be different now
        self.assertNotEqual(self.game.grid, original_state)
        
        # Reset and verify
        self.game.reset_to_original()
        self.assertEqual(self.game.grid, original_state)
    
    def test_get_hint_available(self) -> None:
        """Test getting a hint when available."""
        self.game.grid = [row[:] for row in self.TEST_DATA["puzzle_with_solution"]]
        self.game.original_grid = [row[:] for row in self.TEST_DATA["puzzle_with_solution"]]
        
        hint = self.game.get_hint()
        self.assertIsNotNone(hint)
        
        if hint:
            row, col, num = hint
            # Verify hint is for an empty cell
            self.assertEqual(self.game.grid[row][col], 0)
            self.assertEqual(self.game.original_grid[row][col], 0)
            # Verify hint is valid
            self.assertTrue(self.game.is_valid_move(row, col, num))
    
    def test_get_hint_no_hint_available(self) -> None:
        """Test getting hint when none available (complete puzzle)."""
        self.game.grid = [row[:] for row in self.TEST_DATA["valid_complete_grid"]]
        self.game.original_grid = [row[:] for row in self.TEST_DATA["valid_complete_grid"]]
        
        hint = self.game.get_hint()
        self.assertIsNone(hint)
    
    def test_display_grid_format(self) -> None:
        """Test that display_grid returns properly formatted string."""
        display = self.game.display_grid()
        
        # Check that it's a string
        self.assertIsInstance(display, str)
        
        # Check that it contains expected elements
        self.assertIn("║", display)  # Box drawing characters
        self.assertIn("╔", display)  # Top border
        self.assertIn("╚", display)  # Bottom border
        
        # Check line count (header + borders + 9 rows + separators)
        lines = display.split('\n')
        self.assertEqual(len(lines), 14)  # Expected number of lines
    
    def test_generate_full_grid_validity(self) -> None:
        """Test that generate_full_grid creates a valid complete solution."""
        self.game.generate_full_grid()
        
        # Should be complete and valid
        self.assertTrue(self.game.is_complete())
        self.assertTrue(self.game.is_valid_solution())
        
        # Should have no empty cells
        empty_cells = sum(1 for row in range(9) for col in range(9) 
                        if self.game.grid[row][col] == 0)
        self.assertEqual(empty_cells, 0)


if __name__ == '__main__':
    unittest.main()