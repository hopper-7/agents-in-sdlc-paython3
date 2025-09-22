# 數獨遊戲 Sudoku Game

一個完整的數獨遊戲實作，具有謎題生成、求解、驗證和主控台介面功能。
A complete Sudoku game implementation with puzzle generation, solving, validation, and console interface.

## 功能特色 Features

### 🎮 遊戲功能 Game Features
- **謎題生成**: 支援簡單、中等、困難三種難度
- **Puzzle Generation**: Support for Easy, Medium, Hard difficulty levels
- **自動求解**: 使用回溯算法求解數獨謎題
- **Auto Solver**: Backtracking algorithm for solving Sudoku puzzles
- **提示系統**: 獲得下一步的有效提示
- **Hint System**: Get valid hints for next moves
- **遊戲驗證**: 檢查移動的有效性和解答的正確性
- **Game Validation**: Check move validity and solution correctness

### 💻 技術特色 Technical Features
- **純Python實作**: 無需外部依賴
- **Pure Python**: No external dependencies required
- **類型提示**: 完整的靜態類型支援
- **Type Hints**: Full static type support
- **單元測試**: 全面的測試覆蓋
- **Unit Tests**: Comprehensive test coverage
- **文件字串**: 完整的API文件
- **Docstrings**: Complete API documentation

## 專案結構 Project Structure

```
sudoku-game/
├── src/                    # 主要原始碼 Main source code
│   ├── __init__.py        # 套件初始化 Package initialization
│   ├── sudoku_game.py     # 核心遊戲邏輯 Core game logic
│   └── console_interface.py # 主控台介面 Console interface
├── tests/                  # 單元測試 Unit tests
│   ├── __init__.py        # 測試套件初始化 Test package init
│   ├── test_sudoku_game.py # 遊戲邏輯測試 Game logic tests
│   └── test_console_interface.py # 介面測試 Interface tests
├── docs/                   # 文件 Documentation
├── main.py                # 主要執行檔 Main entry point
└── README.md              # 專案說明 Project documentation
```

## 快速開始 Quick Start

### 安裝需求 Requirements
- Python 3.7 或更高版本 / Python 3.7 or higher
- 無需額外安裝套件 / No additional packages required

### 執行遊戲 Running the Game

```bash
# 導航到數獨遊戲目錄 Navigate to sudoku game directory
cd sudoku-game

# 執行遊戲 Run the game
python main.py
```

## 遊戲說明 How to Play

### 遊戲規則 Game Rules
1. 在9×9的格子中填入1-9的數字
2. 每一橫行都不能有重複的數字
3. 每一直列都不能有重複的數字
4. 每個3×3的小方格都不能有重複的數字

1. Fill numbers 1-9 in a 9×9 grid
2. Each row must contain unique numbers 1-9
3. Each column must contain unique numbers 1-9
4. Each 3×3 box must contain unique numbers 1-9

### 遊戲指令 Game Commands

| 指令 Command | 說明 Description | 範例 Example |
|--------------|------------------|--------------|
| `move <row> <col> <number>` | 在指定位置放置數字<br>Place number at position | `move 1 1 5` |
| `clear <row> <col>` | 清除指定位置的數字<br>Clear number at position | `clear 3 4` |
| `hint` | 獲得提示<br>Get a hint | `hint` |
| `reset` | 重置到原始謎題<br>Reset to original puzzle | `reset` |
| `new [difficulty]` | 開始新遊戲<br>Start new game | `new easy` |
| `quit` | 退出遊戲<br>Quit game | `quit` |

### 難度等級 Difficulty Levels

| 難度 Difficulty | 空格數量 Empty Cells | 說明 Description |
|-----------------|---------------------|------------------|
| **Easy 簡單** | 40 | 適合初學者 Perfect for beginners |
| **Medium 中等** | 50 | 平衡的挑戰 Balanced challenge |
| **Hard 困難** | 60 | 專家級挑戰 Expert level challenge |

## 程式開發 Development

### 執行測試 Running Tests

```bash
# 在sudoku-game目錄中執行所有測試 Run all tests in sudoku-game directory
python -m unittest discover tests/ -v

# 執行特定測試檔案 Run specific test file
python -m unittest tests.test_sudoku_game -v
python -m unittest tests.test_console_interface -v
```

### 程式碼架構 Code Architecture

#### SudokuGame 類別 Class
核心遊戲邏輯類別，處理：
Core game logic class that handles:

- **謎題生成** Puzzle generation
- **移動驗證** Move validation  
- **自動求解** Auto solving
- **提示功能** Hint generation
- **遊戲狀態管理** Game state management

#### SudokuConsole 類別 Class
主控台介面類別，提供：
Console interface class that provides:

- **使用者互動** User interaction
- **指令解析** Command parsing
- **遊戲顯示** Game display
- **錯誤處理** Error handling

### API 文件 API Documentation

詳細的API文件請參考原始碼中的docstring。
Detailed API documentation available in source code docstrings.

主要方法 Key methods:

#### SudokuGame
- `generate_puzzle(difficulty)`: 生成指定難度的謎題
- `make_move(row, col, num)`: 在指定位置放置數字
- `is_valid_move(row, col, num)`: 檢查移動是否有效
- `solve()`: 自動求解謎題
- `get_hint()`: 獲得提示
- `is_complete()`: 檢查謎題是否完成

#### SudokuConsole
- `run()`: 執行主遊戲迴圈
- `handle_move_command(args)`: 處理移動指令
- `display_game_status()`: 顯示遊戲狀態

## 設計原則 Design Principles

### 程式碼品質 Code Quality
- **類型提示**: 所有函數都有完整的類型標註
- **Type Hints**: All functions have complete type annotations
- **文件字串**: 每個類別和方法都有說明文件
- **Docstrings**: Every class and method has documentation
- **單一職責**: 每個類別都有明確的職責範圍
- **Single Responsibility**: Each class has a clear responsibility
- **測試覆蓋**: 全面的單元測試覆蓋
- **Test Coverage**: Comprehensive unit test coverage

### 國際化支援 Internationalization
- 雙語介面（中文/英文）
- Bilingual interface (Chinese/English)
- 錯誤訊息本地化
- Localized error messages
- 使用者友善的操作提示
- User-friendly operation hints

## 故障排除 Troubleshooting

### 常見問題 Common Issues

**Q: 遊戲無法啟動 Game won't start**
A: 確認Python版本是3.7以上 Ensure Python version is 3.7+

**Q: 測試失敗 Tests failing**
A: 確認在sudoku-game目錄中執行測試 Ensure running tests from sudoku-game directory

**Q: 無法輸入中文指令 Cannot input Chinese commands**
A: 使用英文指令，程式會自動識別 Use English commands, the program will recognize them automatically

## 授權 License

本專案遵循MIT開源授權條款。
This project is licensed under the MIT License.

## 貢獻 Contributing

歡迎提交Issue和Pull Request！
Issues and Pull Requests are welcome!

### 開發指南 Development Guidelines
1. 遵循現有的程式碼風格 Follow existing code style
2. 添加適當的測試 Add appropriate tests
3. 更新文件 Update documentation
4. 確保所有測試通過 Ensure all tests pass

---

## 範例遊戲畫面 Example Game Screen

```
🔢 歡迎來到數獨遊戲! Welcome to Sudoku Game! 🔢
==================================================

    1 2 3   4 5 6   7 8 9
  ╔═══════╦═══════╦═══════╗
1 ║ 5 3 ·   · 7 ·   · · · ║
2 ║ 6 · ·   1 9 5   · · · ║
3 ║ · 9 8   · · ·   · 6 · ║
  ╠═══════╬═══════╬═══════╣
4 ║ 8 · ·   · 6 ·   · · 3 ║
5 ║ 4 · ·   8 · 3   · · 1 ║
6 ║ 7 · ·   · 2 ·   · · 6 ║
  ╠═══════╬═══════╬═══════╣
7 ║ · 6 ·   · · ·   2 8 · ║
8 ║ · · ·   4 1 9   · · 5 ║
9 ║ · · ·   · 8 ·   · 7 9 ║
  ╚═══════╩═══════╩═══════╝

已填入: 31/81 個數字 | Filled: 31/81 cells

輸入指令 Enter command: move 1 3 4
✅ 在位置 (1, 3) 放置了數字 4
```

享受您的數獨之旅！🎯
Enjoy your Sudoku journey! 🎯