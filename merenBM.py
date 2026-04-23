# -*- coding: utf-8 -*-
"""
merenBM - Minesweeper Assistant
Version 1.0.0
Copyright (c) 2026 meren. All rights reserved.
"""

import keyboard
import tkinter as tk

from core import MinesweeperHelper
from gui import HelperGUI


if __name__ == "__main__":
    helper = MinesweeperHelper()

    root = tk.Tk()
    app = HelperGUI(root, helper)

    root.protocol("WM_DELETE_WINDOW", lambda: (keyboard.unhook_all(), root.destroy()))
    root.mainloop()
