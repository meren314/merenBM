# -*- coding: utf-8 -*-
"""merenBM - Core Mouse Simulation Logic"""

import win32api
import win32con


class MinesweeperHelper:
    def __init__(self):
        self.running = False
        self.toggle_key = "+"

    def toggle(self):
        self.running = not self.running
        return self.running

    def simulate_left_click(self):
        if not self.running:
            return
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def simulate_right_click(self):
        if not self.running:
            return
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

    def simulate_chord_open(self):
        if not self.running:
            return
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
