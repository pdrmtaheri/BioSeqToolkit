import tkinter as tk

from suffix_tree import Tree

from src.input import InputDialog
from src.output import output
from src.utils import read_fastq


class PatternFinder(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        self.pattern_btn = tk.Button(
            master=self, text='Load Pattern', command=self.load_pattern)
        self.pattern_btn.pack()

        self.sequence_btn = tk.Button(
            master=self, text='Load Sequences', command=self.load_sequences)
        self.sequence_btn.pack()

        self.run_btn = tk.Button(master=self, text='Run', command=self.run)
        self.run_btn.pack()

        self.pack()

        self.sequences = None
        self.pattern = None

    def load_pattern(self):
        self.pattern = InputDialog(master=self).show().strip("\n")

    def load_sequences(self):
        self.sequences = read_fastq(InputDialog(master=self).show())

    def run(self):
        tree = Tree(dict(enumerate(self.sequences)))
        result = '\n'.join([f'{idx} {path.start}' for idx, path in tree.find_all(self.pattern)])
        output(result, 'patterns_found.txt')
