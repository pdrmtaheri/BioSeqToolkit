import os
import tkinter as tk
from tkinter import filedialog


class InputDialog(object):
    def __init__(self, master):
        self.toplevel = tk.Toplevel(master)

        self.input_txt = self.create_input()
        self.browse_btn = self.create_browse_button()
        self.done_btn = self.create_done_button()

        self.data_file = None
        self.data = None

    def create_input(self):
        input_txt = tk.Text(self.toplevel)
        input_txt.pack(side='top')

        return input_txt

    def create_browse_button(self):
        browse_btn = tk.Button(self.toplevel)
        browse_btn['text'] = 'Choose File'
        browse_btn['command'] = self.open_choose_file_dialog
        browse_btn.pack(side='top')

        return browse_btn

    def create_done_button(self):
        done_btn = tk.Button(self.toplevel)
        done_btn['text'] = 'Done'
        done_btn['command'] = self.done
        done_btn.pack(side='top')

        return done_btn

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
            print('File not found')

    def show(self):
        self.toplevel.deiconify()
        self.toplevel.wait_window()
        return self.data
