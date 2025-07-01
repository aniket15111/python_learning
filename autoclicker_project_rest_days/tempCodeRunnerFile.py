import tkinter as tk
from tkinter import messagebox
import pyautogui
import threading
import time
import keyboard
import json

clicking = False
click_points = []
marker_windows = []
draggable_index = None  # Only this marker will be draggable


def start_clicking():
    global clicking
    try:
        interval = float(entry_interval.get()) / 1000.0
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid interval (in ms).")
        return

    if not click_points:
        messagebox.showwarning("No Click Points", "Add at least one click point.")
        return

    clicking = True
    status_label.config(text="Status: Clicking")

    def click_loop():
        while clicking:
            for point in click_points:
                if not clicking:
                    break
                pyautogui.click(point[0], point[1])
                time.sleep(interval)

    threading.Thread(target=click_loop, daemon=True).start()


def stop_clicking():
    global clicking
    clicking = False
    status_label.config(text="Status: Stopped")


def pick_position():
    pos = pyautogui.position()
    click_points.append((pos.x, pos.y))
    update_point_list()
    show_markers()


def save_points():
    with open("save_points.json", "w") as fd:
        json.dump(click_points, fd)
    messagebox.showinfo("Saved", "Click points saved successfully.")


def load_points():
    global click_points
    try:
        with open("save_points.json", "r") as fd:
            click_points = json.load(fd)
            update_point_list()
            show_markers()
        messagebox.showinfo("Loaded", "Click points loaded successfully.")
    except FileNotFoundError:
        messagebox.showerror("Error", "No saved points file found.")
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Saved file is corrupted or invalid.")


def clear_points():
    click_points.clear()
    update_point_list()
    clear_markers()


def update_point_list():
    point_listbox.delete(0, tk.END)
    for i, (x, y) in enumerate(click_points):
        point_listbox.insert(tk.END, f"{i + 1}. X: {x}, Y: {y}")


def clear_markers():
    for win in marker_windows:
        win.destroy()
    marker_windows.clear()


def make_marker_draggable(win, index):
    def start_drag(event):
        if index != draggable_index:
            return
        win.startX = event.x
        win.startY = event.y

    def on_drag(event):
        if index != draggable_index:
            return
        dx = event.x - win.startX
        dy = event.y - win.startY
        x = win.winfo_x() + dx
        y = win.winfo_y() + dy
        win.geometry(f"+{x}+{y}")
        click_points[index] = (x, y)
        update_point_list()

    win.bind("<Button-1>", start_drag)
    win.bind("<B1-Motion>", on_drag)


def show_markers():
    clear_markers()
    for i, (x, y) in enumerate(click_points):
        win = tk.Toplevel(root)
        win.overrideredirect(True)
        win.attributes("-topmost", True)
        win.geometry(f"20x20+{x}+{y}")
        frame = tk.Frame(win, bg="red", width=20, height=20)
        frame.pack()
        label = tk.Label(frame, text=str(i + 1), bg="red", fg="white")
        label.place(relx=0.5, rely=0.5, anchor="center")
        make_marker_draggable(win, i)
        marker_windows.append(win)


def enable_drag_mode():
    global draggable_index
    pos = pyautogui.position()
    for i, win in enumerate(marker_windows):
        win_x = win.winfo_x()
        win_y = win.winfo_y()
        if win_x <= pos.x <= win_x + 20 and win_y <= pos.y <= win_y + 20:
            draggable_index = i
            messagebox.showinfo("Drag Enabled", f"Marker {i+1} is now draggable.")
            return
    messagebox.showwarning("Not on Marker", "Mouse is not over any marker.")


def hotkey_listener():
    keyboard.add_hotkey("f4", pick_position)
    keyboard.add_hotkey("f5", start_clicking)
    keyboard.add_hotkey("f6", stop_clicking)
    keyboard.add_hotkey("f7", save_points)
    keyboard.add_hotkey("f8", load_points)
    keyboard.add_hotkey("f9", clear_points)
    keyboard.add_hotkey("f3", enable_drag_mode)


# GUI setup
root = tk.Tk()
root.title("Multi-Click AutoClicker")

tk.Label(root, text="Interval (ms):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_interval = tk.Entry(root)
entry_interval.insert(0, "500")
entry_interval.grid(row=0, column=1, padx=5, pady=5)

start_button = tk.Button(root, text="Start", command=start_clicking, bg="green", fg="white")
start_button.grid(row=1, column=0, pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_clicking, bg="red", fg="white")
stop_button.grid(row=1, column=1, pady=5)

pick_button = tk.Button(root, text="Add Click Point", command=pick_position)
pick_button.grid(row=2, column=0, columnspan=2, pady=5)

save_button = tk.Button(root, text="Save Points", command=save_points)
save_button.grid(row=3, column=0, columnspan=2, pady=5)

load_button = tk.Button(root, text="Load Points", command=load_points)
load_button.grid(row=4, column=0, columnspan=2, pady=5)

clear_button = tk.Button(root, text="Clear All Points", command=clear_points)
clear_button.grid(row=5, column=0, columnspan=2, pady=5)

tk.Label(root, text="Click Points:").grid(row=6, column=0, columnspan=2)
point_listbox = tk.Listbox(root, width=30)
point_listbox.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

status_label = tk.Label(root, text="Status: Idle")
status_label.grid(row=8, column=0, columnspan=2, pady=10)

threading.Thread(target=hotkey_listener, daemon=True).start()

root.mainloop()
