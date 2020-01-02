import tkinter as tk

from src.commons import InputDialog


class LongestCommonSubstringFinder(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        self.sequence_btn = self.create_sequences_load_button()
        self.k_entry = self.create_k_entry()
        self.run_btn = self.create_run_button()

        self.pack()

    def create_sequences_load_button(self):
        btn = tk.Button(master=self)
        btn['text'] = 'Load Sequences'
        btn['command'] = self.load_sequences
        btn.pack()

        return btn
    
    def create_k_entry(self):
        entry = tk.Entry(master=self)
        entry.pack()

        return entry
    
    def create_run_button(self):
        btn = tk.Button(master=self)
        btn['text'] = 'Run'
        btn['command'] = self.run
        btn.pack()

        return btn

    def load_sequences(self):
        dialog_result = InputDialog(master=self).show()
        print(dialog_result)
    
    def run(self):
        pass
