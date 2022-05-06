from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile


file_name = None

def new_file():
    global file_name
    file_name = 'Без названия'
    text.delete('1.0', END)


def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', END)
    try:
        out.write(data.strip())
    except Exception:
        messagebox.showerror('Извините Вы ошиблись! Нельзя сохранить файл')


def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        file_name = inp.name
        return file_name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)


root = Tk()
root.title('Заметки для Python')
root.geometry("700x700")

text = Text(root, width=700, height=700)
text.pack()

menu_bar = Menu(root)
file_menu = Menu(menu_bar)

file_menu.add_command(label='Новая заметка', command=new_file)
file_menu.add_command(label='Открыть документ', command=open_file)
file_menu.add_command(label='Сохранить документ', command=save_as)
menu_bar.add_cascade(label='Файл', menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()