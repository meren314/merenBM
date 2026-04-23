# merenBM

**A lightweight Minesweeper keyboard assistant for Windows.**

**一款轻量级的 Windows 扫雷键盘辅助工具。**

[English](#english) | [中文](#中文)

---

## 中文

### 简介

merenBM 通过全局热键监听 + Win32 API 鼠标模拟，将键盘输入转化为鼠标点击操作，帮助扫雷玩家实现极低延迟的按键操作。

这是一个使用 AI 编程的扫雷映射软件。由于传统扫雷可能的规则限制，我们暂不建议在扫雷世界排行中进行使用，而提倡这是一种扫雷的新玩法。

### 功能特性

- **标准模式** — A/S/D/F 左键单击，Q/W/E/R 左右键同按开片区
- **NF 模式** — 所有字母/数字键均为左键单击
- **全键点击模式** — 所有字母/数字键均为左右键同按
- **自定义模式** — 自由绑定左键、右键、双键的按键组合
- **中英双语界面** — 支持一键切换
- **极低延迟** — 基于 `win32api.mouse_event`，延迟 < 1ms

### 技术原理

| 方案 | 延迟 | 说明 |
|------|------|------|
| pyautogui | ~10-50ms | 基于 ctypes SendInput，有额外 DPI 缩放处理 |
| pydirectinput | ~5-10ms | 面向游戏外设模拟，API 过于复杂 |
| **keyboard + win32api** | **< 1ms** | 全局热键钩子 + 最底层鼠标事件模拟 |

### 使用方法

1. 从 [Releases](../../releases) 下载最新版 `merenBM.exe`
2. **右键 → 以管理员身份运行**（keyboard 库需要全局热键权限）
3. 按 `+` 键切换启用/禁用
4. 根据当前模式使用对应按键操作扫雷

### 版本历史

| 版本 | 日期 | 说明 |
|------|------|------|
| v1.0.0 | 2026-04-24 | 首次发布：四种模式、中英双语、自定义按键 |

### 许可证

[MIT License](LICENSE) - Copyright (c) 2026 meren314

---

## English

### About

merenBM uses global hotkey capture + Win32 API mouse simulation to convert keyboard input into mouse clicks, enabling Minesweeper players to achieve ultra-low-latency key operations.

This is an AI-programmed Minesweeper mapping tool. Due to potential restrictions in traditional Minesweeper rules, we do not recommend using it in the Minesweeper World Rankings, but rather encourage it as a new way to play Minesweeper.

### Features

- **Standard Mode** — A/S/D/F for left click, Q/W/E/R for chord (L+R)
- **NF Mode** — All letter/digit keys trigger left click
- **Full Key Mode** — All letter/digit keys trigger chord (L+R)
- **Custom Mode** — Freely bind keys for left click, right click, and chord
- **Bilingual UI** — Switch between Chinese and English
- **Ultra-low latency** — Based on `win32api.mouse_event`, latency < 1ms

### Technical Comparison

| Approach | Latency | Notes |
|----------|---------|-------|
| pyautogui | ~10-50ms | ctypes SendInput with extra DPI scaling |
| pydirectinput | ~5-10ms | Designed for game peripherals, overly complex |
| **keyboard + win32api** | **< 1ms** | Global hotkey hooks + lowest-level mouse event API |

### Usage

1. Download the latest `merenBM.exe` from [Releases](../../releases)
2. **Right-click → Run as administrator** (keyboard library requires global hook permissions)
3. Press `+` to toggle on/off
4. Use the corresponding keys based on the current mode

### Version History

| Version | Date | Notes |
|---------|------|-------|
| v1.0.0 | 2026-04-24 | Initial release: four modes, bilingual UI, custom key bindings |

### License

[MIT License](LICENSE) - Copyright (c) 2026 meren314
