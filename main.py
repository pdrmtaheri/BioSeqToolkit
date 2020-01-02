import tkinter as tk

from src.pattern_finder import PatternFinder


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.create_pattern_finder_button()

        self.pack()

    def create_pattern_finder_button(self):
        btn = tk.Button(self)
        btn['text'] = 'Pattern Finder'
        btn['command'] = lambda: PatternFinder(tk.Toplevel(master=self))
        btn.pack()

        return btn


root = tk.Tk()
app = Application(master=root)
app.mainloop()
