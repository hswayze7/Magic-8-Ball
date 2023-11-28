import tkinter as tk
import random


def answer():
    random_response = str(random.randint(1,12))
    if random_response == 1:
        lbl_future["text"] = f"It is decidedly so"
    elif random_response == 2:
        lbl_future["text"] = f"Without a doubt"
    elif random_response == 3:
        lbl_future["text"] = f"Yes, definitely"
    elif random_response == 4:
        lbl_future["text"] = f"Ask again later"
    elif random_response == 5:
        lbl_future["text"] = f"My reply is no"
    elif random_response == 6:
        lbl_future["text"] = f"Very doubtful"




window = tk.Tk()
window.title("Magic Eight Ball.")
main_form = tk.Frame(master=window, width=150, height=150)
main_form.pack()
main_label = tk.Label(master=main_form, text="Magic Eight Ball Simulation")
main_label.pack()
main_label.grid(row=0, column=0)


label1 = tk.Label(master=main_form, text="What is your question?")
entry1 = tk.Entry(master=main_form, width=50)

label1.grid(row=1, column=0)
entry1.grid(row=1, column=1)


main_form_button = tk.Frame()
main_form_button.pack(fill=tk.X, ipadx=5, ipady=5)
button_Enter = tk.Button(master=main_form_button, text="Enter", command=answer)
button_Enter.pack(side=tk.RIGHT, padx=10, ipadx=10)
lbl_future = tk.Label(master=main_form, text="")
lbl_future.grid(row=2, column=0)

button_Clear = tk.Button(master=main_form_button, text = "Clear")
button_Clear.pack(side=tk.RIGHT, ipadx = 10)

events = []







window.mainloop()



