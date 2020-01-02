import tkinter as tk

from src.commons import InputDialog


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.pattern_finder = tk.Button(self)
        self.pattern_finder['text'] = 'Pattern Finder'
        self.pattern_finder['command'] = self.create_pattern_finder_window
        self.pattern_finder.pack(side='top')

    def create_pattern_finder_window(self):
        print(InputDialog(master=self).show())


root = tk.Tk()
app = Application(master=root)
app.mainloop()
