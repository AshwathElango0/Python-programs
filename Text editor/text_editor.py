# Necessary imports
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Function to open a file for editing"""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as in_file:
        text = in_file.read()
        txt_edit.insert(tk.END, text)   # Reading and inserting existing text in the file into the window
    window.title(f"NeoTextEditor - {filepath}")

def save_file():
    """Function to save a file after editing"""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as out_file:
        text = txt_edit.get(1.0, tk.END)
        out_file.write(text)     # Writing newly edited contents of file back into the file being edited
    window.title(f"NeoTextEditor - {filepath}")

window = tk.Tk()    # Creating and configuring main UI window
window.title("NeoTextEditor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)    # Configuring size for the text editing area

# Creating buttons and text editing panel
txt_edit = tk.Text(window)
frame_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
open_button = tk.Button(frame_buttons, text="Open", command=open_file)
save_button = tk.Button(frame_buttons, text="Save As...", command=save_file)

open_button.grid(row=0, column=0, sticky="ew", padx=20, pady=20)     # Positioning elements in UI
save_button.grid(row=1, column=0, sticky="ew", padx=20)

frame_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()