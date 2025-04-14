import tkinter as tk
from tkinter import messagebox


# ----------------------- GUI ---------------------------------
root = tk.Tk()
root.title("🏬 GPU MARKET")
root.geometry("850x450")
root.configure(bg="#363763")
# -------------------------------------------------------------


# ----------------------- COLOR PALETTE -----------------------
BG_MAIN = "#2d2e52"
TEXT_MAIN = "#ffffff"
BUTTON_MAIN = "#2d2e52"
BORDER = "#ffffff"
# -------------------------------------------------------------


# ----------------------- GPU's -------------------------------
products = {
    "🖥️RTX 5090 : 32 GB GDDR7      ": 1499,
    "🖥️RTX 5080 : 16 GB GDDR7      ": 1249,
    "🖥️RTX 5070 Ti : 16 GB GDDR7  ": 1099,
    "🖥️RTX 5070 : 12 GB GDDR7      ": 999,
    "🖥️RTX 4090 : 24 GB GDDR6x    ": 1199,
    "🖥️RTX 4080 : 16 GB GDDR6x    ": 899,
    "🖥️RTX 4070 Ti : 12 GB GDDR6x": 599,
    "🖥️RTX 4070 : 12 GB GDDR6x    ": 499,
    "🖥️RTX 4060 Ti : 8 GB GDDR6    ": 399,
    "🖥️RTX 4060 : 8 GB GDDR6        ": 299
}

selected = {}
quantities = {}
# -------------------------------------------------------------


# ----------------------- GPU Title ---------------------------
tk.Label(root, text="List of GPU's", font=("Arial", 16, "bold"),
         fg=TEXT_MAIN, bg=BG_MAIN).place(x=50, y=20)
# -------------------------------------------------------------

def decrease(qty): 
    qty.set(max(1, qty.get() - 1))
    updateCart()

def increase(qty): 
    qty.set(qty.get() + 1)
    updateCart()

# ----------------------- GPU List -------------------------
y_offset = 70
for name, price in products.items():
    var = tk.IntVar()
    qty = tk.IntVar(value=1)

    cb = tk.Checkbutton(root, text=f"{name}    -    ${price:.2f}", variable=var,
                        command=lambda: updateCart(),
                        bg=BG_MAIN, fg=TEXT_MAIN,
                        activebackground=BG_MAIN, selectcolor=BG_MAIN,
                        font=("Arial", 11))
    cb.place(x=50, y=y_offset)

    tk.Button(root, text="-", width=3, height=1, font=("Arial", 10),
              bg=BUTTON_MAIN, fg="white", command=lambda q=qty: decrease(q)).place(x=420, y=y_offset)

    tk.Label(root, textvariable=qty, width=3, font=("Arial", 11),
             bg=BG_MAIN, fg=TEXT_MAIN).place(x=460, y=y_offset)

    tk.Button(root, text="+", width=3, height=1, font=("Arial", 10),
              bg=BUTTON_MAIN, fg="white", command=lambda q=qty: increase(q)).place(x=500, y=y_offset)
    
    selected[name] = var
    quantities[name] = qty
    y_offset += 35
# --------------------------------------------------------------


# -------------------- Cart Title ------------------------------
tk.Label(root, text="Cart", font=("Arial", 14, "bold"),
         bg=BG_MAIN, fg=TEXT_MAIN).place(x=660, y=30)
# --------------------------------------------------------------


# --------------------- Cart Box -------------------------------
cart_box = tk.Text(root, width=30, height=21, state="disabled",
                   bg=BG_MAIN, fg=TEXT_MAIN, font=("Arial", 10),
                   highlightbackground=BORDER, highlightthickness=2)
cart_box.place(x=580, y=70)
# --------------------------------------------------------------


# --------------------- Update Cart ----------------------------
def updateCart():
    cart_box.config(state="normal")
    cart_box.delete(1.0, tk.END)
    total = 0

    for name in selected:
        if selected[name].get() == 1:
            qty = quantities[name].get()
            price = products[name]
            line_total = qty * price
            total += line_total
            cart_box.insert(tk.END, f"{name}\n  x{qty} = ${line_total:.2f}\n\n")

    cart_box.insert(tk.END, f"Total: ${total:.2f}")
    cart_box.config(state="disabled")
# --------------------------------------------------------------


# --------------------- Show Total -----------------------------
def showTotal():
    total = 0
    for name in selected:
        if selected[name].get() == 1:
            qty = quantities[name].get()
            total += products[name] * qty
    messagebox.showinfo("Total Price", f"Total amount: ${total:.2f}\n\nThanks for shopping")
    root.destroy()
# --------------------------------------------------------------


# --------------------- Enter Button ---------------------------
tk.Button(root, text="Enter", font=("Arial", 12, "bold"),
          bg=BUTTON_MAIN, fg=BORDER, width=20, height=2,
          command=showTotal).place(x=583, y=358)
# --------------------------------------------------------------


# ---------------------- Start GUI -----------------------------
root.mainloop()
# --------------------------------------------------------------
