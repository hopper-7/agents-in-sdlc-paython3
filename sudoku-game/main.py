#!/usr/bin/env python3
"""
Sudoku Game Launcher
Main entry point for the Sudoku game application.
Run this script to start playing Sudoku in the console.
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from console_interface import main

if __name__ == "__main__":
    main()