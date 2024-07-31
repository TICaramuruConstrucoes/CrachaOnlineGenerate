import tkinter as tk
from view.CrachaOnlineView import CrachaOnlineView
from viewModel.CrachaOnlineViewModel import CrachaOnlineViewModel


def main():
    root = tk.Tk()

    view_model = CrachaOnlineViewModel()
    view = CrachaOnlineView(root, view_model)

    root.mainloop()


if __name__ == "__main__":
    main()