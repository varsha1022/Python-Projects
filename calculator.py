import tkinter as tk

#create a main window
root = tk.Tk()
root.title("Calculator")

#entry widget to display the input and output
entry = tk.Entry(root,width = 20 ,font = ("Arial",20))
entry.grid(row = 0,column = 0,columnspan = 4)

#function to update the input field
def button_click(number):
    current = entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,current+str(number))
#function to clear the input field
def clear():
    entry.delete(0,tk.END)
#function to perform calculations
def Calculator():
    try:
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except Exception as e :
        entry.delete(0,tk.END)
        entry.insert(0,"ERROR")
#create calculator button
buttons  = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
]
row_val = 1
col_val = 0


for button in buttons:
    if button == "=":
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20), command=Calculator).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20), command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

#create a clear button
tk.Button(root, text="clear", padx=20, pady=20, font=("Arial", 20), command=clear, bg="lightgray", fg="white").grid(row=row_val, column=col_val, columnspan=4, padx=5, pady=5, ipadx=5, ipady=5)

root.mainloop()