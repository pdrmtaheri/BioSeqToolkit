import tkinter as tk

from src.input import InputDialog


class LongestRepetitiveSubstringFinder(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        self.sequence_btn = tk.Button(master=self, text='Load Sequence', command=self.load_sequence)
        self.sequence_btn.pack()        

        self.run_btn = tk.Button(master=self, text='Run', command=self.run)
        self.run_btn.pack()

        self.pack()

    def load_sequence(self):
        dialog_result = InputDialog(master=self).show()
        print(dialog_result)

    def run(self):
        pass
