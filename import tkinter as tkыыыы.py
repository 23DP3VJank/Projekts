import tkinter as tk
from tkinter import ttk

history = []

def convert():
    try:
        amount = float(entry_amount.get())
        rates = {"USD": 1.08, "EUR": 1.0, "GBP": 0.85, "JPY": 145.0, "CAD": 1.36, "AUD": 1.55, "RUB": 90.0}
        result = amount * rates[combo_to.get()] / rates[combo_from.get()]
        label_result.config(text=f"Result: {result:.2f} {combo_to.get()}")
        
        history.append(f"{amount:.2f} {combo_from.get()} -> {result:.2f} {combo_to.get()}")
    except:
        label_result.config(text="Error!")

def show_rates():
    rates = {"USD": 1.08, "EUR": 1.0, "GBP": 0.85, "JPY": 145.0, "CAD": 1.36, "AUD": 1.55, "RUB": 90.0}
    rate_info = "\n".join([f"{currency}: {rate}" for currency, rate in rates.items()])
    label_rates.config(text=f"Currency Rates:\n{rate_info}")

def show_history():
    if history:
        history_info = "\n".join(history)
    else:
        history_info = "No history yet."
    label_history.config(text=f"Conversion History:\n{history_info}")

root = tk.Tk()
root.title("Converter")
root.geometry("400x490")

entry_amount = tk.Entry(root)
entry_amount.pack(pady=5)

combo_from = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "RUB"], state="readonly")
combo_from.pack(pady=5)
combo_from.set("USD")

combo_to = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "RUB"], state="readonly")
combo_to.pack(pady=5)
combo_to.set("EUR")

button_convert = tk.Button(root, text="Convert", command=convert)
button_convert.pack(pady=10)

button_show_rates = tk.Button(root, text="Show Rates", command=show_rates)
button_show_rates.pack(pady=5)

button_show_history = tk.Button(root, text="Show History", command=show_history)
button_show_history.pack(pady=5)

label_result = tk.Label(root, text="Result:")
label_result.pack(pady=10)

label_rates = tk.Label(root, text="Currency Rates:")
label_rates.pack(pady=5)

label_history = tk.Label(root, text="Conversion History:")
label_history.pack(pady=5)

root.mainloop()
