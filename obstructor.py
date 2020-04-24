import tkinter as tk
from tkinter import ttk
import argparse
import sys
from pynput.keyboard import Key, Listener
import ipdb

obstructor1 = None
obstructor2 = None
obstructor3 = None
obstructor4 = None


def number_or_default(s, default):
    try:
        n = int(s)
        return n
    except ValueError:
        return default


def on_keyboard_press(key):
    global obstructor1
    if (key == Key.esc):
        obstructor1.destroy()
        # obstructor2.destroy()
        # obstructor3.destroy()
        # obstructor4.destroy()
        sys.exit()
        # _g = globals()
        # for i in range(1, 5):
        #     obstructor_name = "obstructor{}".format(i)
        #     _g[obstructor_name].destroy()


if __name__ == '__main__':
    parser = argparse.ArgumentParser("obstructor")
    for i in range(1, 5):
        parser.add_argument(
            "w{}".format(i),
            help="width of obstructor {}".format(i))
        parser.add_argument(
            "h{}".format(i),
            help="height of obstructor {}".format(i))
        parser.add_argument(
            "x{}".format(i),
            help="width of obstructor {}".format(i))
        parser.add_argument(
            "y{}".format(i),
            help="height of obstructor {}".format(i))
    args = parser.parse_args()
    print("args : ", args)

    keyboard_listener = Listener(
        on_press=on_keyboard_press)
    keyboard_listener.start()

    _g = globals()
    for i in range(1, 5):
        wi = "w{}".format(i)
        hi = "h{}".format(i)
        xi = "x{}".format(i)
        yi = "y{}".format(i)
        arg_wi = vars(args)[wi]
        arg_hi = vars(args)[hi]
        arg_xi = vars(args)[xi]
        arg_yi = vars(args)[yi]
        # ipdb.set_trace(context=13)
        _g[wi] = number_or_default(arg_wi, 40)
        _g[hi] = number_or_default(arg_hi, 40)
        _g[xi] = number_or_default(arg_xi, 0)
        _g[yi] = number_or_default(arg_yi, 0)
        obstructor_name = "obstructor{}".format(i)
        _g[obstructor_name] = tk.Tk()
        _g[obstructor_name].title(obstructor_name)
        _g[obstructor_name].geometry("{}x{}+{}+{}".format(_g[wi], _g[hi], _g[xi], _g[yi]))
        _g[obstructor_name].configure()
        _g[obstructor_name]['bg']='#000000'
        _g[obstructor_name].overrideredirect(True)
    print(_g)
    for i in range(1, 5):
        obstructor_name = "obstructor{}".format(i)
        _g[obstructor_name].mainloop()
