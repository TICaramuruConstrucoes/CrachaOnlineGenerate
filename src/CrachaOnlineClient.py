import tkinter as tk

from src.view.CrachaOnlineView import CrachaOnlineView


def main():
    root = tk.Tk()
    CrachaOnlineView(root)
    root.mainloop()


if __name__ == "__main__":
    main()
