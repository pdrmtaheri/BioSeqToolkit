import tkinter as tk

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

        self.pack()

        self.sequence = None

    def load_sequence(self):
        self.sequence = InputDialog(master=self).show()

    def run(self):
        tree = Tree({1: self.sequence, 2: reversed(self.sequence)})
        result = str(tree.common_substrings()[0][2]).replace(' ', '')
        output(result, 'longest_palindrome.txt')
