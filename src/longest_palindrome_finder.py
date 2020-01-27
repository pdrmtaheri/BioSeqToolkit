import tkinter as tk
from tkinter import filedialog, messagebox

import graphviz
from suffix_tree import Tree

from src.output import output


class LongestPalindromeFinder(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        tk.Label(self, text='Sequence').grid(row=0, column=0, sticky='w')
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
            self.sequence_text.delete(1.0, tk.END)
            self.sequence_text.insert(tk.END, open(filename, 'r').read())
        except FileNotFoundError:
            messagebox.showwarning(
                title='Bad file', message='No files selected')

    def load_sequence(self):
        self.sequence = self.sequence_text.get(1.0, tk.END).strip("\n ")

    def construct_tree(self):
        self.tree = Tree({1: self.sequence, 2: reversed(self.sequence)})

    def initialize(self):
        self.load_sequence()
        if not self.sequence:
            messagebox.showerror(
                title='Bad input', message='Invalid input sequence')
            return
        self.construct_tree()

    def run(self):
        self.initialize()
        result = str(self.find_the_longest_palindrome()).replace(' ', '')
        output(result, 'longest_palindrome_found.txt')

    def build_neighbor_leaves(self):
        leaves = {}

        def f(node):
            if node.is_leaf():
                leaves[(node.str_id, node.path.start)] = node

        self.tree.root.post_order(f)
        odd_neighbor_leaves = [(leaves[1, i], leaves[2, len(self.sequence) - 1 - i]) for i in range(len(self.sequence))]
        even_neighbor_leaves = [(self.sequence[i], leaves[1, i + 1], leaves[2, len(self.sequence) + 1 - i]) for i in
                                range(1, len(self.sequence) - 1) if self.sequence[i - 1] == self.sequence[i]]
        # neighbor_leaves = [(leaves[i, 0], leaves[2, 0])]
        return odd_neighbor_leaves, even_neighbor_leaves

    def find_the_longest_odd_palindrome(self, neighbor_leaves):
        candidate_node = None
        for node1, node2 in neighbor_leaves:
            node = self.tree.lca(node1, node2)
            if candidate_node is None or len(node) > len(candidate_node):
                candidate_node = node
        result = str(candidate_node).replace(' ', '')
        result = (result[::-1])[:-1] + result
        return result

    def find_the_longest_even_palindrome(self, neighbor_leaves):
        if not neighbor_leaves:
            return ''
        candidate_node = None
        middle = None
        for mid, node1, node2 in neighbor_leaves:
            node = self.tree.lca(node1, node2)
            if candidate_node is None or len(node) > len(candidate_node):
                candidate_node = node
                middle = mid
        if candidate_node == self.tree.root:
            candidate_node = ''
        result = str(candidate_node).replace(' ', '')
        result = result[::-1] + (middle * 2) + result
        return result

    def find_the_longest_palindrome(self):
        odd_neighbor_leaves, even_neighbor_leaves = self.build_neighbor_leaves()
        self.tree.prepare_lca()
        odd_palindrome = self.find_the_longest_odd_palindrome(odd_neighbor_leaves)
        even_palindrome = self.find_the_longest_even_palindrome(even_neighbor_leaves)

        return max(odd_palindrome, even_palindrome, key=len)

    def export_tree(self):
        self.initialize()
        filename = filedialog.asksaveasfilename(parent=self.master)
        graphviz.Source(self.tree.to_dot()).render(
            filename=filename, format='pdf', view=True, cleanup=True)
