import os
import tkinter as tk
from tkinter import filedialog, messagebox


class FileTypeBinder:
    def __init__(self, root):
        self.root = root
        self.root.title("FileTypeBinder - File Association Editor")
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        # Widgets
        tk.Label(root, text="File Extension (e.g., .txt):", font=("Arial", 12)).pack(pady=10)
        self.extension_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.extension_entry.pack(pady=5)

        tk.Label(root, text="Associated Program:", font=("Arial", 12)).pack(pady=10)
        self.program_path = tk.Entry(root, font=("Arial", 12), width=30)
        self.program_path.pack(pady=5)

        browse_button = tk.Button(root, text="Browse", font=("Arial", 10), command=self.browse_program)
        browse_button.pack(pady=5)

        bind_button = tk.Button(root, text="Bind Association", font=("Arial", 12), command=self.bind_association)
        bind_button.pack(pady=10)

        remove_button = tk.Button(root, text="Remove Association", font=("Arial", 12), command=self.remove_association)
        remove_button.pack(pady=10)

    def browse_program(self):
        program = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe"), ("All Files", "*.*")])
        if program:
            self.program_path.delete(0, tk.END)
            self.program_path.insert(0, program)

    def bind_association(self):
        ext = self.extension_entry.get().strip()
        program = self.program_path.get().strip()

        if not ext.startswith("."):
            messagebox.showerror("Error", "File extension must start with a dot (e.g., .txt).")
            return

        if not program or not os.path.isfile(program):
            messagebox.showerror("Error", "Please provide a valid program path.")
            return

        try:
            os.system(f'assoc {ext}={ext[1:].upper()}File')
            os.system(f'ftype {ext[1:].upper()}File="{program}" "%1"')
            messagebox.showinfo("Success", f"Association created for {ext} with {program}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create association: {e}")

    def remove_association(self):
        ext = self.extension_entry.get().strip()

        if not ext.startswith("."):
            messagebox.showerror("Error", "File extension must start with a dot (e.g., .txt).")
            return

        try:
            os.system(f'assoc {ext}=')
            os.system(f'ftype {ext[1:].upper()}File=')
            messagebox.showinfo("Success", f"Association removed for {ext}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to remove association: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileTypeBinder(root)
    root.mainloop()
