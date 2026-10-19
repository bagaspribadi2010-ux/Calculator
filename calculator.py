import tkinter as tk

def press(button):
    if button == "=":
        try:
            expression = display.get().replace("x", "*").replace(":", "/")
            display.set(str(eval(expression)))
        except Exception:
            display.set("Error")
    elif button == "C":
        display.set("")
    else:
        display.set(display.get() + button)

window = tk.Tk()
window.title("Sija Calculator")
window.geometry("300x400")
window.iconbitmap("sija-logo.ico")  # Set the window icon

display = tk.StringVar()

screen = tk.Entry(
    window,
    textvariable=display,
    font=("Arial", 20),
    justify="right"
)
screen.pack(fill="x", padx=10, pady=10)

buttons = [
    "7", "8", "9", ":",
    "4", "5", "6", "x",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

button_frame = tk.Frame(window)
button_frame.pack(expand=True, fill="both")

for index, symbol in enumerate(buttons):
    button = tk.Button(
        button_frame,
        text=symbol,
        font=("Arial", 16),
        command=lambda value=symbol: press(value)
    )
    button.grid(
        row=index // 4,
        column=index % 4,
        sticky="nsew",
        padx=5,
        pady=5
    )

for row in range(4):
    button_frame.rowconfigure(row, weight=1)

for column in range(4):
    button_frame.columnconfigure(column, weight=1)

window.mainloop()