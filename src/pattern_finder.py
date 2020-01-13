import tkinter as tk
from tkinter import messagebox, filedialog

import graphviz

from src.input import InputDialog
from src.output import output
from src.tree import SuffixTree
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

        self.export_btn = tk.Button(master=self, text='Export Tree', command=self.export_tree)
        self.export_btn.pack()

        self.pack()

        self.sequences = None
        self.pattern = None

        self.tree = None

    def load_pattern(self):
        self.pattern = InputDialog(master=self).show().strip("\n")

    def load_sequences(self):
        self.sequences = read_fastq(InputDialog(master=self).show())

    def construct_tree(self):
        self.tree = SuffixTree(dict(enumerate(self.sequences)))

    def run(self):
        if not self.sequences:
            messagebox.showerror(title='Bad input', message='Invalid input sequences')
            return

        if not self.pattern:
            messagebox.showerror(title='Bad input', message='Invalid input pattern')
            return

        if not self.tree:
            self.construct_tree()

        result = '\n'.join([f'{idx} {path.start}' for idx, path in self.tree.find_all(self.pattern)])
        output(result, 'patterns_found.txt')

    def export_tree(self):
        if not self.tree:
            self.construct_tree()

        filename = filedialog.asksaveasfilename(parent=self.master)
        graphviz.Source(self.tree.to_dot()).render(filename=filename, format='pdf', view=True, cleanup=True)
