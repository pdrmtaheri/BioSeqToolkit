import tkinter as tk
from tkinter import messagebox, filedialog

import graphviz

from src.input import InputDialog
from src.output import output
from src.tree import SuffixTree
from src.utils import read_fastq


class LongestCommonSubstringFinder(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        self.sequence_btn = tk.Button(
            master=self, text='Load Sequences', command=self.load_sequences)
        self.sequence_btn.pack()

        self.k_entry = tk.Entry(master=self)
        self.k_entry.pack()

        self.run_btn = tk.Button(master=self, text='Run', command=self.run)
        self.run_btn.pack()

        self.export_btn = tk.Button(master=self, text='Export Tree', command=self.export_tree)
        self.export_btn.pack()

        self.pack()

        self.sequences = None
        self.k = None

        self.tree = None

    def load_sequences(self):
        self.sequences = read_fastq(InputDialog(master=self).show())

    def load_k(self):
        try:
            self.k = int(self.k_entry.get())
        except ValueError:
            pass

    def construct_tree(self):
        self.tree = SuffixTree(dict(enumerate(self.sequences)))

    def run(self):
        if not self.sequences:
            messagebox.showerror(title='Bad input', message='Invalid input sequences')
            return

        self.load_k()
        if not self.k:
            messagebox.showerror(title='Bad input', message='Invalid input "k"')
            return

        if not self.tree:
            self.construct_tree()

        result = self.tree.longest_common_substring(self.k)
        output(result, 'longest_common_substring.txt')

    def export_tree(self):
        if not self.tree:
            self.construct_tree()

        filename = filedialog.asksaveasfilename(parent=self.master)
        graphviz.Source(self.tree.to_dot()).render(filename=filename, format='pdf', view=True, cleanup=True)
