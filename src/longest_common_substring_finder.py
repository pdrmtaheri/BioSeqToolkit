import tkinter as tk
from tkinter import messagebox

from src.input import InputDialog
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

        self.pack()

        self.sequences = None
        self.k = None

    def load_sequences(self):
        self.sequences = read_fastq(InputDialog(master=self).show())

    def load_k(self):
        try:
            self.k = int(self.k_entry.get())
        except ValueError:
            messagebox.showerror(title='Bad input', message='Invalid input "k"')

    def run(self):
        self.load_k()
        if not self.k or not self.sequences:
            return
