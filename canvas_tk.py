import tkinter as tk
import psutil

root = tk.Tk()


# text = psutil.cpu_percent(0.2)
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()


def delete_can(el):
    canvas.delete(el)


def label_reload():
    text = canvas.create_text(50, 50, text=f'{psutil.cpu_percent(0.2)}', fill='red', font=('Times', 30))
    canvas.configure()
    canvas.after(400, label_reload)


label_reload()
root.mainloop()
