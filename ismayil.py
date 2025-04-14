import tkinter as tk
from tkinter import messagebox, Toplevel, scrolledtext
from datetime import datetime

products = [
    ("Un (1kg)", 1.2),
    ("Düyü (1kg)", 2.0),
    ("Makaron", 1.0),
    ("Kartof (1kg)", 0.8),
    ("Soğan (1kg)", 0.7),
    ("Tomat pastası", 1.5),
    ("Yumurta (10 ədəd)", 2.2),
    ("Yağ (1L)", 3.0),
    ("Süd (1L)", 1.3),
    ("Pendır (500g)", 4.0),
    ("Toyuq əti (1kg)", 5.0),
    ("Mal əti (1kg)", 9.0),
    ("Noxud (1kg)", 1.8),
    ("Lobya (1kg)", 2.0),
    ("Qənd (1kg)", 1.1),
    ("Çay (200g)", 2.5),
    ("Kofe (100g)", 3.2),
    ("Şokolad", 1.4),
    ("Keks", 0.9),
    ("Su (1.5L)", 0.5)
]

selected_vars = []  
quantity_vars = [] 

window = tk.Tk()
window.title("Ərzaq Mağazası")
window.geometry("500x700")

header = tk.Label(window, text="Ərzaqları seçin:", font=("Arial", 16))
header.pack(pady=10)

products_frame = tk.Frame(window)
products_frame.pack(pady=5)

for name, price in products:
    row = tk.Frame(products_frame)
    row.pack(anchor="w", pady=2, padx=5)
    label = tk.Label(row, text=f"{name} - {price} AZN")
    label.pack(side=tk.LEFT)
    var = tk.BooleanVar()
    selected_vars.append(var)
    chk = tk.Checkbutton(row, variable=var)
    chk.pack(side=tk.LEFT, padx=5)
    q_var = tk.IntVar(value=1)
    quantity_vars.append(q_var)
    spin = tk.Spinbox(row, from_=1, to=20, width=5, textvariable=q_var)
    spin.pack(side=tk.LEFT)

total_label = tk.Label(window, text="Ümumi qiymət: 0.00 AZN", font=("Arial", 14, "bold"))
total_label.pack(pady=10)

def calculate_total():
    total = 0
    for sel, (name, price), q_var in zip(selected_vars, products, quantity_vars):
        if sel.get():
            total += price * q_var.get()
    total_label.config(text=f"Ümumi qiymət: {total:.2f} AZN")
    return total

def reset_selections():
    for sel, q_var in zip(selected_vars, quantity_vars):
        sel.set(False)
        q_var.set(1)
    total_label.config(text="Ümumi qiymət: 0.00 AZN")

def confirm_order():
    order_total = calculate_total()
    order_lines = []
    for sel, (name, price), q_var in zip(selected_vars, products, quantity_vars):
        if sel.get():
            qty = q_var.get()
            item_total = price * qty
            order_lines.append(f"{name} - {qty} ədəd - {item_total:.2f} AZN")
    if not order_lines:
        messagebox.showwarning("Diqqət", "Zəhmət olmasa məhsul seçin.")
        return
    now = datetime.now()
    order_time = now.strftime("%d.%m.%Y %H:%M")
    
    summary_win = Toplevel(window)
    summary_win.title("Sifariş Xülasəsi")
    summary_win.geometry("400x400")
    summary_text = scrolledtext.ScrolledText(summary_win, width=45, height=20, font=("Arial", 11))
    summary_text.pack(pady=10, padx=10)
    summary_text.insert(tk.END, "Sifariş etdiyiniz məhsullar:\n\n")
    summary_text.insert(tk.END, "\n".join(order_lines))
    summary_text.insert(tk.END, f"\n\nÜmumi məbləğ: {order_total:.2f} AZN")
    summary_text.insert(tk.END, f"\nTarix və saat: {order_time}")
    summary_text.configure(state='disabled')
    
    try:
        with open("sifarishler.txt", "a", encoding="utf-8") as f:
            f.write(f"\nSifariş tarixi: {order_time}\n")
            f.write("\n".join(order_lines) + "\n")
            f.write(f"Ümumi məbləğ: {order_total:.2f} AZN\n")
            f.write("-" * 40 + "\n")
    except Exception as e:
        messagebox.showerror("Xəta", f"Fayla yazılarkən xəta baş verdi: {e}")

buttons_frame = tk.Frame(window)
buttons_frame.pack(pady=10)

confirm_button = tk.Button(buttons_frame, text="Səbəti təsdiqlə", command=lambda: [calculate_total(), confirm_order()], bg="green", fg="white", font=("Arial", 12), padx=10, pady=5)
confirm_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(buttons_frame, text="Sifarişi sıfırla", command=reset_selections, bg="red", fg="white", font=("Arial", 12), padx=10, pady=5)
reset_button.pack(side=tk.LEFT, padx=5)

for var in selected_vars:
    var.trace("w", lambda *args: calculate_total())

window.mainloop()
