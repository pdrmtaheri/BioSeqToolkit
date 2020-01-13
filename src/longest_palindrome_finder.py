import tkinter as tk
from tkinter import messagebox, filedialog

import graphviz
from suffix_tree import Tree

from src.input import InputDialog
from src.output import output


class LongestPalindromeFinder(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        self.sequence_btn = tk.Button(
            master=self, text='Load Sequence', command=self.load_sequence)
        self.sequence_btn.pack()

        self.run_btn = tk.Button(master=self, text='Run', command=self.run)
        self.run_btn.pack()

        self.export_btn = tk.Button(master=self, text='Export Tree', command=self.export_tree)
        self.export_btn.pack()

        self.pack()

        self.sequence = None

        self.tree = None

    def load_sequence(self):
        self.sequence = InputDialog(master=self).show()

    def construct_tree(self):
        self.tree = Tree({1: self.sequence, 2: reversed(self.sequence)})

    def run(self):
        if not self.sequence:
            messagebox.showerror(title='Bad input', message='Invalid input sequence')
            return

        if not self.tree:
            self.construct_tree()

        result = str(self.tree.common_substrings()[0][2]).replace(' ', '')
        output(result, 'longest_palindrome_found.txt')

    def export_tree(self):
        if not self.tree:
            self.construct_tree()

        filename = filedialog.asksaveasfilename(parent=self.master)
        graphviz.Source(self.tree.to_dot()).render(filename=filename, format='pdf', view=True, cleanup=True)
