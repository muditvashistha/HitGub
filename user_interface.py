import tkinter as tk
from tkinter import ttk

def launch_ui(on_add_checkpoint, on_revert):
    root = tk.Tk()
    root.title("HitGub")
    root.iconbitmap("HitGub.ico")
    root.geometry("400x300")
    root.configure(bg="#1e1e2e")
    root.resizable(False, False)

    style = ttk.Style()
    style.theme_use("default")
    style.configure("TButton",
                    font=("Segoe UI", 12, "bold"),
                    padding=10,
                    background="#89b4fa",
                    foreground="#11111b")
    style.map("TButton", background=[("active", "#89b4fa")])

    
   

    header = tk.Label(root, text="HitGub",
                      font=("Segoe UI", 14, "bold"),
                      bg="#1e1e2e",fg="white")
    header.pack(pady=20)

    button_frame = tk.Frame(root,background="#1e1e2e")
    button_frame.pack(pady=10)


    btn_add = ttk.Button(button_frame, text="✅ Add Checkpoint", width=30, command=on_add_checkpoint)
    btn_add.grid(row=0, column=0, pady=10)

    btn_revert = ttk.Button(button_frame, text="◀️ Revert to Most Recent", width=30, command=on_revert)
    btn_revert.grid(row=1, column=0, pady=10)

   

    root.mainloop()



