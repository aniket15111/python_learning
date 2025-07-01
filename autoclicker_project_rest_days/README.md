# 🔘 Multi-Click AutoClicker

A powerful, GUI-based Python application that allows you to configure and automate multiple mouse clicks across the screen, with precise timing, hotkeys, and draggable visual markers.

Built with:
- 🐍 Python
- 🖱️ PyAutoGUI
- 🎛️ Tkinter
- 🧠 Keyboard
- 💾 JSON (for saving/loading sequences)
- 🔁 Threading (for background execution)

---

## 🚀 Features

- 🎯 **Add click points** at current mouse location
- 🧠 **Set delay** between clicks in milliseconds
- 🔂 **Simultaneous clicking** for grouped zero-delay points
- 🧱 **Draggable markers** to visually move and update click positions
- 💾 **Save and load click sequences** as JSON
- 🧼 **Clear all points** quickly
- 🧵 **Threaded click execution** — UI stays responsive
- 🔥 **Hotkey control** for all major actions

---

## ⌨️ Hotkeys

| Hotkey | Action |
|--------|--------|
| `F4`   | Add click point at current mouse position |
| `F5`   | Start clicking sequence |
| `F6`   | Stop clicking |
| `F7`   | Save points to file |
| `F8`   | Load saved points |
| `F9`   | Clear all points |
| `F3`   | Enable drag mode (on marker under mouse) |

---

## 📦 Requirements

Install the required Python libraries:

```bash
pip install pyautogui keyboard
