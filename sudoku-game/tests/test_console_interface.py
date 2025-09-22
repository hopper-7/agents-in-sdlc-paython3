"""
Unit tests for Sudoku Console Interface.
Tests console command parsing, user interaction, and interface functionality.
"""

import unittest
import sys
import os
from unittest.mock import patch, MagicMock
from io import StringIO
from typing import List, Dict, Any, Optional

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from console_interface import SudokuConsole
from sudoku_game import SudokuGame


class TestSudokuConsole(unittest.TestCase):
    """Test cases for the SudokuConsole class."""
    
    # Test data for console commands
    TEST_DATA: Dict[str, Any] = {
        "valid_commands": [
            ("move 1 1 5", ("move", ["1", "1", "5"])),
            ("clear 3 4", ("clear", ["3", "4"])),
            ("hint", ("hint", [])),
            ("reset", ("reset", [])),
            ("new easy", ("new", ["easy"])),
            ("quit", ("quit", []))
        ],
        "invalid_commands": [
            "",
            "   ",
            "invalid",
            "move",
            "move 1",
            "move 1 2",
            "clear",
            "clear 1"
        ]
    }
    
    def setUp(self) -> None:
        """Set up test environment with a fresh console instance."""
        self.console = SudokuConsole()
        # Use a simple puzzle for testing
        self.console.game.grid = [
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
        self.console.game.original_grid = [row[:] for row in self.console.game.grid]
    
    def tearDown(self) -> None:
        """Clean up after each test."""
        pass
    
    def test_initialization(self) -> None:
        """Test that SudokuConsole initializes correctly."""
        self.assertIsInstance(self.console.game, SudokuGame)
        self.assertTrue(self.console.running)
    
    def test_parse_command_valid(self) -> None:
        """Test parsing valid commands."""
        for command_str, expected in self.TEST_DATA["valid_commands"]:
            with self.subTest(command=command_str):
                result = self.console.parse_command(command_str)
                self.assertIsNotNone(result)
                action, args = result
                expected_action, expected_args = expected
                self.assertEqual(action, expected_action)
                self.assertEqual(args, expected_args)
    
    def test_parse_command_invalid(self) -> None:
        """Test parsing invalid commands."""
        for command_str in self.TEST_DATA["invalid_commands"]:
            with self.subTest(command=command_str):
                result = self.console.parse_command(command_str)
                if command_str.strip():  # Non-empty commands should return something
                    if result:
                        action, args = result
                        # Commands with missing args are still parsed but handled later
                        self.assertIsInstance(action, str)
                        self.assertIsInstance(args, list)
                else:  # Empty commands should return None
                    self.assertIsNone(result)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_move_command_valid(self, mock_stdout: StringIO) -> None:
        """Test handling valid move commands."""
        # Test valid move
        self.console.handle_move_command(["1", "3", "4"])
        output = mock_stdout.getvalue()
        self.assertIn("✅", output)  # Success indicator
        self.assertEqual(self.console.game.grid[0][2], 4)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_move_command_invalid_format(self, mock_stdout: StringIO) -> None:
        """Test handling move commands with invalid format."""
        # Too few arguments
        self.console.handle_move_command(["1", "2"])
        output = mock_stdout.getvalue()
        self.assertIn("❌", output)  # Error indicator
        self.assertIn("格式錯誤", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_move_command_invalid_range(self, mock_stdout: StringIO) -> None:
        """Test handling move commands with out-of-range values."""
        # Row out of range
        self.console.handle_move_command(["10", "1", "5"])
        output = mock_stdout.getvalue()
        self.assertIn("❌", output)
        self.assertIn("行列必須在1-9之間", output)
        
        # Number out of range
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        self.console.handle_move_command(["1", "1", "10"])
        output = mock_stdout.getvalue()
        self.assertIn("❌", output)
        self.assertIn("數字必須在1-9之間", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_move_command_original_cell(self, mock_stdout: StringIO) -> None:
        """Test handling move commands on original puzzle cells."""
        # Try to modify an original cell (0,0 has value 5)
        self.console.handle_move_command(["1", "1", "7"])
        output = mock_stdout.getvalue()
        self.assertIn("❌", output)
        self.assertIn("不能修改原始謎題的數字", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_move_command_rule_violation(self, mock_stdout: StringIO) -> None:
        """Test handling move commands that violate Sudoku rules."""
        # Try to place 5 in row 0 (already has 5)
        self.console.handle_move_command(["1", "3", "5"])
        output = mock_stdout.getvalue()
        self.assertIn("❌", output)
        self.assertIn("無效的移動", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_clear_command_valid(self, mock_stdout: StringIO) -> None:
        """Test handling valid clear commands."""
        # First place a number, then clear it
        self.console.game.make_move(0, 2, 4)
        self.console.handle_clear_command(["1", "3"])
        output = mock_stdout.getvalue()
        self.assertIn("✅", output)
        self.assertEqual(self.console.game.grid[0][2], 0)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_clear_command_invalid_format(self, mock_stdout: StringIO) -> None:
        """Test handling clear commands with invalid format."""
        self.console.handle_clear_command(["1"])
        output = mock_stdout.getvalue()
        self.assertIn("❌", output)
        self.assertIn("格式錯誤", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_clear_command_original_cell(self, mock_stdout: StringIO) -> None:
        """Test handling clear commands on original puzzle cells."""
        self.console.handle_clear_command(["1", "1"])
        output = mock_stdout.getvalue()
        self.assertIn("❌", output)
        self.assertIn("不能清除原始謎題的數字", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_hint_command(self, mock_stdout: StringIO) -> None:
        """Test handling hint commands."""
        self.console.handle_hint_command()
        output = mock_stdout.getvalue()
        # Should either show a hint or say no hint available
        self.assertTrue("💡" in output or "❌" in output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_new_game_command_valid(self, mock_stdout: StringIO) -> None:
        """Test handling new game commands with valid difficulty."""
        original_grid = [row[:] for row in self.console.game.grid]
        self.console.handle_new_game_command(["easy"])
        output = mock_stdout.getvalue()
        self.assertIn("✅", output)
        # Grid should be different after generating new puzzle
        self.assertNotEqual(self.console.game.grid, original_grid)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_new_game_command_invalid_difficulty(self, mock_stdout: StringIO) -> None:
        """Test handling new game commands with invalid difficulty."""
        self.console.handle_new_game_command(["invalid"])
        output = mock_stdout.getvalue()
        self.assertIn("❌", output)
        self.assertIn("難度必須是", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_new_game_command_default_difficulty(self, mock_stdout: StringIO) -> None:
        """Test handling new game commands with no difficulty specified."""
        original_grid = [row[:] for row in self.console.game.grid]
        self.console.handle_new_game_command([])
        output = mock_stdout.getvalue()
        self.assertIn("✅", output)
        # Should use medium difficulty by default
        self.assertNotEqual(self.console.game.grid, original_grid)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_reset_command(self, mock_stdout: StringIO) -> None:
        """Test handling reset commands."""
        # Make a move first
        self.console.game.make_move(0, 2, 4)
        original_state = [row[:] for row in self.console.game.original_grid]
        
        self.console.handle_reset_command()
        output = mock_stdout.getvalue()
        self.assertIn("🔄", output)
        self.assertEqual(self.console.game.grid, original_state)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_game_status(self, mock_stdout: StringIO) -> None:
        """Test displaying game status."""
        self.console.display_game_status()
        output = mock_stdout.getvalue()
        
        # Should contain grid display
        self.assertIn("║", output)
        self.assertIn("╔", output)
        
        # Should contain cell count
        self.assertIn("已填入", output)
        self.assertIn("Filled", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_game_status_complete(self, mock_stdout: StringIO) -> None:
        """Test displaying game status when puzzle is complete."""
        # Set up a complete puzzle
        complete_grid = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        self.console.game.grid = complete_grid
        
        self.console.display_game_status()
        output = mock_stdout.getvalue()
        
        # Should show completion message
        self.assertIn("🎉", output)
        self.assertIn("恭喜", output)
        self.assertIn("Congratulations", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_welcome(self, mock_stdout: StringIO) -> None:
        """Test displaying welcome message."""
        self.console.display_welcome()
        output = mock_stdout.getvalue()
        
        # Should contain welcome message
        self.assertIn("歡迎來到數獨遊戲", output)
        self.assertIn("Welcome to Sudoku", output)
        
        # Should contain game rules
        self.assertIn("遊戲規則", output)
        self.assertIn("Game Rules", output)
        
        # Should contain commands
        self.assertIn("指令", output)
        self.assertIn("Commands", output)
    
    @patch('os.system')
    def test_clear_screen(self, mock_system: MagicMock) -> None:
        """Test screen clearing functionality."""
        self.console.clear_screen()
        mock_system.assert_called_once()
        
        # Should call appropriate clear command
        call_args = mock_system.call_args[0][0]
        self.assertTrue(call_args in ['cls', 'clear'])


if __name__ == '__main__':
    unittest.main()