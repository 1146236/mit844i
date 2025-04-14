import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Items with their prices per kg/unit
items = {
    "Apples": 3.5,
    "Bananas": 2.0,
    "Potatoes": 1.2,
    "Onions": 1.5,
    "Tomatoes": 2.8,
    "Carrots": 2.0,
    "Cucumbers": 1.7,
    "Peppers": 3.2,
    "Lettuce": 1.0,
    "Garlic": 4.0
}

def update_cart():
    total = 0.0
    cart_lines = []

    for item in items:
        if item_vars[item].get():
            try:
                qty = float(qty_vars[item].get())
                if qty > 0:
                    price = items[item] * qty
                    total += price
                    cart_lines.append(f"{item}: {qty}kg x ${items[item]:.2f} = ${price:.2f}")
            except ValueError:
                cart_lines.append(f"{item}: Invalid quantity")

    cart_text = "\n".join(cart_lines)
    cart_label.config(text=f"Your Cart:\n{cart_text}")
    total_label.config(text=f"Total: ${total:.2f}")

def finish_purchase():
    summary_lines = []
    total = 0.0

    for item in sorted(items):  # sort alphabetically
        if item_vars[item].get():
            try:
                qty = float(qty_vars[item].get())
                if qty > 0:
                    unit_price = items[item]
                    subtotal = unit_price * qty
                    total += subtotal
                    summary_lines.append(f"{item}: {qty}kg x ${unit_price:.2f} = ${subtotal:.2f}")
            except ValueError:
                summary_lines.append(f"{item}: Invalid quantity")

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    summary_text = f"Date: {now}\n\n"
    summary_text += "\n".join(summary_lines)
    summary_text += f"\n\nFinal Total: ${total:.2f}"
    summary_text += "\n\nThanks for your purchase! 🎉"

    # Show popup window with summary
    popup = tk.Toplevel(root)
    popup.title("Purchase Summary")
    popup.geometry("400x400")
    tk.Label(popup, text="🧾 Purchase Summary", font=('Arial', 14, 'bold')).pack(pady=10)
    tk.Label(popup, text=summary_text, justify="left", anchor="w", font=('Arial', 11)).pack(padx=20, anchor="w")

def reset_cart():
    confirm = messagebox.askyesno("Reset Cart", "Are you sure you want to clear the cart?")
    if confirm:
        for item in items:
            item_vars[item].set(False)
            qty_vars[item].set("1")
        update_cart()

# GUI setup
root = tk.Tk()
root.title("Market Cart")
root.geometry("500x750")

tk.Label(root, text="🛒 Select Items to Buy", font=('Arial', 14, 'bold')).pack(pady=10)

item_frame = tk.Frame(root)
item_frame.pack()

item_vars = {}
qty_vars = {}

for item, price in items.items():
    frame = tk.Frame(item_frame)
    frame.pack(anchor='w', pady=4)

    var = tk.BooleanVar()
    item_vars[item] = var

    check = tk.Checkbutton(frame, text=f"{item} - ${price}/kg", variable=var, command=update_cart)
    check.pack(side="left")

    qty_var = tk.StringVar(value="1")
    qty_vars[item] = qty_var

    entry = tk.Entry(frame, textvariable=qty_var, width=5)
    entry.pack(side="left", padx=10)
    entry.bind("<KeyRelease>", lambda e: update_cart())

cart_label = tk.Label(root, text="Your Cart:", justify="left", anchor="w", font=('Arial', 11))
cart_label.pack(pady=20, anchor="w", padx=20)

total_label = tk.Label(root, text="Total: $0.00", font=('Arial', 14, 'bold'))
total_label.pack(pady=10)

tk.Button(root, text="Finish Purchase", font=('Arial', 12), command=finish_purchase).pack(pady=10)
tk.Button(root, text="Reset Cart", font=('Arial', 12), command=reset_cart).pack(pady=10)

root.mainloop()
