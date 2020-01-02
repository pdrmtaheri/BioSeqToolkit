import tkinter as tk

from src.commons import InputDialog


class LongestPalindromeFinder(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        self.sequence_btn = self.create_sequence_load_button()
        self.run_btn = self.create_run_button()

        self.pack()

    def create_sequence_load_button(self):
        btn = tk.Button(master=self)
        btn['text'] = 'Load Sequence'
        btn['command'] = self.load_sequence
        btn.pack()

        return btn

    def create_run_button(self):
        btn = tk.Button(master=self)
        btn['text'] = 'Run'
        btn['command'] = self.run
        btn.pack()

        return btn

    def load_sequence(self):
        dialog_result = InputDialog(master=self).show()
        print(dialog_result)

    def run(self):
        pass
