import tkinter as tk
from tkinter import ttk

def convert():
    try:
        amount = float(entry_amount.get())
        rates = {"USD": 1.08, "EUR": 1.0, "GBP": 0.85}
        result = amount * rates[combo_to.get()] / rates[combo_from.get()]
        label_result.config(text=f"Result: {result:.2f} {combo_to.get()}")
    except:
        label_result.config(text="Error!")

root = tk.Tk()
root.title("Converter")
root.geometry("300x250")

entry_amount = tk.Entry(root)
entry_amount.pack(pady=5)

combo_from = ttk.Combobox(root, values=["USD", "EUR", "GBP"], state="readonly")
combo_from.pack(pady=5)
combo_from.set("USD")

combo_to = ttk.Combobox(root, values=["USD", "EUR", "GBP"], state="readonly")
combo_to.pack(pady=5)
combo_to.set("EUR")

button = tk.Button(root, text="Convert", command=convert)
button.pack(pady=10)

label_result = tk.Label(root, text="Result:")
label_result.pack(pady=10)

root.mainloop()
