# -*- coding: utf-8 -*-
"""merenBM - Internationalization"""

LANG = {
    "zh": {
        "title": "merenBM",
        "menu_settings": "设置",
        "menu_language": "语言 / Language",
        "menu_about": "制作者",
        "menu_help": "软件说明",
        "mode_standard": "标准模式",
        "mode_nf": "NF模式",
        "mode_full": "全键点击模式",
        "mode_custom": "自定义模式",
        "current_mode": "当前模式：{mode}",
        "btn_on": "模式开启",
        "btn_off": "模式关闭",
        "hotkey_info": {
            "standard": "[ + ] 切换启用/禁用\n[ A/S/D/F ] 左键单击\n[ Q/W/E/R ] 左右键同按开片区",
            "nf": "[ + ] 切换启用/禁用\n[ 所有字母/数字 ] 左键单击",
            "full": "[ + ] 切换启用/禁用\n[ 所有字母/数字 ] 左右键同时点击",
            "custom": "自定义按键绑定",
        },
        "custom_title": "自定义模式设置",
        "custom_left": "左键点击按键：",
        "custom_right": "右键点击按键：",
        "custom_chord": "双键点击按键：",
        "custom_hint": "用英文逗号分隔，仅限字母和数字，不可重复",
        "custom_save": "保存",
        "custom_cancel": "取消",
        "custom_err_invalid": "输入包含无效字符！仅允许26个英文字母和数字。",
        "custom_err_dup": "按键存在重复！请检查同一输入框内或跨输入框是否有重复按键。",
        "about_title": "制作者",
        "about_text": "软件制作和灵感来源：meren",
        "help_title": "软件说明",
        "help_text": (
            "技术原理：\n"
            "本软件通过 keyboard 库进行全局热键监听，\n"
            "捕获键盘输入后调用 Win32 API（win32api.mouse_event）\n"
            "模拟鼠标事件，实现低延迟的鼠标点击操作。\n\n"
            "方案选择分析：\n"
            "1. 为什么不用 pyautogui？\n"
            "   pyautogui 基于 ctypes 调用 SendInput，\n"
            "   内部有额外的坐标计算和 DPI 缩放处理，\n"
            "   延迟较高（约 10-50ms），不适合扫雷\n"
            "   这种对实时性要求极高的场景。\n\n"
            "2. 为什么不用 pydirectinput？\n"
            "   pydirectinput 虽然直接调用 SendInput，\n"
            "   但其 API 设计面向游戏外设模拟，\n"
            "   对简单鼠标点击来说过于复杂，\n"
            "   且对鼠标事件的精确控制不如直接调用\n"
            "   mouse_event 灵活。\n\n"
            "3. 为什么选择 keyboard + win32api？\n"
            "   - keyboard 库提供可靠的全局热键钩子，\n"
            "     即使窗口不在前台也能响应；\n"
            "   - win32api.mouse_event 是最底层的\n"
            "     鼠标事件模拟接口，延迟极低（<1ms）；\n"
            "   - 两者组合在延迟和可靠性上均为最优。\n"
        ),
        "copyright": "Copyright (c) 2026 meren. All rights reserved.",
    },
    "en": {
        "title": "merenBM",
        "menu_settings": "Settings",
        "menu_language": "语言 / Language",
        "menu_about": "About",
        "menu_help": "Software Info",
        "mode_standard": "Standard",
        "mode_nf": "NF Mode",
        "mode_full": "Full Key Mode",
        "mode_custom": "Custom",
        "current_mode": "Current: {mode}",
        "btn_on": "Enabled",
        "btn_off": "Disabled",
        "hotkey_info": {
            "standard": "[ + ] Toggle on/off\n[ A/S/D/F ] Left click\n[ Q/W/E/R ] Chord (L+R)",
            "nf": "[ + ] Toggle on/off\n[ All letters/digits ] Left click",
            "full": "[ + ] Toggle on/off\n[ All letters/digits ] Chord (L+R)",
            "custom": "Custom key bindings",
        },
        "custom_title": "Custom Mode Settings",
        "custom_left": "Left click keys:",
        "custom_right": "Right click keys:",
        "custom_chord": "Chord (L+R) keys:",
        "custom_hint": "Separate with commas. Letters and digits only, no duplicates.",
        "custom_save": "Save",
        "custom_cancel": "Cancel",
        "custom_err_invalid": "Invalid characters! Only letters (a-z) and digits (0-9) are allowed.",
        "custom_err_dup": "Duplicate keys found! Check within and across input fields.",
        "about_title": "About",
        "about_text": "Created by: meren",
        "help_title": "Software Info",
        "help_text": (
            "Technical Principle:\n"
            "This software uses the 'keyboard' library for global\n"
            "hotkey capture, then calls Win32 API\n"
            "(win32api.mouse_event) to simulate mouse events\n"
            "with minimal latency.\n\n"
            "Why not other approaches?\n\n"
            "1. Why not pyautogui?\n"
            "   pyautogui uses ctypes SendInput with extra\n"
            "   coordinate calculations and DPI scaling,\n"
            "   resulting in higher latency (10-50ms),\n"
            "   unsuitable for real-time scenarios like minesweeper.\n\n"
            "2. Why not pydirectinput?\n"
            "   pydirectinput directly calls SendInput but is\n"
            "   designed for game controller simulation.\n"
            "   It's overly complex for simple mouse clicks\n"
            "   and offers less precise control over mouse events\n"
            "   compared to direct mouse_event calls.\n\n"
            "3. Why keyboard + win32api?\n"
            "   - keyboard provides reliable global hotkey hooks\n"
            "     that work even when the window is not focused;\n"
            "   - win32api.mouse_event is the lowest-level mouse\n"
            "     event simulation API with latency <1ms;\n"
            "   - This combination offers the best latency\n"
            "     and reliability.\n"
        ),
        "copyright": "Copyright (c) 2026 meren. All rights reserved.",
    },
}
