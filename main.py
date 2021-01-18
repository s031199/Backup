import tkinter as tk

from Log_structure import *

window = tk.Tk(className=" UVS Script")
window.geometry("450x300")
window.resizable(width=False, height=False)
window.wm_attributes("-topmost", 1)
window.lift()

textarea = tk.Text()
textarea.place(x=10, y=100, width=420, height=150)

print(u"\uA789")

def folderdublicate():
	textarea.insert(tk.END, "-------------------Folder Backup--------------------\n")
	textarea.insert(tk.END, logShowDirectory())
	os.chdir('A:\python darbai')
	textarea.insert(tk.END, logShowDirectory())
	textarea.insert(tk.END, logCopyFolder())


folderBackupButton = tk.Button(window, text='Duplicate: ', command=lambda: folderdublicate())
folderBackupButton.place(x=10, y=10)


def fileupdate():
	textarea.insert(tk.END, "-------------------Config Update--------------------\n")
	textarea.insert(tk.END, mainfolderexist())
	textarea.insert(tk.END, configfileexist())


B = tk.Button(text="Update", command=lambda: fileupdate())
B.place(x=360, y=10)

window.mainloop()
