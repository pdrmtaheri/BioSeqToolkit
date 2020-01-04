from tkinter import filedialog, messagebox


def output(data, out_filename):
    save_dir = filedialog.askdirectory()
    if not save_dir:
        messagebox.showerror(title='Bad directory', message='No directory selected')
        return

    with open(f'{save_dir}/{out_filename}', 'w') as out:
        out.write(data)
