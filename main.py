import tkinter as tk

from src.longest_common_substring_finder import LongestCommonSubstringFinder
from src.longest_palindrome_finder import LongestPalindromeFinder
from src.longest_repetitive_substring_finder import \
    LongestRepetitiveSubstringFinder
from src.pattern_finder import PatternFinder


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        pf_btn = tk.Button(master=self, text='Pattern Finder',
                           command=lambda: PatternFinder(tk.Toplevel(master=self)))
        pf_btn.pack()

        lrsf_btn = tk.Button(master=self, text='Longest Repetitive Substring Finder',
                             command=lambda: LongestRepetitiveSubstringFinder(tk.Toplevel(master=self)))
        lrsf_btn.pack()

        lcsf_btn = tk.Button(master=self, text='Longest Common Substring Finder',
                             command=lambda: LongestCommonSubstringFinder(tk.Toplevel(master=self)))
        lcsf_btn.pack()

        lpf_btn = tk.Button(master=self, text='Longest Palindrome Finder',
                            command=lambda: LongestPalindromeFinder(tk.Toplevel(master=self)))
        lpf_btn.pack()

        self.pack()


root = tk.Tk()
app = Application(master=root)
app.mainloop()
