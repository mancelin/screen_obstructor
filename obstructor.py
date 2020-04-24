import tkinter as tk
from tkinter import ttk
import argparse
import sys
from pynput.keyboard import Key, Listener

w = 400
h = 200
app = None

"""
class Example(tk.Tk):
    def __init__(self):
        app = tk.Tk.__init__(self)
        app.root.title("obstructor")
        # root.__init__(self)
        # root.title("obstructor")
        self.floater = FloatingWindow(self)


class FloatingWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.overrideredirect(True)
        self.wm_geometry("{}x{}".format(w, h))

        self.label = tk.Label(self, text="")
        self.label.pack(side="top", fill="both", expand=True)

        self.grip = ttk.Sizegrip(self)
        self.grip.place(relx=1.0, rely=1.0, anchor="se")
        self.grip.lift(self.label)
        self.grip.bind("<B1-Motion>", self.OnMotion)

    def OnMotion(self, event):
        x1 = self.winfo_pointerx()
        y1 = self.winfo_pointery()
        x0 = self.winfo_rootx()
        y0 = self.winfo_rooty()
        self.geometry("%sx%s" % ((x1-x0), (y1-y0)))
        return
"""


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
        print("close")
        # sys.exit()
        app.destroy()

    keyboard_listener = Listener(
        on_press=on_keyboard_press)
    keyboard_listener.start()

    app['bg'] = '#000000'
    app.overrideredirect(True)
    # app.bind('<Escape>', close)
    app.mainloop()
