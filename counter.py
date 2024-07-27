import tkinter as tk

counter = 0

def countIncrement():
    global counter
    counter += 1
    counterLabel.config(text=str(counter))
    # print("Increment")
    return counter


def countDecrement():
    global counter
    counter -= 1
    counterLabel.config(text=str(counter))
    # print("Decrement")
    return counter


def countReset():
    global counter
    counter = 0
    counterLabel.config(text="0")
    # print("Reset")
    return counter

root = tk.Tk()
root.title = "Counter Application"
root.geometry("600x600")
root.configure(bg="black", bd=42)

labelHead = tk.Label(root, text="Counter Application", height=2, font="Helvetica 22 bold", bg="black", fg="white",relief="solid")
labelHead.pack(pady=(10, 20))

counterLabel = tk.Label(root, text="0", height=2, width=6, font="Arial 24 bold", fg="white", bg="gray",relief="solid")
counterLabel.pack(pady=(10, 20))

button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=(10, 30))

btn_style = {
    "height": 2,
    "width": 10,
    "bg": "gray",
    "fg": "white",
    "font": "Arial 14 bold",
    "relief": "solid",
    "activebackground": "gray",
    "activeforeground": "white",
    "cursor": "hand2"
}
incBtn = tk.Button(button_frame, text="Increment", command=countIncrement, **btn_style,)
incBtn.pack(side="left", padx=5)

decBtn = tk.Button(button_frame, text="Decrement", command=countDecrement, **btn_style)
decBtn.pack(side="left", padx=5)

resetBtn = tk.Button(button_frame, text="Reset", command=countReset, **btn_style)
resetBtn.pack(side="left", padx=5)

root.mainloop()