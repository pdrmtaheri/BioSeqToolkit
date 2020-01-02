import tkinter as tk

from src.input import InputDialog


class PatternFinder(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        self.pattern_btn = tk.Button(master=self, text='Load Pattern', command=self.load_pattern)
        self.pattern_btn.pack()

        self.sequence_btn = tk.Button(master=self, text='Load Sequences', command=self.load_sequences)
        self.sequence_btn.pack()

        self.run_btn = tk.Button(master=self, text='Run', command=self.run)
        self.run_btn.pack()

        self.pack()

    def load_pattern(self):
        dialog_result = InputDialog(master=self).show()
        print(dialog_result)

    def load_sequences(self):
        dialog_result = InputDialog(master=self).show()
        print(dialog_result)

    def run(self):
        pass
