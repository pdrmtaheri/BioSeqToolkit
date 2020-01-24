import tkinter as tk
from tkinter import filedialog, messagebox

import graphviz
from suffix_tree import Tree

from src.input import InputDialog
from src.output import output


class LongestPalindromeFinder(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        tk.Label(self, text='Sequence:').grid(row=0, column=0, sticky='w')
        self.sequence_text = tk.Text(self)
        self.sequence_text.grid(row=1, column=0, columnspan=2, sticky='nsew')

        self.sequence_load_btn = tk.Button(
            self, text='Choose file', command=self.choose_sequence_file)
        self.sequence_load_btn.grid(row=2, column=1, sticky='e')

        buttons_frame = tk.Frame(self)
        self.run_btn = tk.Button(master=buttons_frame,
                                 text='Run', command=self.run)
        self.run_btn.grid(row=0, column=1)

        self.export_btn = tk.Button(
            master=buttons_frame, text='Export Tree', command=self.export_tree)
        self.export_btn.grid(row=0, column=0)
        buttons_frame.grid(row=3, column=0, columnspan=2, sticky='e')

        for i in range(2):
            self.grid_columnconfigure(i, weight=1)

        for i in range(4):
            self.grid_rowconfigure(i, weight=1)

        self.sequence = None

        self.tree = None

    def choose_sequence_file(self):
        filename = filedialog.askopenfilename(parent=self)
        try:
            self.sequence_text.insert(tk.END, open(filename, 'r').read())
        except FileNotFoundError:
            messagebox.showwarning(
                title='Bad file', message='No files selected')

    def load_sequence(self):
        self.sequence = self.sequence_text.get(1.0, tk.END)

    def construct_tree(self):
        self.tree = Tree({1: self.sequence, 2: reversed(self.sequence)})

    def run(self):
        self.load_sequence()
        if not self.sequence:
            messagebox.showerror(
                title='Bad input', message='Invalid input sequence')
            return

        if not self.tree:
            self.construct_tree()

        result = str(self.tree.common_substrings()[0][2]).replace(' ', '')
        output(result, 'longest_palindrome_found.txt')

    def export_tree(self):
        if not self.tree:
            self.construct_tree()

        filename = filedialog.asksaveasfilename(parent=self.master)
        graphviz.Source(self.tree.to_dot()).render(
            filename=filename, format='pdf', view=True, cleanup=True)
