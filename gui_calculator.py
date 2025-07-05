import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

expression = ""
input_text = tk.StringVar()

def update_display(value):
    global expression
    expression += value
    input_text.set(expression)

def clear_display():
    global expression
    expression = ""
    input_text.set(expression)

def calculate_result():
    global expression
    try:
        result =str(eval(expression))
        input_text.set(result)
        expression = result
    except Exception:
        input_text.set("Error")
        expression = ""

root.configure(bg="white")

input_text = tk.StringVar()

input_frame = tk.Frame(root, width=312, height=50, bd=0)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('Arial', 18), textvariable=input_text, bd=0, width=15, bg="#eee", fg="black", justify='right')
input_field.grid(row=0, column=0)
input_field.pack(ipady=10,padx=5, pady=5)

btns_frame = tk.Frame(root, bg='white')
btns_frame.pack()

button_specs = [
    [("C", clear_display), ("/", lambda: update_display("/")), ("*", lambda: update_display("*")), ("-", lambda: update_display("-"))],
    [("7", lambda: update_display("7")), ("8", lambda: update_display("8")), ("9", lambda: update_display("9")), ("+", lambda: update_display("+"))],
    [("4", lambda: update_display("4")), ("5", lambda: update_display("5")), ("6", lambda: update_display("6"))],
    [("1", lambda: update_display("1")), ("2", lambda: update_display("2")), ("3", lambda: update_display("3"))],
    [("0", lambda: update_display("0")), (".", lambda: update_display(".")), ("=", calculate_result)]
]

for row_index, row in enumerate(button_specs):
    for col_index, (label, command) in enumerate(row):
        button = tk.Button(
            btns_frame, text=label, fg="black", width=10, height=3, bg="#f0f0f0" 
            if label not in {"C", "="} else "#ff8080" 
            if label == "C" else "#80ff80",
            cursor="hand2",
            command=command
        )
        button.grid(row=row_index, column=col_index, padx=1, pady=1)

btns_frame.grid_columnconfigure(0, weight=1)
btns_frame.grid_columnconfigure(1, weight=1)
btns_frame.grid_columnconfigure(2, weight=1)
btns_frame.grid_columnconfigure(3, weight=1)

tk.Button(btns_frame, text="", state="disabled", width=10, height=3, bg="#f0f0f0").grid(row=2, column=3, padx=1, pady=1)
tk.Button(btns_frame, text="", state="disabled", width=10, height=3, bg="#f0f0f0").grid(row=3, column=3, padx=1, pady=1)

root.mainloop()