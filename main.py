import tkinter as tk

from src.longest_common_substring_finder import LongestCommonSubstringFinder
from src.longest_palindrome_finder import LongestPalindromeFinder
from src.longest_repetitive_substring_finder import \
    LongestRepetitiveSubstringFinder
from src.pattern_finder import PatternFinder


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pf_btn = tk.Button(master=self, text='Pattern Finder',
                                command=self.toggle_pf)
        self.pf_btn.grid(row=0, column=0, sticky='nsew')

        self.lrsf_btn = tk.Button(master=self, text='Longest Repetitive Substring Finder',
                                  command=self.toggle_lrsf)
        self.lrsf_btn.grid(row=1, column=0, sticky='nsew')

        self.lcsf_btn = tk.Button(master=self, text='Longest Common Substring Finder',
                                  command=self.toggle_lcsf)
        self.lcsf_btn.grid(row=2, column=0, sticky='nsew')

        self.lpf_btn = tk.Button(master=self, text='Longest Palindrome Finder',
                                 command=self.toggle_lpf)
        self.lpf_btn.grid(row=3, column=0, sticky='nsew')

        self.active_frame = tk.Frame()
        self.active_frame.grid(row=0, column=1, rowspan=4, sticky='nsew')

        for i in range(2):
            self.grid_columnconfigure(i, weight=1)

        for i in range(4):
            self.grid_rowconfigure(i, weight=1)

        tk.Grid.columnconfigure(master, 0, weight=1)
        tk.Grid.rowconfigure(master, 0, weight=1)

        self.grid(column=0, row=0, sticky='nsew')

    def _activate_buttons(self):
        self.pf_btn.configure(state='normal')
        self.lrsf_btn.configure(state='normal')
        self.lcsf_btn.configure(state='normal')
        self.lpf_btn.configure(state='normal')

    def toggle_pf(self):
        self._activate_buttons()
        self.pf_btn.configure(state='disabled')

        self.active_frame.destroy()
        self.active_frame = PatternFinder(self)
        self.active_frame.grid(row=0, column=1, rowspan=4, sticky='nsew')

    def toggle_lrsf(self):
        self._activate_buttons()
        self.lrsf_btn.configure(state='disabled')

        self.active_frame.destroy()
        self.active_frame = LongestRepetitiveSubstringFinder(self)
        self.active_frame.grid(row=0, column=1, rowspan=4, sticky='nsew')

    def toggle_lcsf(self):
        self._activate_buttons()
        self.lcsf_btn.configure(state='disabled')

        self.active_frame.destroy()
        self.active_frame = LongestCommonSubstringFinder(self)
        self.active_frame.grid(row=0, column=1, rowspan=4, sticky='nsew')

    def toggle_lpf(self):
        self._activate_buttons()
        self.lpf_btn.configure(state='disabled')

        self.active_frame.destroy()
        self.active_frame = LongestPalindromeFinder(self)
        self.active_frame.grid(row=0, column=1, rowspan=4, sticky='nsew')


root = tk.Tk()
root.resizable(False, False)
app = Application(master=root)
app.mainloop()
