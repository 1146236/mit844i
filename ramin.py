#MARKET
import tkinter as tk
from tkinter import ttk

# Updated product list (name, price)
products = [
    ("Bread", 0.7),
    ("Milk", 1.2),
    ("Eggs", 2.3),
    ("Butter", 4.0),
    ("Cheese", 3.5),
    ("Sausage", 5.0),
    ("Rice", 2.0),
    ("Macaroni", 1.5),
    ("Sugar", 1.8),
    ("Tea", 2.6),
]

# Main window
root = tk.Tk()
root.title("Product List")

# Variables for checkboxes
vars = []
for name, price in products:
    var = tk.BooleanVar()
    chk = tk.Checkbutton(root, text=name, variable=var)
    chk.pack(anchor="w")
    vars.append((var, name, price))

# ✅ Select all function
def select_all():
    for var, _, _ in vars:
        var.set(True)

# ✅ Show selected products and total price
def show_prices():
    selected = [(name, price) for var, name, price in vars if var.get()]
    
    if not selected:
        return

    total = sum(price for _, price in selected)

    win = tk.Toplevel(root)
    win.title("Selected Products and Prices")

    text_widget = tk.Text(win, height=14, width=35, font=("Segoe UI", 10))
    text_widget.pack(padx=10, pady=10)

    for name, price in selected:
        text_widget.insert(tk.END, f"{name}: {price:.2f} AZN\n")

    text_widget.insert(tk.END, f"\nTotal Price: {total:.2f} AZN")
    text_widget.config(state="disabled")

    ttk.Button(win, text="OK", command=win.destroy).pack(pady=(0, 10))

# ✅ Show only total price (on Enter)
def show_total(event=None):
    total = sum(price for var, _, price in vars if var.get())

    if total == 0:
        return

    win = tk.Toplevel(root)
    win.title("Total Price")
    lbl = tk.Label(win, text=f"Total Price: {total:.2f} AZN", font=("Segoe UI", 11, "bold"))
    lbl.pack(padx=20, pady=20)
    ttk.Button(win, text="OK", command=win.destroy).pack(pady=(0, 10))

# 🔘 Select All button
select_all_button = tk.Button(root, text="Select All", command=select_all)
select_all_button.pack(pady=5)

# 🔘 Price button
price_button = tk.Button(root, text="Price", command=show_prices)
price_button.pack(pady=5)

# ⌨️ Enter key shows total price
root.bind("<Return>", show_total)

# Start the application
root.mainloop()
