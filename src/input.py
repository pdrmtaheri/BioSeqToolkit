import os
import tkinter as tk
from tkinter import filedialog, messagebox


class InputDialog(object):
    def __init__(self, master):
        self.toplevel = tk.Toplevel(master)

        self.input_txt = tk.Text(master=self.toplevel)
        self.input_txt.pack()

        self.browse_btn = tk.Button(
            master=self.toplevel, text='Choose File', command=self.open_choose_file_dialog)
        self.browse_btn.pack()

        self.done_btn = tk.Button(
            master=self.toplevel, text='Done', command=self.done)
        self.done_btn.pack()

        self.data_file = None
        self.data = None

    def done(self):
        if self.data_file is not None:
            self.data = self.data_file.read()
        else:
            self.data = self.input_txt.get(1.0, tk.END)

        self.toplevel.destroy()

    def open_choose_file_dialog(self):
        filename = filedialog.askopenfilename(parent=self.toplevel)
        try:
            self.data_file = open(filename, 'r')
        except FileNotFoundError:
            messagebox.showwarning(title='Bad file', message='No files selected')

    def show(self):
        self.toplevel.deiconify()
        self.toplevel.wait_window()
        return self.data
