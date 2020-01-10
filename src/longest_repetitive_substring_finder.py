import tkinter as tk

from src.input import InputDialog


class LongestRepetitiveSubstringFinder(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        self.sequence_btn = tk.Button(
            master=self, text='Load Sequence', command=self.load_sequence)
        self.sequence_btn.pack()

        self.k_entry = tk.Entry(master=self)
        self.k_entry.pack()

        self.run_btn = tk.Button(master=self, text='Run', command=self.run)
        self.run_btn.pack()

        self.pack()

        self.sequence = None
        self.k = None

    def load_sequence(self):
        self.sequence = InputDialog(master=self).show()

    def load_k(self):
        self.k = int(self.k_entry.get())

    def run(self):
        self.load_k()
