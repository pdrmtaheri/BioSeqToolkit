import tkinter as tk

from src.commons import InputDialog


class PatternFinder(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        self.pattern_btn = self.create_pattern_load_button()
        self.sequence_btn = self.create_sequences_load_button()

        self.pack()

    def create_pattern_load_button(self):
        btn = tk.Button(master=self)
        btn['text'] = 'Load Pattern'
        btn['command'] = self.load_pattern
        btn.pack()

        return btn

    def create_sequences_load_button(self):
        btn = tk.Button(master=self)
        btn['text'] = 'Load Sequences'
        btn['command'] = self.load_sequences
        btn.pack()

        return btn
    
    def create_run_button(self):
        btn = tk.Button(master=self)
        btn['text'] = 'Run'
        btn['command'] = self.run
        btn.pack()

        return btn

    def load_pattern(self):
        dialog_result = InputDialog(master=self).show()
        print(dialog_result)

    def load_sequences(self):
        dialog_result = InputDialog(master=self).show()
        print(dialog_result)
    
    def run(self):
        pass
