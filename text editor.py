# import tkinter for creating GUI(graphical user interface) app 

import tkinter as tk 
from tkinter import messagebox, filedialog 

# main window code 

root = tk.Tk() 
root.title("TEXT EDITOR") 
root.geometry("800x600") 


#----------------------------------------- CREATE TEXT AREA--------------------------------------------------------------------------------------------- 

text = tk.Text( 
    root,               # parent window 
    wrap=tk.WORD,       # wrap text by word (not character) 
    font=("helvetica", 12)  # FIXED TYPO: "helvetical" -> "helvetica"
) 

# make text area fill entire window 
# FIXED TYPOS: "expend" -> "expand", "file" -> "fill"

text.pack(expand=True, fill=tk.BOTH) 

# main logic start now 
# function 2 - to create a new file 

def new_file(): 
    text.delete(1.0, tk.END) 

# function 2 to open new file 

def open_file(): 
    file_path = filedialog.askopenfilename( 
        defaultextension=".txt", 
        filetypes=[("text file", "*.txt")] 
    ) 

    # open selected file 

    if file_path: 
        with open(file_path, "r") as file: 
            text.delete(1.0, tk.END) 
            text.insert(tk.END, file.read()) 


# function to save file 

def save_file(): 
    file_path = filedialog.asksaveasfilename( 
        filetypes=[("text file", "*.txt")] 
    ) 
    if file_path: 
        with open(file_path, "w") as file: 
            file.write(text.get(1.0, tk.END)) 
        messagebox.showinfo("info", "save file successfully") # FIXED TYPO: "succesfully"

# Menu bar 

menu = tk.Menu(root) 
root.config(menu=menu) 

# FIXED MENU STRUCTURING:
# Create the dropdown sub-menu

file_menu = tk.Menu(menu, tearoff=0) 

# Add choices inside the sub-menu

file_menu.add_command(label="New", command=new_file) 
file_menu.add_command(label="Open", command=open_file) 
file_menu.add_command(label="Save", command=save_file) 
file_menu.add_separator() 
file_menu.add_command(label="Exit", command=root.quit) # FIXED TYPO: "exist" -> "Exit"

# Cascade the sub-menu onto the main menu bar

menu.add_cascade(label="File", menu=file_menu) 

# start and keep window open 

root.mainloop()
