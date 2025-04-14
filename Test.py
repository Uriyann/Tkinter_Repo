import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create main frame
frame = ttk.LabelFrame(root, text="User Information", padding=10)
frame.grid(padx=20, pady=20)

# Labels and entry widgets
ttk.Label(frame, text="First Name:").grid(row=0, column=0, sticky="e", padx=5, pady=2)
ttk.Entry(frame).grid(row=0, column=1, padx=5, pady=2)

ttk.Label(frame, text="Middle Name:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
ttk.Entry(frame).grid(row=1, column=1, padx=5, pady=2)

ttk.Label(frame, text="Last Name:").grid(row=2, column=0, sticky="e", padx=5, pady=2)
ttk.Entry(frame).grid(row=2, column=1, padx=5, pady=2)

# Separator
separator = ttk.Separator(frame, orient='horizontal')
separator.grid(row=3, column=0, columnspan=2, sticky="ew", pady=10)

# Allow column 1 to expand (column with entries)
frame.columnconfigure(1, weight=1)

root.mainloop()
