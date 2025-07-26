import tkinter as tk
from tkinter import messagebox

def process():
    global night
    try:
        deg = int(entry.get())
        night = var.get() == "night"

        heater = 'off'
        cooler = 'off'
        light = 'on' if night else 'off'

        if deg > 30:
            heater = 'off'
            cooler = 'on'
        else:
            heater = 'on'
            cooler = 'off'

        result = f"heater: {heater}\ncooler: {cooler}\nlight: {light}"
        messagebox.showinfo("Result", result)
        root.destroy()
    except:
        messagebox.showerror("Error", "Please enter a valid number.")

root = tk.Tk()
root.title("Control Panel")
root.geometry("250x200")

label = tk.Label(root, text="Enter temperature:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

var = tk.StringVar(value="night")
tk.Radiobutton(root, text="Night", variable=var, value="night").pack()
tk.Radiobutton(root, text="Day", variable=var, value="day").pack()

tk.Button(root, text="Submit", command=process).pack(pady=10)

root.mainloop()
