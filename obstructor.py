import tkinter as tk
import argparse
import sys
from pynput.keyboard import Key, Listener
# import ipdb

obstructor1 = None
obstructor2 = None
obstructor3 = None
obstructor4 = None


def on_keyboard_press(key):
    global obstructor1
    if (key == Key.esc):
        obstructor1.destroy()
        sys.exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser("obstructor.py")
    parser.add_argument("w", help="width of screen")
    parser.add_argument("h", help="height of screen")
    parser.add_argument("x", help="x of visble")
    parser.add_argument("y", help="y of visble")
    parser.add_argument("wv", help="width of visble")
    parser.add_argument("hv", help="height of visble")
    args = parser.parse_args()

    keyboard_listener = Listener(
        on_press=on_keyboard_press)
    keyboard_listener.start()

    w1 = int(args.x)
    h1 = int(args.h)
    x1 = 0
    y1 = 0
    w2 = int(args.w)
    h2 = int(args.y)
    x2 = 0
    y2 = 0
    w3 = int(args.w) - (int(args.wv) + int(args.x))
    h3 = int(args.h)
    x3 = int(args.x) + int(args.wv)
    y3 = 0
    w4 = int(args.w)
    h4 = int(args.h) - (int(args.hv) + int(args.y))
    x4 = 0
    y4 = int(args.y) + int(args.hv)

    _g = globals()
    for i in range(1, 5):
        wi = "w{}".format(i)
        hi = "h{}".format(i)
        xi = "x{}".format(i)
        yi = "y{}".format(i)
        obstructor_name = "obstructor{}".format(i)
        _g[obstructor_name] = tk.Tk()
        _g[obstructor_name].title(obstructor_name)
        _g[obstructor_name].geometry("{}x{}+{}+{}".format(_g[wi], _g[hi], _g[xi], _g[yi]))
        _g[obstructor_name].configure()
        _g[obstructor_name]['bg']='#000000'
        _g[obstructor_name].overrideredirect(True)
    for i in range(1, 5):
        obstructor_name = "obstructor{}".format(i)
        _g[obstructor_name].mainloop()
