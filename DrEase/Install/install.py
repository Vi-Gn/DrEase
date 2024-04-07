import tkinter as tk
import tkinter.filedialog as fd
import tkinter.ttk as ttk
import os

def Choose(etr: ttk.Entry):
  tempDir = fd.askdirectory()
  if tempDir != "":
    etr.delete(0,"end")
  etr.insert(0,tempDir)

def Install(etr: ttk.Entry):
  path = etr.get()
  if path == "":
    raise "Label is empty!"
  path = os.path.abspath(path)
  
  f = open("pathToInstall.txt", "w")
  f.write(path+"\\")
  f.close()
  # os.system("call ..\\Source\\Build.bat")
  os.system("start script.bat")
  # absPath = os.path.abspath("")
  # os.chdir("..\\Source")
  # os.startfile("Build.bat")
  # os.chdir(absPath)
  # os.startfile("script.bat")
  
  
  
root = tk.Tk()
root.title("Install Path")
root.minsize(width=400, height=100)
root.grid_columnconfigure(0, minsize=50)
root.grid_columnconfigure(1, weight=9)
root.grid_columnconfigure(2, minsize=50)
root.grid_rowconfigure(0, minsize=50)
root.grid_rowconfigure(1, minsize=30)
root.grid_rowconfigure(2, minsize=30)

ttk.Label(root, text="Path :").grid(column=0, row=0, sticky="nsew")
entry = ttk.Entry(root)
entry.grid(column=1, row=0, sticky="nsew", padx=2, pady=10)

ttk.Button(root, padding=0, text="Browse", command=lambda etr=entry :Choose(etr)).grid(column=2, row=0, sticky="nsew", padx=2, pady=8)

ttk.Button(root, text="Install", command=lambda etr=entry, rootRef=root :[Install(etr), rootRef.destroy()]).grid(column=1, row=1)
ttk.Button(root, text="Quit", command=lambda rootRef=root :rootRef.destroy()).grid(column=1, row=2)


style =ttk.Style()
style.theme_use("vista")

root.mainloop()