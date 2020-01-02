import tkinter as tk

from src.longest_common_substring_finder import LongestCommonSubstringFinder
from src.longest_palindrome_finder import LongestPalindromeFinder
from src.longest_repetitive_substring_finder import \
    LongestRepetitiveSubstringFinder
from src.pattern_finder import PatternFinder


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.create_pattern_finder_button()
        self.create_longest_palindrome_finder_button()
        self.create_longest_common_substring_finder_button()
        self.create_longest_repeptivie_substring_finder_button()

        self.pack()

    def create_pattern_finder_button(self):
        btn = tk.Button(self)
        btn['text'] = 'Pattern Finder'
        btn['command'] = lambda: PatternFinder(
            tk.Toplevel(master=self))
        btn.pack()

        return btn

    def create_longest_repeptivie_substring_finder_button(self):
        btn = tk.Button(self)
        btn['text'] = 'Longest Repetitive Substring Finder'
        btn['command'] = lambda: LongestRepetitiveSubstringFinder(
            tk.Toplevel(master=self))
        btn.pack()

        return btn

    def create_longest_common_substring_finder_button(self):
        btn = tk.Button(self)
        btn['text'] = 'Longest Common Substring Finder'
        btn['command'] = lambda: LongestCommonSubstringFinder(
            tk.Toplevel(master=self))
        btn.pack()

        return btn

    def create_longest_palindrome_finder_button(self):
        btn = tk.Button(self)
        btn['text'] = 'Longest Palindrome Finder'
        btn['command'] = lambda: LongestPalindromeFinder(
            tk.Toplevel(master=self))
        btn.pack()

        return btn


root = tk.Tk()
app = Application(master=root)
app.mainloop()
