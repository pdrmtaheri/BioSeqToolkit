import tkinter as tk

from suffix_tree import Tree

from src.input import InputDialog

internal_nodes = {}


def compute_internals(node):
    global internal_nodes
    if node.is_leaf():
        internal_nodes[node] = 0
        return
    internals = 1
    for child in node.children.values():
        internals += internal_nodes[child]
    internal_nodes[node] = internals


class LongestRepetitiveSubstringFinder(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        self.sequence_btn = tk.Button(
            master=self, text='Load Sequence', command=self.load_sequence)
        self.sequence_btn.pack()

        self.k_entry = tk.Entry(master=self)
        self.k_entry.pack()

        self.run_btn = tk.Button(master=self, text='Run', command=self.run)
        self.run_btn.pack()

        self.pack()

        self.sequence = None
        self.k = None

    def load_sequence(self):
        self.sequence = InputDialog(master=self).show()

    def load_k(self):
        self.k = int(self.k_entry.get())

    def run(self):
        self.load_k()
        tree = Tree({1: self.sequence})
        tree.root.post_order(compute_internals)
        candidate_nodes = list(filter(lambda node: internal_nodes[node] + 1 >= self.k, internal_nodes))
        candidate_strings = list(map(lambda node: str(node.path), candidate_nodes))
        candidate_strings = list(map(lambda string: string.translate(str.maketrans('', '', ' \n$')), candidate_strings))
        print(max(candidate_strings, key=lambda string: len(string)))
