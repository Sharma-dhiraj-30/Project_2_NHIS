import tkinter as tk
import math

# ---------------- Main Window ----------------
app = tk.Tk()
app.title("Scientific Calculator")
app.geometry("380x520")
app.resizable(False, False)
app.configure(bg="#2c3e50")

expression = tk.StringVar()
scientific_mode = False
scientific_buttons = []

# ---------------- Display Screen ----------------
display = tk.Entry(
    app,
    textvariable=expression,
    font=("Arial", 24),
    justify="right",
    bd=8,
    relief="flat",
    bg="white"
)
display.grid(row=0, column=0, columnspan=4, padx=15, pady=20, sticky="nsew")
display.focus()


# ---------------- Basic Operations ----------------
def add_value(value):
    current = expression.get()
    expression.set(current + str(value))


def clear_display(event=None):
    expression.set("")


def delete_last(event=None):
    expression.set(expression.get()[:-1])


def calculate(event=None):
    try:
        result = eval(expression.get())
        expression.set(str(result))
    except:
        expression.set("Error")


def calculate_percentage():
    try:
        result = eval(expression.get()) / 100
        expression.set(str(result))
    except:
        expression.set("Error")


# ---------------- Scientific Functions ----------------
def apply_scientific_function(function):
    try:
        value = float(expression.get())
        result = function(value)
        expression.set(str(result))
    except:
        expression.set("Error")


# ---------------- Toggle Scientific Mode ----------------
def toggle_mode():
    global scientific_mode

    if not scientific_mode:
        app.geometry("700x520")
        create_scientific_buttons()
        toggle_button.config(text="Normal Mode")
        scientific_mode = True
    else:
        app.geometry("380x520")
        remove_scientific_buttons()
        toggle_button.config(text="Scientific Mode")
        scientific_mode = False


# ---------------- Button Creator ----------------
def create_button(text, row, column, command, colspan=1):
    btn = tk.Button(
        app,
        text=text,
        font=("Arial", 16),
        command=command,
        bg="#34495e",
        fg="white",
        activebackground="#1abc9c",
        bd=0,
        padx=10,
        pady=15
    )
    btn.grid(row=row, column=column, columnspan=colspan,
             sticky="nsew", padx=5, pady=5)


# ---------------- Basic Buttons Layout ----------------
basic_buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('%',4,2), ('+',4,3),
]

for text, row, column in basic_buttons:
    if text == '%':
        create_button(text, row, column, calculate_percentage)
    else:
        create_button(text, row, column,
                      lambda t=text: add_value(t))

create_button("C", 5, 0, clear_display)
create_button("=", 5, 1, calculate, colspan=2)

toggle_button = tk.Button(
    app,
    text="Scientific Mode",
    font=("Arial", 14),
    command=toggle_mode,
    bg="#e67e22",
    fg="white",
    bd=0
)
toggle_button.grid(row=5, column=3, sticky="nsew", padx=5, pady=5)


# ---------------- Scientific Buttons ----------------
def create_scientific_buttons():
    functions = [
        ('sin', lambda: apply_scientific_function(math.sin)),
        ('cos', lambda: apply_scientific_function(math.cos)),
        ('tan', lambda: apply_scientific_function(math.tan)),
        ('log', lambda: apply_scientific_function(math.log10)),
        ('ln', lambda: apply_scientific_function(math.log)),
        ('√', lambda: apply_scientific_function(math.sqrt)),
        ('π', lambda: expression.set(str(math.pi))),
        ('x²', lambda: expression.set(str(float(expression.get())**2))),
    ]

    row = 1
    column = 4

    for text, cmd in functions:
        btn = tk.Button(
            app,
            text=text,
            font=("Arial", 15),
            command=cmd,
            bg="#16a085",
            fg="white",
            bd=0,
            padx=10,
            pady=15
        )
        btn.grid(row=row, column=column,
                 sticky="nsew", padx=5, pady=5)
        scientific_buttons.append(btn)

        row += 1
        if row > 4:
            row = 1
            column += 1


def remove_scientific_buttons():
    for btn in scientific_buttons:
        btn.destroy()
    scientific_buttons.clear()


# ---------------- Grid Configuration ----------------
for i in range(6):
    app.grid_rowconfigure(i, weight=1)

for i in range(6):
    app.grid_columnconfigure(i, weight=1)


# ---------------- Keyboard Bindings ----------------
app.bind("<Return>", calculate)
app.bind("<Escape>", clear_display)
app.bind("<BackSpace>", delete_last)


app.mainloop()
