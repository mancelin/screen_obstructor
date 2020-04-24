import tkinter as tk
from tkinter import ttk
import argparse
import sys
from pynput.keyboard import Key, Listener

w = 400
h = 200
app = None



def number_or_default(s, default):
    try:
        n = int(s)
        return n
    except ValueError:
        return default


def on_keyboard_press(key):
    global app
    if (key == Key.esc):
        app.destroy()



if __name__ == '__main__':
    parser = argparse.ArgumentParser("obstructor")
    parser.add_argument("w", help="width of obstructor")
    parser.add_argument("h", help="height of obstructor")
    args = parser.parse_args()
    w = number_or_default(args.w, w)
    h = number_or_default(args.h, h)
    # app = Example()
    # app.mainloop()
    app = tk.Tk()
    app.title("obstructor")
    app.geometry("{}x{}".format(w, h))
    app.configure()

    def close(event):
        app.destroy()

    keyboard_listener = Listener(
        on_press=on_keyboard_press)
    keyboard_listener.start()

    app['bg'] = '#000000'
    app.overrideredirect(True)
    app.mainloop()
