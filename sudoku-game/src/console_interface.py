"""
Sudoku Game Console Interface
Console-based user interface for playing Sudoku games.
This module provides an interactive command-line interface for the Sudoku game.
"""

import os
import sys
from typing import Optional, Tuple
from sudoku_game import SudokuGame


class SudokuConsole:
    """
    Console interface for the Sudoku game.
    
    Provides a text-based user interface for playing Sudoku with commands
    for making moves, getting hints, and managing the game state.
    """
    
    def __init__(self) -> None:
        """Initialize the console interface."""
        self.game = SudokuGame()
        self.running = True
    
    def clear_screen(self) -> None:
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_welcome(self) -> None:
        """Display the welcome message and game instructions."""
        print("🔢 歡迎來到數獨遊戲! Welcome to Sudoku Game! 🔢")
        print("=" * 50)
        print()
        print("遊戲規則 Game Rules:")
        print("• 在9x9的格子中填入1-9的數字")
        print("• 每行、每列、每個3x3的方格都不能有重複數字")
        print("• Fill numbers 1-9 in each row, column, and 3x3 box without repetition")
        print()
        print("指令 Commands:")
        print("• move <row> <col> <number> - 在指定位置放置數字 (例: move 1 1 5)")
        print("• clear <row> <col> - 清除指定位置的數字")
        print("• hint - 獲得提示")
        print("• reset - 重置到原始謎題")
        print("• new [difficulty] - 開始新遊戲 (easy/medium/hard)")
        print("• quit - 退出遊戲")
        print("=" * 50)
        print()
    
    def display_game_status(self) -> None:
        """Display current game state and statistics."""
        print(self.game.display_grid())
        print()
        
        # Count filled cells
        filled_cells = sum(1 for row in range(9) for col in range(9) 
                          if self.game.grid[row][col] != 0)
        print(f"已填入: {filled_cells}/81 個數字 | Filled: {filled_cells}/81 cells")
        
        if self.game.is_complete():
            print("🎉 恭喜！您完成了數獨謎題！ Congratulations! You solved the puzzle! 🎉")
        print()
    
    def parse_command(self, command: str) -> Optional[Tuple[str, list]]:
        """
        Parse user input command.
        
        Args:
            command: Raw command string from user
            
        Returns:
            Tuple of (action, arguments) or None if invalid
        """
        parts = command.strip().lower().split()
        if not parts:
            return None
        
        action = parts[0]
        args = parts[1:]
        
        return (action, args)
    
    def handle_move_command(self, args: list) -> None:
        """
        Handle move command to place a number on the grid.
        
        Args:
            args: List containing [row, col, number]
        """
        if len(args) != 3:
            print("❌ 格式錯誤。使用: move <行> <列> <數字> | Invalid format. Use: move <row> <col> <number>")
            return
        
        try:
            row = int(args[0]) - 1  # Convert to 0-based index
            col = int(args[1]) - 1  # Convert to 0-based index
            num = int(args[2])
            
            if not (0 <= row <= 8 and 0 <= col <= 8):
                print("❌ 行列必須在1-9之間 | Row and column must be between 1-9")
                return
            
            if not (1 <= num <= 9):
                print("❌ 數字必須在1-9之間 | Number must be between 1-9")
                return
            
            if self.game.make_move(row, col, num):
                print(f"✅ 在位置 ({row + 1}, {col + 1}) 放置了數字 {num}")
            else:
                if self.game.original_grid[row][col] != 0:
                    print("❌ 不能修改原始謎題的數字 | Cannot modify original puzzle numbers")
                else:
                    print("❌ 無效的移動！這個數字違反了數獨規則 | Invalid move! This violates Sudoku rules")
        
        except ValueError:
            print("❌ 請輸入有效的數字 | Please enter valid numbers")
    
    def handle_clear_command(self, args: list) -> None:
        """
        Handle clear command to remove a number from the grid.
        
        Args:
            args: List containing [row, col]
        """
        if len(args) != 2:
            print("❌ 格式錯誤。使用: clear <行> <列> | Invalid format. Use: clear <row> <col>")
            return
        
        try:
            row = int(args[0]) - 1
            col = int(args[1]) - 1
            
            if not (0 <= row <= 8 and 0 <= col <= 8):
                print("❌ 行列必須在1-9之間 | Row and column must be between 1-9")
                return
            
            if self.game.make_move(row, col, 0):
                print(f"✅ 清除了位置 ({row + 1}, {col + 1}) 的數字")
            else:
                print("❌ 不能清除原始謎題的數字 | Cannot clear original puzzle numbers")
        
        except ValueError:
            print("❌ 請輸入有效的數字 | Please enter valid numbers")
    
    def handle_hint_command(self) -> None:
        """Handle hint command to provide a suggestion."""
        hint = self.game.get_hint()
        if hint:
            row, col, num = hint
            print(f"💡 提示: 試試在位置 ({row + 1}, {col + 1}) 放置數字 {num}")
            print(f"💡 Hint: Try placing {num} at position ({row + 1}, {col + 1})")
        else:
            print("❌ 無法提供提示 | No hint available")
    
    def handle_new_game_command(self, args: list) -> None:
        """
        Handle new game command with optional difficulty.
        
        Args:
            args: List containing optional difficulty level
        """
        difficulty = 'medium'  # default
        if args:
            difficulty = args[0].lower()
            if difficulty not in ['easy', 'medium', 'hard']:
                print("❌ 難度必須是: easy, medium, hard | Difficulty must be: easy, medium, hard")
                return
        
        print(f"🎮 生成新的{difficulty}難度謎題... | Generating new {difficulty} puzzle...")
        self.game.generate_puzzle(difficulty)
        print("✅ 新謎題已生成！ | New puzzle generated!")
    
    def handle_reset_command(self) -> None:
        """Handle reset command to restore original puzzle state."""
        self.game.reset_to_original()
        print("🔄 已重置到原始謎題 | Reset to original puzzle")
    
    def run(self) -> None:
        """Run the main game loop."""
        self.clear_screen()
        self.display_welcome()
        
        # Generate initial puzzle
        print("🎮 生成中等難度謎題... | Generating medium difficulty puzzle...")
        self.game.generate_puzzle('medium')
        print("✅ 謎題已生成！開始遊戲吧！ | Puzzle generated! Let's start playing!")
        print()
        
        while self.running:
            self.display_game_status()
            
            if self.game.is_complete():
                play_again = input("🎯 想要開始新遊戲嗎？(y/n) | Play again? (y/n): ").strip().lower()
                if play_again in ['y', 'yes', '是']:
                    self.handle_new_game_command(['medium'])
                    continue
                else:
                    self.running = False
                    break
            
            user_input = input("輸入指令 Enter command: ").strip()
            if not user_input:
                continue
            
            parsed = self.parse_command(user_input)
            if not parsed:
                print("❌ 無效指令 | Invalid command")
                continue
            
            action, args = parsed
            
            if action == 'move':
                self.handle_move_command(args)
            elif action == 'clear':
                self.handle_clear_command(args)
            elif action == 'hint':
                self.handle_hint_command()
            elif action == 'reset':
                self.handle_reset_command()
            elif action == 'new':
                self.handle_new_game_command(args)
            elif action in ['quit', 'exit', 'q']:
                self.running = False
            else:
                print("❌ 未知指令 | Unknown command")
            
            print()  # Add spacing after each command


def main() -> None:
    """Main function to start the Sudoku console game."""
    try:
        console = SudokuConsole()
        console.run()
        print("👋 感謝遊玩數獨遊戲！ Thanks for playing Sudoku!")
    except KeyboardInterrupt:
        print("\n👋 遊戲中斷。再見！ | Game interrupted. Goodbye!")
    except Exception as e:
        print(f"❌ 遊戲發生錯誤: {e} | Game error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()