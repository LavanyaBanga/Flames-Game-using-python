import tkinter as tk
from tkinter import messagebox
def flames_game(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)
    
    count = len(name1) + len(name2)
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    
    while len(flames) > 1:
        idx = (count % len(flames) - 1)
        if idx >= 0:
            right = flames[idx + 1:]
            left = flames[:idx]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    
    return flames[0]

def check_relationship():
    name1 = entry1.get()
    name2 = entry2.get()
    
    if name1.strip() == "" or name2.strip() == "":
        messagebox.showerror("Error", "Please enter both names.")
        return
    
    result = flames_game(name1, name2)
    messagebox.showinfo("Result", f"The relationship between {name1} and {name2} is: {result}")

# GUI setup
root = tk.Tk()
root.title("Flames Game")

frame = tk.Frame(root, bg="white")
frame.pack(padx=20, pady=20)

label_title = tk.Label(frame, text="Flames Game", font=("Arial", 18), bg="white")
label_title.grid(row=0, columnspan=2, pady=10)

label1 = tk.Label(frame, text="Enter Name 1:", bg="white")
label1.grid(row=1, column=0, padx=10, pady=5)

entry1 = tk.Entry(frame)
entry1.grid(row=1, column=1, padx=10, pady=5)
label2 = tk.Label(frame, text="Enter Name 2:", bg="white")
label2.grid(row=2, column=0, padx=10, pady=5)

entry2 = tk.Entry(frame)
entry2.grid(row=2, column=1, padx=10, pady=5)
button = tk.Button(frame, text="Check Relationship", command=check_relationship)
button.grid(row=3, columnspan=2, pady=10)

root.mainloop()