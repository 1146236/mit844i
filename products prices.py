import tkinter as tk
products = ['Şokolad', 'Yumurta', 'Yağ', 'Çörək', 'Duz', 'Alma', 'Banan', 'Kələm', 'Şəkər Tozu', 'Pendir']
prices = [2, 3, 6, 1, 1, 2.50, 3, 1.40, 3.20, 9]

def show_prices():
    price_label.config(text="Qiymətlər:\n")
    for i in range(len(products)):
        if checkboxes[i].get() == 1:
            price_label.config(text=price_label.cget("text") + f"{products[i]}: {prices[i]} AZN\n")

#ümumi qiyməti hesablamaq
def calculate_total():
    total = 0
    for i in range(len(products)):
        if checkboxes[i].get() == 1:
            total += prices[i]
    total_label.config(text=f"Ümumi qiymət: {total} AZN")

root = tk.Tk()
root.title("Məhsul Seçimi")

checkboxes = []

#Məhsulları əlavə etmək
for i in range(len(products)):
    var = tk.IntVar()
    checkbox = tk.Checkbutton(root, text=products[i], variable=var)
    checkbox.grid(row=i, column=0, sticky='w')
    checkboxes.append(var)

# Qiymətlər üçün button
price_button = tk.Button(root, text="Price", command=show_prices)
price_button.grid(row=len(products), column=0)

#Ümumi qiymət
total_label = tk.Label(root, text="Ümumi qiymət: 0 AZN")
total_label.grid(row=len(products) + 1, column=0)

#Enter 
enter_button = tk.Button(root, text="Enter", command=calculate_total)
enter_button.grid(row=len(products) + 2, column=0)

# Qiymətləri göstərmək üçün yeni label
price_label = tk.Label(root, text="Qiymətlər:\n")
price_label.grid(row=len(products) + 3, column=0)

#Pəncərəni başlatmaq
root.mainloop()
