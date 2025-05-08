import tkinter as tk
from tkinter import ttk
from datetime import datetime

history = []

def convert():
    try:
        amount = float(entry_amount.get())
        rates = {"USD": 1.08, "EUR": 1.0, "GBP": 0.85, "JPY": 145.0, "CAD": 1.36, "AUD": 1.55, "KRW": 1460.0}
        result = amount * rates[combo_to.get()] / rates[combo_from.get()]
        label_result.config(text=f"Result: {result:.2f} {combo_to.get()}")

        date = datetime.now().strftime("%d.%m.%Y") 
        history.append(f"{date} | {amount:.2f} {combo_from.get()} -> {result:.2f} {combo_to.get()}")
    except:
        label_result.config(text="Error!")

def show_rates():
    rates = {"USD": 1.08, "EUR": 1.0, "GBP": 0.85, "JPY": 145.0, "CAD": 1.36, "AUD": 1.55, "KRW": 1460.0}
    text = "\n".join(f"{currency}: {rate}" for currency, rate in rates.items())
    label_rates.config(text="Currency Rates:\n" + text)

def show_history():
    if history:
        text = "\n".join(history)
    else:
        text = "No history yet."
    label_history.config(text="Conversion History:\n" + text)

def search_by_date():
    date = entry_date.get()
    matches = [record for record in history if record.startswith(date)]

    if matches:
        text = "\n".join(matches)
    else:
        text = "No records for this date."

    label_history.config(text="Conversion History:\n" + text)


root = tk.Tk()
root.title("Converter")
root.geometry("400x600")

entry_amount = tk.Entry(root)
entry_amount.pack(pady=5)

combo_from = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "KRW"], state="readonly")
combo_from.pack(pady=5)
combo_from.set("USD")

combo_to = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "KRW"], state="readonly")
combo_to.pack(pady=5)
combo_to.set("EUR")


button_convert = tk.Button(root, text="Convert", command=convert)
button_convert.pack(pady=5)

button_show_rates = tk.Button(root, text="Show Rates", command=show_rates)
button_show_rates.pack(pady=5)

button_show_history = tk.Button(root, text="Show History", command=show_history)
button_show_history.pack(pady=5)

entry_date = tk.Entry(root)
entry_date.pack(pady=5)
entry_date.insert(0, "DD.MM.YY")  

button_search_date = tk.Button(root, text="Search by Date", command=search_by_date)
button_search_date.pack(pady=5)

label_result = tk.Label(root, text="Result:")
label_result.pack(pady=10)

label_rates = tk.Label(root, text="Currency Rates:")
label_rates.pack(pady=5)

label_history = tk.Label(root, text="Conversion History:")
label_history.pack(pady=5)

root.mainloop()
