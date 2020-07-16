import model
import tkinter as tk

# Event handlers
def get_params():
    params = {
        "phone": entry.get(),
        "constant": constant_var.get()
    }
    return(params)

def execute():
    params = get_params()
    window.destroy()
    model.monitorMask(
        params["phone"],
        params["constant"]
    )

# Window components
window = tk.Tk(className="Mask Off - Start Options")
window.bg="#000080"

start_button = tk.Button(
    master=window,
    text="Start application",
    bg="#000080",
    highlightbackground="#000080",
    activebackground="#000080",
    activeforeground="#eeeeff",
    fg="white",
    height=2,
    width=20,
    command=execute
)

# User options
options = tk.Frame(
    master=window,
    bg="#000080"
)

label = tk.Label(
    master=options, 
    text="Enter your phone number",
    bg="#000080",
    fg="white"
)
entry = tk.Entry(master=options)

label.pack()
entry.pack()

constant_var = tk.BooleanVar()
constant_checkbox = tk.Checkbutton(
    master=options, 
    text="Remind me to wear a mask at my desk", 
    variable=constant_var
)
constant_checkbox.pack()

options.pack()
start_button.pack()

# Loop window until closed by execute function
window.mainloop()
