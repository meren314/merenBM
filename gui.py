# -*- coding: utf-8 -*-
"""merenBM - GUI (tkinter)"""

import string
import keyboard
import tkinter as tk
from tkinter import messagebox

from config import MODE_ORDER, ALL_KEYS, ALLOWED_CHARS
from i18n import LANG


class HelperGUI:
    def __init__(self, root, helper):
        self.root = root
        self.helper = helper
        self.lang = "zh"
        self.current_mode = "standard"

        self.left_click_keys = ["a", "s", "d", "f"]
        self.chord_open_keys = ["q", "w", "e", "r"]
        self.right_click_keys = []

        self.custom_left = list(self.left_click_keys)
        self.custom_right = list(self.right_click_keys)
        self.custom_chord = list(self.chord_open_keys)

        self.mode_buttons = []

        self._build_ui()
        self._bind_mode_keys()

    # ── text helper ──

    def t(self, key):
        return LANG[self.lang][key]

    def mode_name(self, mode=None):
        if mode is None:
            mode = self.current_mode
        return self.t(f"mode_{mode}")

    # ── build UI ──

    def _build_menubar(self):
        menubar = tk.Menu(self.root)

        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label=self.t("menu_language"), command=self._switch_language)
        menubar.add_cascade(label=self.t("menu_settings"), menu=settings_menu)

        about_menu = tk.Menu(menubar, tearoff=0)
        about_menu.add_command(label=self.t("menu_about"), command=self._show_about)
        about_menu.add_command(label=self.t("menu_help"), command=self._show_help)
        menubar.add_cascade(label=self.t("menu_about"), menu=about_menu)

        self.root.config(menu=menubar)

    def _build_ui(self):
        self.root.title(self.t("title"))
        self.root.geometry("480x480")
        self.root.resizable(False, False)

        self._build_menubar()

        mode_frame = tk.Frame(self.root, bg="#e8e8e8", padx=5, pady=5)
        mode_frame.pack(fill="x", padx=10, pady=(10, 5))

        for mode_key in MODE_ORDER:
            btn = tk.Button(
                mode_frame,
                text=self.t(f"mode_{mode_key}"),
                font=("微软雅黑", 10),
                bg="#d0d0d0",
                fg="black",
                activebackground="#c0c0c0",
                activeforeground="black",
                relief="raised",
                width=9,
                command=lambda m=mode_key: self._switch_mode(m),
            )
            btn.pack(side="left", padx=3, pady=4)
            self.mode_buttons.append(btn)

        self._highlight_mode()

        self.mode_label = tk.Label(
            self.root,
            text=self.t("current_mode").format(mode=self.mode_name()),
            font=("微软雅黑", 16, "bold"),
        )
        self.mode_label.pack(pady=(15, 5))

        self.toggle_btn = tk.Button(
            self.root,
            text=self.t("btn_off"),
            font=("微软雅黑", 18, "bold"),
            fg="white",
            bg="#ff4444",
            activebackground="#ff4444",
            activeforeground="white",
            width=14,
            height=2,
            relief="raised",
            command=self._manual_toggle,
        )
        self.toggle_btn.pack(pady=15)

        self.info_label = tk.Label(
            self.root,
            text=self.t("hotkey_info")[self.current_mode],
            font=("微软雅黑", 10),
            justify="left",
        )
        self.info_label.pack(pady=10, padx=20, anchor="w")

        tk.Label(
            self.root,
            text=self.t("copyright"),
            font=("微软雅黑", 8),
            fg="#888888",
        ).pack(side="bottom", pady=5)

    # ── mode switching ──

    def _highlight_mode(self):
        for i, mode_key in enumerate(MODE_ORDER):
            if mode_key == self.current_mode:
                self.mode_buttons[i].config(bg="#ffffff", relief="sunken")
            else:
                self.mode_buttons[i].config(bg="#d0d0d0", relief="raised")

    def _switch_mode(self, mode):
        if mode == self.current_mode:
            return
        if mode == "custom":
            self._show_custom_dialog()
            return
        self.current_mode = mode
        self._bind_mode_keys()
        self._refresh_ui()

    def _refresh_ui(self):
        self.mode_label.config(text=self.t("current_mode").format(mode=self.mode_name()))
        self.info_label.config(text=self.t("hotkey_info")[self.current_mode])
        self._highlight_mode()

    def _bind_mode_keys(self):
        keyboard.unhook_all()
        keyboard.add_hotkey(self.helper.toggle_key, self._toggle_and_update)
        if self.current_mode == "standard":
            for k in self.left_click_keys:
                keyboard.add_hotkey(k, self.helper.simulate_left_click)
            for k in self.chord_open_keys:
                keyboard.add_hotkey(k, self.helper.simulate_chord_open)
        elif self.current_mode == "nf":
            for k in ALL_KEYS:
                keyboard.add_hotkey(k, self.helper.simulate_left_click)
        elif self.current_mode == "full":
            for k in ALL_KEYS:
                keyboard.add_hotkey(k, self.helper.simulate_chord_open)
        elif self.current_mode == "custom":
            for k in self.custom_left:
                keyboard.add_hotkey(k, self.helper.simulate_left_click)
            for k in self.custom_right:
                keyboard.add_hotkey(k, self.helper.simulate_right_click)
            for k in self.custom_chord:
                keyboard.add_hotkey(k, self.helper.simulate_chord_open)

    # ── custom mode dialog ──

    def _show_custom_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title(self.t("custom_title"))
        dialog.geometry("420x320")
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()

        fields = []

        labels = [
            ("custom_left", ",".join(self.custom_left)),
            ("custom_right", ",".join(self.custom_right)),
            ("custom_chord", ",".join(self.custom_chord)),
        ]

        for lang_key, default_val in labels:
            row = tk.Frame(dialog)
            row.pack(fill="x", padx=15, pady=(10, 0))

            tk.Label(row, text=self.t(lang_key), font=("微软雅黑", 10), width=16, anchor="e").pack(side="left")

            entry = tk.Entry(row, font=("Consolas", 11), width=22)
            entry.insert(0, default_val)
            entry.pack(side="left", padx=(10, 0))
            fields.append(entry)

        tk.Label(
            dialog,
            text=self.t("custom_hint"),
            font=("微软雅黑", 8),
            fg="#888888",
        ).pack(pady=(12, 0))

        btn_frame = tk.Frame(dialog)
        btn_frame.pack(pady=20)

        def save():
            all_keys_set = set()
            results = []
            for entry in fields:
                raw = entry.get().strip()
                if not raw:
                    results.append([])
                    continue
                stripped = raw.replace(",", "")
                if not stripped:
                    results.append([])
                    continue
                if any(c not in ALLOWED_CHARS for c in stripped):
                    messagebox.showerror(self.t("custom_title"), self.t("custom_err_invalid"), parent=dialog)
                    return
                parts = [p.strip().lower() for p in raw.split(",") if p.strip()]
                for p in parts:
                    if not all(c in string.ascii_lowercase + string.digits for c in p):
                        messagebox.showerror(self.t("custom_title"), self.t("custom_err_invalid"), parent=dialog)
                        return
                if len(parts) != len(set(parts)):
                    messagebox.showerror(self.t("custom_title"), self.t("custom_err_dup"), parent=dialog)
                    return
                for p in parts:
                    if p in all_keys_set:
                        messagebox.showerror(self.t("custom_title"), self.t("custom_err_dup"), parent=dialog)
                        return
                    all_keys_set.add(p)
                results.append(parts)

            self.custom_left = results[0]
            self.custom_right = results[1]
            self.custom_chord = results[2]

            self.current_mode = "custom"
            self._bind_mode_keys()
            self._refresh_ui()
            dialog.destroy()

        def cancel():
            dialog.destroy()

        tk.Button(
            btn_frame, text=self.t("custom_save"), font=("微软雅黑", 10),
            width=10, command=save,
        ).pack(side="left", padx=10)

        tk.Button(
            btn_frame, text=self.t("custom_cancel"), font=("微软雅黑", 10),
            width=10, command=cancel,
        ).pack(side="left", padx=10)

    # ── toggle ──

    def _toggle_and_update(self):
        on = self.helper.toggle()
        self.root.after(0, lambda: self._update_toggle_ui(on))

    def _manual_toggle(self):
        on = self.helper.toggle()
        self._update_toggle_ui(on)

    def _update_toggle_ui(self, on):
        if on:
            self.toggle_btn.config(text=self.t("btn_on"), bg="#00C851", activebackground="#00C851")
        else:
            self.toggle_btn.config(text=self.t("btn_off"), bg="#ff4444", activebackground="#ff4444")

    # ── language ──

    def _switch_language(self):
        self.lang = "en" if self.lang == "zh" else "zh"
        self.root.title(self.t("title"))
        self._build_menubar()
        for i, mode_key in enumerate(MODE_ORDER):
            self.mode_buttons[i].config(text=self.t(f"mode_{mode_key}"))
        self._refresh_ui()
        on = self.helper.running
        self.toggle_btn.config(text=self.t("btn_on" if on else "btn_off"))

    # ── dialogs ──

    def _show_about(self):
        messagebox.showinfo(self.t("about_title"), self.t("about_text"))

    def _show_help(self):
        messagebox.showinfo(self.t("help_title"), self.t("help_text"))
